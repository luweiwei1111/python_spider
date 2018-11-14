from .sql import Sql
from twisted.internet.threads import deferToThread
from cvedetails.items import CvedetailsItem

class CvedetailsPipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        Sql.ctl_tb_cve_details()
        #Sql.ctl_tb_cve_detail_list()
        if isinstance(item, CvedetailsItem):    
            name = item['name']
            year = item['year']
            vul_type = item['vul_type']
            cve = item['cve']
            #sql = item['sql']
            Sql.insert_cve_details(name, year, vul_type, cve)
            print('开始保存cve details内容')