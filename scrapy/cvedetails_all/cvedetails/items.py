# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CvedetailsItem(scrapy.Item):
    # define the fields for your item here like:
    product_id = scrapy.Field()
    product_name = scrapy.Field()
    year = scrapy.Field()
    vul_type = scrapy.Field()
    cve = scrapy.Field()
    sql = scrapy.Field()