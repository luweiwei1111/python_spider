# -*- coding:UTF-8 -*-
import re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from cnnvd.items import CnnvdItem ##这是我定义的需要保存的字段，（导入cnnvd项目中，items文件中的CnnvdItem类)
from cnnvd.items import CnnvdUrlItem
from cnnvd.mysqlpipelines.sql import Sql
from lxml import etree

#from dingdian.items import DcontentItem
#from dingdian.mysqlpipelines.sql import Sql


class Myspider(scrapy.Spider):

    name = 'cnnvd'
    allowed_domains = ['cnnvd.org.cn']
    base_url = 'http://www.cnnvd.org.cn'
    bash_url = 'http://www.cnnvd.org.cn/web/vulnerability/querylist.tag'
    bashurl = '&repairLd='
    #num = 2
    #page_num = 11609

    def start_requests(self):
        #url = self.bash_url
        count_progress = 0
        url_list = Sql.select_url_list()
        for urls in url_list:
            count_progress = count_progress + 1
            print('############progress:' + str(count_progress))
            url = urls[0]  
            cnnvd = urls[0].split('=')[1]
            #查询url是否已经扫描成功
            ret = Sql.select_cnnvd(cnnvd)
            if ret[0] == 1:
                #print('cnnvd->' + cnnvd + '已经完成扫描,continue ...')
                continue
            else:
                print('cnnvd->' + cnnvd + '需要扫描')
                yield Request(url, self.get_cnnvd_detail)
    
    def get_cnnvd_detail(self, response):
        #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        item = CnnvdItem()

        selector = etree.HTML(response.text)
        #print('#####漏洞信息详情：')
        #print('#1 标题')
        vulnerability_details = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/h2/text()')[0].replace('\'', '\'\'')
        #print(vulnerability_details)
        item['name'] = vulnerability_details
        item['language'] = 'cn'

        #print('#1.1 CNNVD编号：')
        cnnvd_id = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[1]/span/text()')[0].replace('CNNVD编号：', '')
        print(cnnvd_id)
        item['cnnvd'] = cnnvd_id

        #print('#1.2 危害等级：')
        hazard_level = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[2]/a/text()')[0].replace('\n', '')
        #print(hazard_level)
        item['cvss_base'] = hazard_level

        #print('#1.3 CVE编号：')
        cve_id = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[3]/a/text()')[0].replace('\n', '').replace(' ', '')
        #print(cve_id)
        item['cve'] = cve_id

        #print('#1.4 漏洞类型：')
        vulnerability_type = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[4]/a/text()')[0].replace('\n', '').replace('\t', '')
        #print(vulnerability_type)
        item['vuldetect'] = vulnerability_type

        #print('#1.5 发布时间：')
        release_time = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[5]/a/text()')[0].replace('\n', '').replace('\t', '')
        #print(release_time)
        item['publish_date'] = release_time

        #print('#1.6 威胁类型：')
        threat_type = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[5]/a/text()')[0].replace('\n', '').replace('\t', '')
        #print(threat_type)
        item['threat_type'] = threat_type
        
        #print('#1.7 更新时间：')
        update_time = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[7]/a/text()')[0].replace('\n', '').replace('\t', '')
        #print(update_time)
        item['update_date'] = update_time

        #print('#1.8 厂商：')
        vendor = selector.xpath('/html/body/div[4]/div/div[1]/div[2]/ul/li[8]/text()')[0].replace('\n', '').replace('\'', '\'\'')
        #print(vendor)
        item['company'] = vendor

        #print('#1.9 漏洞来源：')
        #vulnerability_source = selector.xpath('//*[@id="1"]/text()')[0].replace('\'', '\'\'')
        #print(vulnerability_source)

        #print('#2 漏洞简介：')
        vul_source_1 = selector.xpath('/html/body/div[4]/div/div[1]/div[3]/p[1]/text()')[0].replace('\t', '').replace('\'', '\'\'')
        vul_source_2 = selector.xpath('/html/body/div[4]/div/div[1]/div[3]/p[2]/text()')#[0].replace('\t', '').replace('\'', '\'\'')
        if len(vul_source_2) == 0:
            print('vul_source_2 is null')
            vulnerability_summary = vul_source_1# + vul_source_2
        else:
            vulnerability_summary = vul_source_1 + vul_source_2[0].replace('\t', '').replace('\'', '\'\'')
        #print(vulnerability_summary)
        item['summary'] = vulnerability_summary

        #print('#3 漏洞公告：')
        vul_announcement_1 = selector.xpath('/html/body/div[4]/div/div[1]/div[4]/p[1]/text()')[0].replace('\t', '').replace('\'', '\'\'')
        vul_announcement_2 = selector.xpath('/html/body/div[4]/div/div[1]/div[4]/p[2]/text()')#[0].replace('\t', '').replace('\'', '\'\'')
        if len(vul_announcement_2) == 0:
            print('vul_announcement_2 is null')
            vulnerability_announcement = vul_announcement_1
        else:
            vulnerability_announcement = vul_source_1 + vul_announcement_2[0].replace('\t', '').replace('\'', '\'\'')
        #print(vulnerability_announcement)
        item['solution'] = vulnerability_announcement

        #print('#4 参考网址：')
        reference_source = selector.xpath('/html/body/div[4]/div/div[1]/div[5]/p[1]/text()')[0].replace('\t', '').replace('\'', '\'\'')
        reference_link = selector.xpath('/html/body/div[4]/div/div[1]/div[5]/p[2]/text()')#[0].replace('\t', '').replace('\'', '\'\'')
        if len(reference_link) == 0:
            reference_url = reference_source
        else:
            reference_url = reference_source + reference_link[0].replace('\t', '').replace('\'', '\'\'')
        #print(reference_url)
        item['xref'] = reference_url

        #print('#5 受影响实体：')
        vulnerability_entity = selector.xpath('/html/body/div[4]/div/div[1]/div[6]/div[3]/text()')#[0].replace('\n', '').replace('\t', '').replace('\'', '\'\'')
        if len(vulnerability_entity) == 0:
            item['affected'] = ' '
        else:
            #print(vulnerability_entity)
            item['affected'] = vulnerability_entity[0].replace('\n', '').replace('\t', '').replace('\'', '\'\'')

        #print('#6 补丁：')
        patch = selector.xpath('//*[@id="pat"]/p/text()')[0].replace('\n', '').replace('\t', '').replace('\'', '\'\'')
        #print(patch)
        item['patch'] = patch

        #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        return item