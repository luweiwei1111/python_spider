# -*- coding:UTF-8 -*-
import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from cvedetails.items import CvedetailsItem
from cvedetails.sqlitepiplines.sql import Sql
from lxml import etree
from cvedetails import settings

class Myspider(scrapy.Spider):

    name = 'fanyi_init'
    allowed_domains = ['translate.google.cn/']
    base_url = 'https://translate.google.cn/'

    def __init__(self):
        Sql.ctl_tb_cve_details()

    def start_requests(self):
        count = 0
        print('###base url:' + self.base_url)
        url = self.base_url
        yield Request(url, self.get_product_url)

    def get_product_url(self, response):
        #print(response.text)
        #获取url
        return
        """
        soup = BeautifulSoup(response.text, 'lxml')
        for vul_type in settings.TYPE_LIST:
            print('##########漏洞类别：' + vul_type)
            result_list = soup.find_all('a', 
                href=re.compile("/vulnerability-list/vendor_id"), 
                title=re.compile(settings.TYPE_DICT[vul_type]))
            for item in result_list:
                url = self.base_url + item['href']
                print(url)
                if 'year-' in url:
                    print(url)
                    yield Request(url, callback=self.get_cve_details_page)
                    """
