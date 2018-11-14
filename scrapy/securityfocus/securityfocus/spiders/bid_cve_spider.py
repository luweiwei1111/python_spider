# -*- coding:UTF-8 -*-
import re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request
from securityfocus.items import SecurityfocusItem
from securityfocus.sqlitepiplines.sql import Sql
from lxml import etree

class Myspider(scrapy.Spider):

    name = 'cvebid'
    allowed_domains = ['securityfocus.com']
    base_url = 'https://www.securityfocus.com'
    start_url = 'https://www.securityfocus.com/bid'

    def start_requests(self):
        url = self.start_url
        print(url)
        yield Request(url, self.get_page_max)

    def get_page_max(self, response):
        #获取最大页数
        soup = BeautifulSoup(response.text, 'lxml')
        max_page = soup.find('span', class_="pages").text.split('(')[1].split(')')[0].replace('Page 1 of ', '')
        print(max_page)
        #https://www.securityfocus.com/cgi-bin/index.cgi?o=300&l=30&c=12&op=display_list&vendor=&version=&title=&CVE=
        url_head = 'https://www.securityfocus.com/cgi-bin/index.cgi?o='
        url_tail = '&l=30&c=12&op=display_list&vendor=&version=&title=&CVE='
        #for i in range(1, 3):
        for i in range(1, int(max_page)):
            print('i=' + str(i))
            o_num = 30 * i
            url = url_head + str(o_num) + url_tail
            #print(url)
            yield Request(url, self.get_bid_url)

    def get_bid_url(self, response):
        #<a href="/bid/105912">http://www.securityfocus.com/bid/105912</a>
        #获取每个url链接
        soup = BeautifulSoup(response.text, 'lxml')
        bid_url_list = soup.find_all('a', 
            href=re.compile("/bid/"), 
            text=re.compile("http://www.securityfocus.com/bid/"))
        print('##############################################')
        for item in bid_url_list:
            url = item.text
            print(url)
            yield Request(url, self.get_bid_cve_details)

    def get_bid_cve_details(self, response):
        item = SecurityfocusItem()
        soup = BeautifulSoup(response.text, 'lxml')

        #1.bid
        """
        <tr>
            <td>
                <span class="label">Bugtraq ID:</span> 
            </td>
            <td>
                105912
            </td>
        </tr>
        """
        bid = soup.find('span', 
            class_='label',
            text="Bugtraq ID:").find_next().text.replace('\n', '').replace('\r', '').replace('\t', '').replace(' ', '')
        print('##bid[' + bid + ']')
        item['bid'] = bid

        #2.cve
        """
        <tr valign="top">
            <td>
                <span class="label">CVE:</span> 
            </td>
            <td>
                
                    CVE-2018-15767<br>
                 
            </td>
        </tr>
        """
        cve_list = soup.find('span', 
            class_='label',
            text="CVE:").find_next().text.replace('\r', '').replace('\t', '').replace(' ', '')
        count_n = 0
        if len(cve_list) != 0:
            for cve_char in cve_list:
                if '\n' in cve_char:
                    count_n = count_n + 1
        if count_n > 3:
            cve = cve_list[2:].replace('\n\n', ',').replace('\n', '')
        else:
            cve = cve_list.replace('\n', '')
        print('##cve[' + cve + ']')
        item['cve'] = cve

        return item

