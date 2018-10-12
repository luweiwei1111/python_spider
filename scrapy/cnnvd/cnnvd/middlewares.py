import random
from cnnvd.settings import IPPOOL
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware
from cnnvd.mysqlpipelines.sql import Sql

class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        #thisip = random.choice(IPPOOL)
        thisip = Sql.select_ip_port_random()
        thisip = str(thisip).replace('(', '').replace(')', '').replace(',', '').replace('\'', '')
        print('ip=' + thisip)
        #request.meta["proxy"] = "http://"+ thisip["ipaddr"]
        request.meta["proxy"] = "http://"+ thisip
