# -*- coding: utf-8 -*-
import json
start_urls = []
allowed_domains=[]
with open("WebHtmlSpider/spiders/doMain.json", "r") as f :
    temp = json.loads(f.read())
    for url in temp['start_urls']:
        start_urls.append(str(url))

    for url in temp['allowed_domains']:
        allowed_domains.append(str(url))

print  start_urls