# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


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
class CnnvdItem(scrapy.Item):
    # define the fields for your item here like:
    # 1.cve
    cve = scrapy.Field()
    # 2.language 'cn/en'
    language = scrapy.Field()
    # 3.name
    name = scrapy.Field()
    # 4.cnnvd
    cnnvd = scrapy.Field()
    # 5.publish_date
    publish_date = scrapy.Field()
    # 6.update_date
    update_date = scrapy.Field()
    # 7.cvss_base
    cvss_base = scrapy.Field()
    # 8.vuldetect
    vuldetect = scrapy.Field()
    # 9.threat_type
    threat_type = scrapy.Field()
    # 10.company
    company = scrapy.Field()
    # 11.summary
    summary = scrapy.Field()
    # 12.solution
    solution = scrapy.Field()
    # 13.xref
    xref = scrapy.Field()
    # 14.affected
    affected = scrapy.Field()
    # 15.patch
    patch = scrapy.Field()
    #pass

class CnnvdUrlItem(scrapy.Item):
    # define the fields for your item here like:
    # 1.cve
    cnnvd = scrapy.Field()
    # 2.language 'cn/en'
    url = scrapy.Field()
    # 3.name
    ok = scrapy.Field()
    #pass

class CnnvdProxyItem(scrapy.Item):
    # define the fields for your item here like:
    # 1.cve
    ip_port = scrapy.Field()