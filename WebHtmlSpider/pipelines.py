# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import time
import json
import os
from twisted.enterprise import  adbapi
from scrapy.conf import settings
from scrapy.exceptions import DropItem
import hashlib

class WebhtmlspiderPipeline(object):
    def process_item(self, item, spider):
        return item

#
#采集的网页源码存储为文件
#并且存储一个log
#
class JsonWritePipline(object):
    def __init__(self):
        self.logPath = 'json/' + time.strftime("%Y%m%d", time.localtime())
        self.logfilename =  self.logPath + '/'+time.strftime("%H", time.localtime())+'.log'
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath,0777)

    def process_item(self, item, spider):
        if 'url' in item and 'html' in item:
            nItem = dict(item)
            self.filename = nItem['filePath']
            with open(self.filename, 'a+') as f:
                f.writelines(nItem['html'])
            pass
        line = json.dumps(dict(item)['url']) + "\n"
        with open(self.logfilename, 'a+') as f:
            f.writelines(line)
        pass
        return item

    # 当spider被关闭时，这个方法被调用
    def close_spider(self, spider):
        line = time.strftime("%Y%m%d", time.localtime())+"==========================spider=====end==============================="+"\n"
        with open(self.logfilename, 'a+') as f:
            f.writelines(line)
        pass


#
#网页源码存储后并将其他信息和文件路径存储到sql
#删除字段中的源码
#
class  MongoPipeline(object):
    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        dbname = settings["MONGODB_DBNAME"]
        sheetname = settings["MONGODB_SHEETNAME"]
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[sheetname]
    def process_item(self, item, spider):
        if 'url' in item and 'html' in item:
            data = dict(item)
            query = {"urlId": data['urlId']}
            res = self.post.find_one(query)
            #判断是否已经查询过
            if not res:
                del data['html']
                self.post.insert(data)
        return item

    #爬虫开启事件  当spider被开启时，这个方法被调用。
    #从配置文件获取入口地址
    def open_spider(self, spider):
        with open("WebHtmlSpider/spiders/doMain.json", "r") as f:
            temp = json.loads(f.read())
            for url in temp['start_urls']:
                self.post.remove({"url": url})