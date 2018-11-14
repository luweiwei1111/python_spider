from .sql import Sql
from twisted.internet.threads import deferToThread
from securityfocus.items import SecurityfocusItem

class BidcvePipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        Sql.ctl_tb_bid_cve()
        if isinstance(item, SecurityfocusItem):    
            bid = item['bid']
            cve = item['cve']
            Sql.insert_bid_cve(bid, cve)
            print('开始保存bid_cve内容')