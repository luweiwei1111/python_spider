# -*- coding:UTF-8 -*-
import re
import scrapy #导入scrapy包
from bs4 import BeautifulSoup
from scrapy.http import Request ##一个单独的request的模块，需要跟进URL的时候，需要用它
from cnnvd.items import CnnvdItem ##这是我定义的需要保存的字段，（导入cnnvd项目中，items文件中的CnnvdItem类)
from cnnvd.items import CnnvdUrlItem
from cnnvd.mysqlpipelines.sql import Sql
from lxml import etree

class Myspider(scrapy.Spider):

    name = 'cnnvd_url'
    allowed_domains = ['cnnvd.org.cn']
    base_url = 'http://www.cnnvd.org.cn'
    bash_url = 'http://www.cnnvd.org.cn/web/vulnerability/querylist.tag'
    bashurl = '&repairLd='

    def start_requests(self):
        url = self.bash_url
        print(url)
        yield Request(url, self.parse)
        #yield Request('http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno=1&repairLd=', self.parse)

    def parse(self, response):
        """
        <input id="pagecount" name="pagecount" type="hidden" value="11581"/>
        获取总页数
        """
        #print(response.text)
        page_num = BeautifulSoup(response.text, 'lxml').find_all('input', id='pagecount')[0].attrs['value']
        print(page_num)
        print('###################page num=' + page_num)

        bashurl = self.bash_url
        max_num = int(page_num)
        #max_num = 2

        for num in range(1, int(max_num) + 1):
            if num == 1:
                url = bashurl
            else:
                url = bashurl + '?pageno=' + str(num) + self.bashurl
            print('##url:' + url)
            print('############progress:' + str(num))
            #查询url是否已经扫描成功
            ret = Sql.select_url(url)
            if ret[0] == 1:
                #print('url->' + url + '已经完成扫描，continue...')
                continue
            else:
                print('url->' + url + '需要解析')
                yield Request(url, callback=self.get_cnnvd_url)
                #yieid Request，请求新的URL，后面跟的是回调函数，你需要哪一个函数来处理这个返回值，就调用那一个函数，
                #返回值会以参数的形式传递给你所调用的函数。
                #

    def get_cnnvd_url(self, response):
        #print(response.text)
        item = CnnvdUrlItem()
        tds = BeautifulSoup(response.text, 'lxml').find_all('a', class_='a_title2', href=re.compile("ldxqById.tag"))
        #print('#####################################')
        count = 0
        for td in tds:
            #print(td)
            cnnvd_url = self.base_url + td.attrs['href']
            print(cnnvd_url)
            count = count  + 1
            #print('#########' + str(count) + '##############')
            #if count == 2:
            #    return
            cnnvd = cnnvd_url.split('=')[1]
            print('cnnvd=' + cnnvd)
            item['cnnvd'] = cnnvd
            item['url'] = cnnvd_url
            item['ok'] = '0'
            yield item