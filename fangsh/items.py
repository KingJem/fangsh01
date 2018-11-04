# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangshItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fangjia =scrapy.Field()
    huxing =scrapy.Field()
    chaoxing =scrapy.Field()
    daxiao =scrapy.Field()
    louceng =scrapy.Field()
    danjia =scrapy.Field()
    zhuangxiu =scrapy.Field()
    jiage     =scrapy.Field()