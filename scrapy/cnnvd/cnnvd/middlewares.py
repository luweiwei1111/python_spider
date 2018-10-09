import random
from cnnvd.settings import IPPOOL
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip = ip

    def process_request(self, request, spider):
        thisip = random.choice(IPPOOL)
        print(thisip)
        request.meta["proxy"] = "http://"+thisip["ipaddr"]
