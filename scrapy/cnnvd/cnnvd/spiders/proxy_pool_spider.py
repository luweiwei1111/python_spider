# -*- coding:UTF-8 -*-
import re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from cnnvd.mysqlpipelines.sql import Sql
from cnnvd.items import CnnvdProxyItem
import requests
from lxml import etree

class My_proxy_spider(scrapy.Spider):

    name = 'proxy_pool'
    #http://ip.zdaye.com/dayProxy.html
    allowed_domains = ['ip.zdaye.com']
    base_url = 'http://ip.zdaye.com'
    bash_url = 'http://ip.zdaye.com/dayProxy.html'

    def start_requests(self):
        Sql.ctl_tb_ip_port_pool()
        url = self.bash_url
        print(url)
        yield Request(url, self.parse)

    def parse(self, response):
        #print(response.text)
        page_url = BeautifulSoup(response.text, 'lxml').find('div').find_all('a')#.find_all('a')#.find_all('a')#[0].attrs['value']
        #print(page_url)
        count = 0
        for num in range(0, len(page_url)):
            href_str = page_url[num].get('href')
            if '/dayProxy/ip' in href_str:
                ip_url = self.base_url + href_str
                count = count + 1
                if count == 10:
                    break
                print(ip_url)
                yield Request(ip_url, self.get_ip_detail)
    
    def get_ip_detail(self, response):
        item = CnnvdProxyItem()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        ip_pool = BeautifulSoup(response.text, 'lxml').find_all('div', class_='cont')
        ip_str = ''
        for i in range(0, len(ip_pool)):
            ip_str = ip_str + ip_pool[i].text

        ip_str = ip_str.replace('[', '').replace(']', '').replace(' ', '').replace('HTTP#', '').replace('HTTPS#', '').replace('(', '').replace(')', '')
        ip_str = re.sub(r'[A-Za-z]', '', ip_str)
        ip_str = re.sub(r'[^\x00-\x7f]', '', ip_str)


        list_ip = ip_str.split('@')
        succ_ip = []
        goodNum = 0
        badNum = 0
        for i in range(0, len(list_ip) - 1):
            #print('ip->' + proxy_host)
            try: 
                proxy_host = 'http://' + list_ip[i]
                proxies = {'http': proxy_host}
                response = requests.get('http://www.baidu.com', proxies=proxies, timeout=2)
                if response.status_code != 200:
                    badNum = badNum + 1
                    print(proxy_host + '->bad proxy')
                else: 
                    goodNum = goodNum + 1 
                    print(proxy_host + '->success proxy')
                    item['ip_port'] = list_ip[i]
                    yield item
            except Exception as e: 
                continue

        print('success proxy:' + str(goodNum))
        print('bad proxy:' + str(badNum))
        print('end')
