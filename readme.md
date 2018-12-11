##深度采集部署文档

### 部署文档
```angular2html
git clone  https://github.com/dvliwei/WebHtmlSpider.git  WebHtmlSpider

cd WebHtmlSpider

mkdir json

chmod -R 777 json

```

### mongo数据库部署
```db2
use WebHtmlUrl
db.createCollection("articles")
db.articles.ensureIndex({"urlId":1},{"unique":1})
db.articles.find({})
db.articles.count()
db.articles.remove()
```

### crontab 定时任务设置
````exasol
0 * * * * scrapy crawl web >> example.log 2>&1 &

```