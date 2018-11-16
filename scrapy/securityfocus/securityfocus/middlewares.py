# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from securityfocus.settings import IPPOOL
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from securityfocus.sqlitepiplines.sql import Sql

class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        #thisip = random.choice(IPPOOL)
        thisip = Sql.select_ip_port_random()
        thisip = thisip[0]
        #thisip = str(thisip).replace('(', '').replace(')', '').replace(',', '').replace('\'', '')
        print('ip=' + thisip)
        #request.meta["proxy"] = "http://"+ thisip["ipaddr"]
        request.meta["proxy"] = "http://"+ thisip
