# -*- coding: utf-8 -*-

# Scrapy settings for cnnvd project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'cnnvd'

SPIDER_MODULES = ['cnnvd.spiders']
NEWSPIDER_MODULE = 'cnnvd.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/62.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置下载延迟
# 原理：网站会通过我们对网页的访问频率进行分析，此时我们只需要控制一下爬行的时间间隔。
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 01-禁止Cookie
# 原理：网站会通过Cookie信息对用户进行识别和分析，此时如果我们禁止本地Cookie信息让对方网站无法识别出我们的会话信息。
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cnnvd.middlewares.CnnvdSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'cnnvd.middlewares.CnnvdDownloaderMiddleware': 543,
#}
DOWNLOADER_MIDDLEWARES = {
   #'qianmu.middlewares.MyCustomDownloaderMiddleware': 543,
    #'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':123,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware':123,
    'cnnvd.middlewares.IPPOOLS':125,
    #'cnnvd.uamid.Uamid':1
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'cnnvd.pipelines.CnnvdPipeline': 300,
    'cnnvd.mysqlpipelines.pipelines.CnnvdPipeline': 1,
}

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
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#for mysql settings
MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '12345678'
MYSQL_PORT = '3306'
MYSQL_DB = 'spider'

#for sqlite3 settings
SQLITE3_DB = 'cnnvd.db'

# 设置IP池
IPPOOL = [
    #{"ipaddr":"47.105.144.119:80"},
    #{"ipaddr":"47.95.50.158:80"},
    #{"ipaddr":"47.94.230.42:9999"},
    #{"ipaddr":"47.106.122.223:8888"},
    #50|120.78.215.151:808
    {"ipaddr":"221.2.174.28:8060"},
    {"ipaddr":"39.137.140.13:8080"},
    {"ipaddr":"121.46.95.27:8080"},
    {"ipaddr":"58.240.53.194:8080"},
    {"ipaddr":"39.137.141.142:8080"}
    #{"ipaddr":"175.9.160.154:8060"},
    #{"ipaddr":"39.135.9.231:8080"},
    #{"ipaddr":"47.105.146.225:80"},
]

"""
http://ip.zdaye.com/dayProxy/ip/133009.html
站大爷
"""
