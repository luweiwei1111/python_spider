# -*- coding:UTF-8 -*-
import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from cvedetails.items import CvedetailsItem
from cvedetails.sqlitepiplines.sql import Sql
from lxml import etree

class Myspider(scrapy.Spider):

    name = 'cvedetails'
    allowed_domains = ['cvedetails.com']
    base_url = 'https://www.cvedetails.com'
    #bash_url = 'https://www.cvedetails.com/product/11366/?q=Windows+Server+2008'
    """
    https://www.cvedetails.com/product/11366/Microsoft-Windows-Server-2008.html?vendor_id=26   -> windows server 2008
    https://www.cvedetails.com/product/17153/Microsoft-Windows-7.html?vendor_id=26             -> windows 7
    https://www.cvedetails.com/product/9591/Microsoft-Windows-Vista.html?vendor_id=26          -> windows vista
    https://www.cvedetails.com/product/23546/Microsoft-Windows-Server-2012.html?vendor_id=26   -> windows server 2012
    https://www.cvedetails.com/product/739/Microsoft-Windows-Xp.html?vendor_id=26              -> windows xp
    https://www.cvedetails.com/product/26434/Microsoft-Windows-8.1.html?vendor_id=26           -> windows 8.1
    https://www.cvedetails.com/product/32238/Microsoft-Windows-10.html?vendor_id=26            -> windows 10
    https://www.cvedetails.com/product/26435/Microsoft-Windows-Rt-8.1.html?vendor_id=26        -> windows Rt8.1
    https://www.cvedetails.com/product/107/Microsoft-Windows-2000.html?vendor_id=26            -> windows 2000
    https://www.cvedetails.com/product/34965/Microsoft-Windows-Server-2016.html?vendor_id=26   -> windows server 2016
    https://www.cvedetails.com/product/2594/Microsoft-Windows-2003-Server.html?vendor_id=26    -> woindows 2003 server
    """

    #操作系统列表
    os_list = [
            'windows server 2008', 
            'windows 7', 
            'windows vista', 
            'windows server 2012',
            'windows xp',
            'windows 8.1',
            'windows 10',
            'windows Rt8.1',
            'windows 2000',
            'windows server 2016',
            'woindows 2003 server']

    #操作系统对应的product id
    os_dict = {
            'windows server 2008': '11366', 
            'windows 7': '17153', 
            'windows vista': '9591', 
            'windows server 2012': '23546',
            'windows xp': '739',
            'windows 8.1': '26434',
            'windows 10': '32238',
            'windows Rt8.1': '26435',
            'windows 2000': '107',
            'windows server 2016': '34965',
            'woindows 2003 server': '2594',
            }

    type_list =[
            'dos',
            'Code Execution',
            'Overflow',
            'Memory Corruption',
            'XSS',
            'Directory Traversal',
            'Bypass something',
            'Gain Information',
            'Gain Privileges',
            'CSRF',
            'of exploits'
            ]
    
    #漏洞类型列表
    type_dict = {
            'dos': 'Denial of service vulnerabilities for',                                   #1.拒绝服务
            'Code Execution': 'Code execution vulnerabilities for',                           #2.代码执行
            'Overflow': 'Overflow vulnerabilities for',                                       #3.溢出
            'Memory Corruption': 'Memory corruption vulnerabilities for',                     #4.内存崩溃
            'Sql Injection': 'Sql injection vulnerabilities for',                             #sql注入  ->NA
            'XSS': 'Cross site scripting vulnerabilities for',                                #5.跨站脚本攻击
            'Directory Traversal': 'Directory traversal vulnerabilities for',                 #6.目录遍历
            'Http Response Splitting': 'Http response splitting vulnerabilities for',         #http拆分攻击  -->NA
            'Bypass something': 'By pass a restriction or similar type vulnerabilities for',  #7.绕过
            'Gain Information': 'Information gain, leak vulnerabilities for',                 #8.信息收集
            'Gain Privileges': 'Privilege gain, elevation vulnerabilities for',               #9,权限获取
            'CSRF': 'Cross site request forgery, CSRF, vulnerabilities for',                  #10.跨站请求伪造
            'File Inclusion': '',                                                             #文件包含  -->NA
            'of exploits': 'Total number of public exploits'                                  #11.漏洞利用量
            }

    type_dict_cn = {
            'opdos': '1拒绝服务',
            'opec': '2代码执行',
            'opov': '3溢出',
            'opmemc': '4内存崩溃',
            'opsqli': '5sql注入',
            'opxss': '6跨站脚本攻击',
            'opdirt': '7目录遍历',
            'ophttprs': '8http拆分攻击',
            'opbyp': '9绕过',
            'opginf': 'a信息收集',
            'opgpriv': 'b权限获取',
            'opcsrf': 'c跨站请求伪造',
            'opfileinc': 'd文件包含',
            'of exploits': 'e漏洞利用量'
            }

    year_list = {'2000', '2001', '2002', '2003', '2004', 
                 '2005', '2006', '2007', '2008', '2009', 
                 '2010', '2011', '2012', '2013', '2014',
                 '2015', '2016', '2017', '2018'}

    def start_requests(self):
        #url = self.base_url
        count = 0
        print(self.base_url)
        for os in self.os_list:
            url = self.base_url + '/product/' + self.os_dict[os]
            count = count + 1
            print('url->' + url)
            yield Request(url, self.parse)

    def parse(self, response):
        #print(response.text)
        #获取url
        Sql.ctl_tb_cve_detail_list()
        soup = BeautifulSoup(response.text, 'lxml')
        for vul_type in self.type_list:
            print('##########' + vul_type)
            result_list = soup.find_all('a', 
                href=re.compile("/vulnerability-list/vendor_id-26/product_id-"), 
                title=re.compile(self.type_dict[vul_type]))
            for item in result_list:
                url = self.base_url + item['href']
                #print(url)
                if 'year-' in url:
                    print(url)
                    yield Request(url, callback=self.get_cve_details_page)


    def get_cve_details_page(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        page_list = soup.find_all('a', title = re.compile('Go to page '))
        #print('############################################')
        for item in page_list:
            page_url = self.base_url + item['href']
            print('page url:' + page_url)
            yield Request(page_url, callback=self.get_cve_details_url)

    def get_cve_details_url(self, response):
        item = CvedetailsItem()
        soup = BeautifulSoup(response.text, 'lxml')
        
        #1.name        TEXT NOT NULL
        result_list = soup.find_all('a', 
                href=re.compile("//www.cvedetails.com/product"))
        
        name = result_list[0].text
        item['name'] = name

        print('1.操作系统：' + item['name'])

        #2.year        TEXT NOT NULL
        result_list = soup.find_all('a', title = re.compile('Go to page '))

        vul_type_list = result_list[0]['href'].split('&')
        print(vul_type_list)
        year = ''
        for value in vul_type_list:
            if 'year=' in value:
                year = value.split('=')[1]
                break

        item['year'] = year
        print('2.年份：' + item['year'])

        #3.vul_type    TEXT
        vul_type = ''
        for value in vul_type_list:
            if '=1' in value and 'op' in value:
                vul_type = value.split('=')[0]
                break
        
        if vul_type == '':
            print('#ERROR# vul_type is null')
            vul_type ='of exploits'

        vul_type = self.type_dict_cn[vul_type]
        item['vul_type'] = vul_type
        print('3.漏洞类别：' + item['vul_type'])

        #4.cve         TEXT NOT NULL
        cve_list = soup.find_all('a',
                href=re.compile("/cve/CVE"))
        #print(cve_list)
        print('4.cve：')
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
            Sql.insert_cve_detail_list(name, year, vul_type, cve.text)
        
        return item
