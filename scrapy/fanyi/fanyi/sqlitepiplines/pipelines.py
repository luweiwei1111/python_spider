from .sql import Sql
from twisted.internet.threads import deferToThread
from fanyi.items import FanyiItem

class FanyiPipeline(object):

    def process_item(self, item, spider):
        Sql.ctl_tb_cve_details()

        if isinstance(item, FanyiItem):
            product_id = item['product_id']
            product_name = item['product_name']
            year = item['year']
            vul_type = item['vul_type']
            cve = item['cve']

            Sql.insert_cve_details(product_id, product_name, year, vul_type, cve)
            print('开始保存cve details内容')