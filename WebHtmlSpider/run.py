# -*- coding: utf-8 -*-
# 一个文件管理所有爬虫

import scrapy

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class Aljarida24MaSpider(scrapy.Spider):
    # Your first spider definition
    name = 'aljarida24.ma'

class AlweeamComSaSpider(scrapy.Spider):
    # Your first spider definition
    name = 'alweeam.com.sa'

configure_logging()
runner = CrawlerRunner()
runner.crawl(Aljarida24MaSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())