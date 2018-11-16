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

    name = 'cvedetails-all'
    allowed_domains = ['cvedetails.com']
    base_url = 'https://www.cvedetails.com'
    exten_url = 'https://www.cvedetails.com/product-list.php'

    """
    https://www.cvedetails.com/product/11366   -> windows server 2008
    """

    def start_requests(self):
        count = 0
        url = self.base_url + '/product-list.php'
        print('###base url:' + url)
        yield Request(url, self.parse)

    def parse(self, response):
        #创建表
        Sql.ctl_tb_product_details()
        Sql.ctl_tb_cve_detail_list()

        #获取所以的page页href
        soup = BeautifulSoup(response.text, 'lxml')
        page_list = soup.find_all('a', title="Next Page-List of software or hardware products")

        count = 0
        for item in page_list:
            #count = count + 1
            #if count == 2:
            #    return
            page_url = self.base_url + item['href']
            print(page_url)
            yield Request(page_url, self.get_product_id)

    def get_product_id(self, response):
        #获取最大的product id
        soup = BeautifulSoup(response.text, 'lxml')
        href_url = soup.find_all('a',
            href=re.compile("//www.cvedetails.com/product/"),
            title=re.compile("Product Details"))
        print('#####################################')
        for url in href_url:
            print(url['href'])
            page_detail_list = url['href'].split('/')
            product_id = page_detail_list[4]
            product_name = Sql.sqliteEscape(page_detail_list[5].split('?')[0].replace('.html', ''))
            vendor_id = page_detail_list[5].split('?')[1].replace('vendor_id=', '')
            #print('product_id=%s, product_name=%s, vendor_id=%s' % (product_id, product_name, vendor_id))
            Sql.insert_product_details(product_id, product_name, vendor_id)
            product_url = self.base_url + '/product/' + product_id
            print('#####product_url:' + product_url)
            yield Request(product_url, self.get_product_url)

    def get_product_url(self, response):
        #print(response.text)
        #获取url
        Sql.ctl_tb_cve_detail_list()
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

    def get_cve_details_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        page_list = soup.find_all('a', title = re.compile('Go to page '))
        print('############################################')
        for item in page_list:
            page_url = self.base_url + item['href']
            print('page url:' + page_url)
            yield Request(page_url, callback=self.get_cve_details_url)

    def get_cve_details_url(self, response):
        item = CvedetailsItem()
        soup = BeautifulSoup(response.text, 'lxml')

        #1.product_id        TEXT NOT NULL
        result_list = soup.find_all('a', title = re.compile('Go to page '))

        vul_type_list = result_list[0]['href'].split('&')
        print(vul_type_list)
        product_id = ''
        for value in vul_type_list:
            if 'product_id=' in value:
                product_id = value.split('=')[1]
                break

        item['product_id'] = product_id
        print('1.产品ID：' + item['product_id'])

        #2.product_name        TEXT NOT NULL
        product_list = soup.find_all('a', 
                href=re.compile("//www.cvedetails.com/product"))
        
        product_name = Sql.sqliteEscape(product_list[0].text)
        item['product_name'] = product_name
        print('2.操作系统：' + item['product_name'])

        #3.year TEXT NOT NULL
        #print(vul_type_list)
        year = ''
        for value in vul_type_list:
            if 'year=' in value:
                year = value.split('=')[1]
                break

        item['year'] = year
        print('3.年份：' + item['year'])

        #3.vul_type    TEXT
        vul_type = ''
        for value in vul_type_list:
            if '=1' in value and 'op' in value:
                vul_type = value.split('=')[0]
                break
        
        if vul_type == '':
            print('#ERROR# vul_type is null')
            vul_type ='of exploits'

        vul_type = settings.TYPE_DICT_CN[vul_type]
        item['vul_type'] = vul_type
        print('4.漏洞类别：' + item['vul_type'])

        #4.cve         TEXT NOT NULL
        cve_list = soup.find_all('a',
                href=re.compile("/cve/CVE"))
        #print(cve_list)
        print('5.cve：')
        cve_all = ''
        count = 0
        for cve in cve_list:
            count = count + 1
            if count == 1:
                cve_all = cve_all + cve.text
            else:
                cve_all = cve_all + ',' + cve.text
        item['cve'] = cve_all
        print('###' + item['cve'])

        for cve in cve_list:
            Sql.insert_cve_detail_list(product_id, product_name, year, vul_type, cve.text)
        
        return item