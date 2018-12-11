# -*- coding: utf-8 -*-
import scrapy
import re
import os
import hashlib
import  time
import json
import urllib
from scrapy.spiders import CrawlSpider ,Rule
from scrapy.linkextractors import LinkExtractor
from WebHtmlSpider.items import WebhtmlspiderItem

class WebSpider(CrawlSpider):

    name = 'web'
    #allowed_domains = ['3a2elaty.com']
    #start_urls = ['https://3a2elaty.com/']

    #
    #重写入口
    #
    def __init__(self, group=None, *args, **kwargs):
        super(WebSpider, self).__init__(*args, **kwargs)
        start_urls = []
        allowed_domains = []
        with open("WebHtmlSpider/spiders/doMain.json", "r") as f:
            temp = json.loads(f.read())
            for url in temp['start_urls']:
                start_urls.append(str(url))
            for url in temp['allowed_domains']:
                allowed_domains.append(str(url))

        self.start_urls = start_urls
        self.allowed_domains = allowed_domains


    rules = (
        # 提取匹配 'category.php' (但不匹配 'subsection.php') 的链接并跟进链接(没有callback意味着follow默认为True)
        #Rule(LinkExtractor(allow=('3a2elaty.com',)), callback='parse_item', follow=True),
        # 提取匹配 'item.php' 的链接并使用spider的parse_item方法进行分析
        Rule(LinkExtractor(allow=('.*',)), callback='parse_item', follow=True),
    )

    def parse_item(self,response):
        item = WebhtmlspiderItem()
        item['url'] = response.url
        urlId = hashlib.md5(response.url).hexdigest();
        item['urlId'] = urlId
        str = response.url.split('/')[2].strip()
        host = str.split('.')[-2].strip()
        suffix = str.split('.')[-1].strip()
        doMain = host+"."+suffix
        item['domain'] = doMain
        item['status'] = 0
        item['time'] = time.time()
        item['html'] = response.body
        self.htmlPath = 'json/' + time.strftime("%Y%m%d", time.localtime())+'/' + time.strftime("%H", time.localtime())+'/'
        if not os.path.exists(self.htmlPath):
            os.makedirs(self.htmlPath,0777)
        item['filePath'] = self.htmlPath+urlId+".html"
        yield item