from .sql import Sql
from twisted.internet.threads import deferToThread
from cnnvd.items import CnnvdItem
from cnnvd.items import CnnvdUrlItem

"""
             cve              TEXT NOT NULL,  'cve'
             language         TEXT NOT NULL,  'cn/en'
             name             TEXT,   '标题'
             cnnvd            TEXT,   'cnnvd'
             publish_date     TEXT,   '发布时间'
             update_date      TEXT,   '更新时间'
             cvss_base        TEXT,   '危害等级'
             vuldetect        TEXT,   '危害类型'
             threat_type      TEXT,   '威胁类型'
             company          TEXT,   '厂商'
             summary          TEXT,   '漏洞简介'
             solution         TEXT,   '漏洞公告'
             xref             TEXT,   '参考网址'
             affected         TEXT,   '影响实体'
             patch            TEXT,   '补丁'
"""

class CnnvdPipeline(object):

    def process_item(self, item, spider):
        #deferToThread(self._process_item, item, spider)
        Sql.ctl_tb_cve_cnnvd_cn()
        if isinstance(item, CnnvdItem):
            cnnvd = item['cnnvd']
            ret = Sql.select_cnnvd(cnnvd)
            if ret[0] == 1:
                print('cnnvd->' + cnnvd + '已经存在了')
                pass
            else:
                cve = item['cve']
                language = item['language']
                name = item['name']
                cnnvd = item['cnnvd']
                publish_date = item['publish_date']
                update_date = item['update_date']
                cvss_base = item['cvss_base']
                vuldetect = item['vuldetect']
                threat_type = item['threat_type']
                company = item['company']
                summary = item['summary']
                solution = item['solution']
                xref = item['xref']
                affected = item['affected']
                patch = item['patch']
                Sql.insert_cve_cnnvd_cn(cve, language, name, cnnvd, publish_date, update_date, cvss_base, vuldetect, threat_type, company, summary, solution, xref, affected, patch)
                print('开始保存cnnvd内容')

        if isinstance(item, CnnvdUrlItem):
            Sql.ctl_tb_cnnvd_url()
            url = item['url']
            ret = Sql.select_url(url)
            if ret[0] == 1:
                print('url->' + url + '已经存在了')
                pass
            else:
                cnnvd = item['cnnvd']
                ok = item['ok']
                Sql.insert_cnnvd_url(cnnvd, url, ok)
                print('开始保存cnnvd url')
                return item
