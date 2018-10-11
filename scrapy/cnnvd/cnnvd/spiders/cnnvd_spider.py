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
        Sql.ctl_tb_cve_cnnvd_cn()
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
                print('cnnvd->' + cnnvd + '数据爬取')
                yield Request(url, self.get_cnnvd_detail)

    def get_cnnvd_detail(self, response):
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        item = CnnvdItem()
        #print(response.text)
        
        ######1.CVE#############################################
        print('#1.cve编号:')
        cve_list = BeautifulSoup(response.text, 'lxml').find_all('a', href=re.compile("cve.mitre.org"))
        if len(cve_list) != 0:
            cve = cve_list[0].text.replace('\n', '').replace(' ', '')
        else:
            cve = 'null'
        print(cve)
        item['cve'] = cve

        ######2.language#############################################
        print('#2.language:cn')
        item['language'] = 'cn'

        ######3.name#############################################
        print('3.标题：')
        #/html/body/div[4]/div[1]/div/div[2]/h2/text()
        #/html/body/div[4]/div[1]/div/div[2]/h2/div
        selector = etree.HTML(response.text)
        title1 = selector.xpath('/html/body/div[4]/div[1]/div/div[2]/h2/text()')
        name = ''
        if len(title1) != 0:
            name = title1[0]
        
        title2 = selector.xpath('/html/body/div[4]/div[1]/div/div[2]/h2/div/text()')
        if len(title2) != 0:
            name = name + title2[0]
        print(name)
        item['name'] = name.replace('\n', '')

        ######4.cnnvd#############################################
        print('4.CNNVD编号：')
        cnnvd = ''
        span_list = BeautifulSoup(response.text, 'lxml').find_all('span')
        for i in range(0, len(span_list)):
            span_text = span_list[i].text
            if 'CNNVD编号：' in span_text:
                cnnvd = span_text.replace('CNNVD编号：', '')
                break
        print(cnnvd)
        if len(cnnvd) != 0:
            item['cnnvd'] = cnnvd
        else:
            print('#ERROR#cnnvd null')
            return

        ######5.publish_date#############################################
        print('5.发布日期：')
        publish_date = ''
        date_list = BeautifulSoup(response.text, 'lxml').find_all('a', href=re.compile("qstartdateXq"))
        if len(date_list) != 0:
            publish_date = date_list[0].text.replace(' ', '').replace('\n', '').replace('\t', '')
        else:
            print('#ERROR#publish_date null')
        print(publish_date)
        item['publish_date'] = publish_date

        ######6.update_date#############################################
        print('6.更新时间：')
        update_date = ''
        date_list = BeautifulSoup(response.text, 'lxml').find_all('a', href=re.compile("cvCnnvdUpdatedateXq"))
        if len(date_list) != 0:
            update_date = date_list[0].text.replace(' ', '').replace('\n', '').replace('\t', '')
        else:
            print('#ERROR#update_date null')
        print(update_date)
        item['update_date'] = update_date

        ######7.cvss_base#############################################
        #print(response.text)
        print('7.危害等级：')
        cvss_base = ''
        a_list = BeautifulSoup(response.text, 'lxml').find_all('a', onclick=re.compile("cvHazardRating"))
        print(a_list)
        if len(a_list) != 0:
            cvss_base = a_list[0].text.replace('\n', '').replace(' ', '')
        print(cvss_base)
        item['cvss_base'] = cvss_base

        ######8.vuldetect#############################################
        print('8.漏洞类型')
        vuldetect = ''
        a_list = BeautifulSoup(response.text, 'lxml').find_all('a', onclick=re.compile("cvVultype"))
        if len(a_list) != 0:
            vuldetect = a_list[0].text.replace('\n', '').replace(' ', '').replace('\t', '')
        print(vuldetect)
        item['vuldetect'] = vuldetect

        ######9.threat_type#############################################
        print('9.威胁类型：')
        threat_type = ''
        a_list = BeautifulSoup(response.text, 'lxml').find_all('a', onclick=re.compile("cvUsedStyle"))
        if len(a_list) != 0:
            threat_type = a_list[0].text.replace('\n', '').replace(' ', '').replace('\t', '')
        print(threat_type)
        item['threat_type'] = threat_type

        ######10.company#############################################
        print('10.厂商：')
        #/html/body/div[4]/div[1]/div/div[2]/ul/li[8]/a
        company = selector.xpath('/html/body/div[4]/div[1]/div/div[2]/ul/li[8]/text')#[0].text()
        print(company)
        item['company'] = 'company'

        ######11.summary#############################################
        print('11.漏洞简介：')
        summary = ''
        p_list = BeautifulSoup(response.text, 'lxml').find('div', class_='d_ldjj').find_all('p')
        if len(p_list) != 0:
            summary = p_list[0].text
        print(summary)
        item['summary'] = Sql.sqliteEscape(summary)
        len_p = len(p_list)
        print('len=' + str(len_p))

        ######12.solution#############################################
        print('12.漏洞公告：')
        solution = ''
        #p_list = BeautifulSoup(response.text, 'lxml').find('div', class_='d_ldjj').find_all('p')
        if len(p_list) >= 2:
            solution = p_list[1].text
        print(solution)
        item['solution'] = Sql.sqliteEscape(solution)

        ######13.xref#############################################
        print('13.参考网址：')
        xref = ''
        #p_list = BeautifulSoup(response.text, 'lxml').find('div', class_='d_ldjj').find_all('p')
        if len(p_list) >= 3:
            xref = p_list[2].text
        print(xref)
        item['xref'] = Sql.sqliteEscape(xref)

        ######14.affected#############################################
        print('14.影响实体')
        affected = ''
        a_list = BeautifulSoup(response.text, 'lxml').find_all('a', class_='a_title2')#.find_all('p')
        if len(a_list) != 0:
            affected = a_list[0].text
        print(affected)
        item['affected'] = Sql.sqliteEscape(affected)

        ######15.patch#############################################
        print('15.补丁：')
        #//*[@id="pat"]/p/text()
        #/html/body/div[4]/div/div[1]/div[7]/div[3]/text()
        patch_0 = selector.xpath('//*[@id="pat"]/p/text()')
        #print(patch)
        if len(patch_0) == 0:
            patch_1 = selector.xpath('/html/body/div[4]/div/div[1]/div[7]/div[3]/text()')
            if len(patch_1) == 0:
                patch = 'null'
            else:
                patch = patch_1[0]
        else:
            patch = patch_0[0]
        print(patch)
        item['patch'] = Sql.sqliteEscape(patch)

        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        return item