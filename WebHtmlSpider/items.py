# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#html  网页源码
#domain 域名
#status 状态
#url web地址
#urlId url  hash后
#time 时间戳
#filePath html存储路径
class WebhtmlspiderItem(scrapy.Item):
    url = scrapy.Field()
    urlId = scrapy.Field()
    domain = scrapy.Field()
    status = scrapy.Field()
    filePath = scrapy.Field()
    time = scrapy.Field()
    html = scrapy.Field()
    pass
