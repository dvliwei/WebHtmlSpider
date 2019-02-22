# -*- coding: utf-8 -*-

# Scrapy settings for WebHtmlSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WebHtmlSpider'

SPIDER_MODULES = ['WebHtmlSpider.spiders']
NEWSPIDER_MODULE = 'WebHtmlSpider.spiders'

# 设置爬虫持续多少秒后结束爬虫
CLOSESPIDER_TIMEOUT=0

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'WebHtmlSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 默认 Item 并发数：100
CONCURRENT_ITEMS = 100

#增加并发数
CONCURRENT_REQUESTS = 16

# 默认每个域名的并发数：8
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# 每个IP的最大并发数：0表示忽略
CONCURRENT_REQUESTS_PER_IP = 0

#爬去网站最大允许的深度如果是0则没有限制
DEPTH_LIMIT=2


# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Language': 'zh,en;q=0.9,ar;q=0.8,zh-CN;q=0.7,ja;q=0.6,zh-TW;q=0.5',
  'Cache-Control':'max-age=0',
  'Accept-Encoding':'gzip, deflate',
  'Upgrade-Insecure-Requests':'1'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'WebHtmlSpider.middlewares.WebhtmlspiderSpiderMiddleware': 543,
   'WebHtmlSpider.middlewares.AlbawabhnewsDownloaderMiddleware': None,
   'WebHtmlSpider.middlewares.MyUserAgentMiddleware': 300,
   'scrapy.contrib.spidermiddleware.offsite.OffsiteMiddleware': 500,

}

DOWNLOADER_MIDDLEWARES = {
    'WebHtmlSpider.middlewares.UrlFilter': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'WebHtmlSpider.middlewares.WebhtmlspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'WebHtmlSpider.pipelines.WebhtmlspiderPipeline': 300,
   'WebHtmlSpider.pipelines.JsonWritePipline': 300,
   'WebHtmlSpider.pipelines.MongoPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 301,
}
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_DBNAME = "WebHtmlUrl"
MONGODB_SHEETNAME = "articles"


MY_USER_AGENT = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 "
    "Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 "
    "Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; WindowHTTPCACHE_ENABLEDs NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR "
    "2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    ]


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True
LOG_LEVEL = 'INFO'

#这意味着该网站提供了原本只有ajax获取到的数据的纯HTML版本。 网站通过两种方法声明:
AJAXCRAWL_ENABLED = True

#广度优先
#深度优先是指网络爬虫会从起始页开始，一个链接一个链接跟踪下去，处理完这条线路之后再转入下一个起始页，继续追踪链接
#广度优先，有人也叫宽度优先，是指将新下载网页发现的链接直接插入到待抓取URL队列的末尾，也就是指网络爬虫会先抓取起始页中的所有网页，然后在选择其中的一个连接网页，继续抓取在此网页中链接的所有网页
#经过官方文档查询，因为scrapy使用的是后进先出队列，基本可以看成是深度优先（DFO）。如果需要设置广度优先（BFO），可以在settings中添加以下代码。另外当DEPTH_PRIORITY为正值时越靠广度优先，负值则越靠深度优先，默认值为0

DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#通过缓存实现增量式爬取（占据内存）
# 打开缓存
#HTTPCACHE_ENABLED = True

# 设置缓存过期时间（单位：秒）
#HTTPCACHE_EXPIRATION_SECS = 0

# 缓存路径(默认为：.scrapy/httpcache)
#HTTPCACHE_DIR = 'httpcache'

# 忽略的状态码
#HTTPCACHE_IGNORE_HTTP_CODES = []

# 缓存模式(文件缓存)
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# =====================scrapy-redis配置 =====================
# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# Ensure all spiders share same duplicates filter through redis.
#确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 调度状态持久化
SCHEDULER_PERSIST = True
# 请求调度使用优先队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
#指定连接到redis时使用的端口和地址（可选）
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
#REDIS_URL = 'redis://root:@127.0.0.1:6379'
#序列化项目管道作为redis Key存储
#REDIS_ITEMS_KEY = '%(spider)s:items'
#如果为True，则使用redis的'spop'进行操作。
#如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
#REDIS_START_URLS_AS_SET = True