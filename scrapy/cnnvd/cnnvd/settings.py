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
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3551.3 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 设置下载延迟
# 原理：网站会通过我们对网页的访问频率进行分析，此时我们只需要控制一下爬行的时间间隔。
# DOWNLOAD_DELAY = 2

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
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

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
    {"ipaddr":"61.150.113.28:8908"},
    {"ipaddr":"27.208.82.98:8060"},
    {"ipaddr":"39.135.11.97:8080"},
    #{"ipaddr":"222.223.40.221:8060"},
    #{"ipaddr":"47.105.149.45:80"},
    #{"ipaddr":"60.217.154.47:8060"},
    #{"ipaddr":"175.9.160.154:8060"},
    #{"ipaddr":"39.135.9.231:8080"},
    #{"ipaddr":"47.105.146.225:80"},
]

"""
http://ip.zdaye.com/dayProxy/ip/133009.html
站大爷
47.105.144.119:80@HTTP#[透明]浙江省杭州市 阿里云
124.206.133.219:3128@HTTP#[透明]北京市 鹏博士长城宽带
61.150.113.28:8908@HTTP#[普匿]陕西省安康市 电信
27.208.82.98:8060@HTTP#[普匿]山东省威海市 联通
222.223.40.221:8060@HTTP#[普匿]河北省沧州市任丘市 电信
114.244.84.19:8060@HTTP#[普匿]北京市 联通
183.185.196.65:8060@HTTP#[未知]山西省太原市 联通
47.105.149.45:80@HTTP#[未知]浙江省杭州市 阿里云
58.87.86.75:3128@HTTP#[未知]浙江省温州市 广电网
186.233.199.154:53179@HTTP#[高匿]河南省鹤壁市 电信
60.217.154.47:8060@HTTP#[普匿]山东省威海市 联通
39.135.11.97:8080@HTTP#[普匿]北京市 移动
175.9.160.154:8060@HTTP#[普匿]湖南省长沙市 电信
123.138.89.133:9999@HTTP#[未知]陕西省西安市 联通
47.105.146.225:80@HTTP#[透明]浙江省杭州市 阿里云
39.135.9.231:8080@HTTP#[普匿]北京市 移动
183.63.90.98:8060@HTTP#[普匿]广东省广州市 电信
114.223.161.10:8118@HTTP#[普匿]江苏省无锡市江阴市 电信
121.8.98.198:80@HTTP#[高匿]广东省广州市 电信
113.121.240.116:808@HTTP#[未知]山东省德州市 电信
27.208.225.176:8060@HTTP#[普匿]山东省威海市 联通
118.89.164.175:8080@HTTP#[普匿]天津市滨海新区 腾讯云华北数据中心
171.221.239.11:808@HTTP#[透明]四川省成都市 电信
47.105.147.231:80@HTTP#[透明]浙江省杭州市 阿里云
47.105.146.135:80@HTTP#[透明]浙江省杭州市 阿里云
47.105.147.167:80@HTTP#[未知]浙江省杭州市 阿里云
223.223.187.195:80@HTTP#[高匿]北京市 中关村数据中心
183.215.206.39:53281@HTTP#[未知]湖南省 移动
47.105.150.187:80@HTTP#[未知]浙江省杭州市 阿里云
27.208.191.50:8060@HTTP#[普匿]山东省威海市荣成市 联通
45.239.137.9:48729@HTTP#[高匿]浙江省 电信中心网络
39.135.10.98:80@HTTP#[普匿]北京市 移动
165.138.225.250:8080@HTTP#[透明]陕西省西安市 联通
47.105.146.220:80@HTTP#[未知]浙江省杭州市 阿里云
121.40.138.161:8000@HTTP#[普匿]浙江省杭州市 阿里巴巴网络有限公司BGP数据中心
185.22.174.69:1448@HTTP#[透明]江苏省镇江市 电信
104.248.113.238:8080@HTTP#[透明]中国
120.92.118.127:8080@HTTP#[普匿]北京市 北京金山云网络技术有限公司
113.91.66.9:9797@HTTP#[未知]广东省深圳市 电信
47.105.147.164:80@HTTP#[透明]浙江省杭州市 阿里云
181.54.251.14:21231@HTTP#[未知]浙江省 电信中心网络
39.135.9.165:80@HTTP#[普匿]北京市 移动
173.212.219.151:3128@HTTP#[透明]江苏省南通市 BurstNET网络公司
218.59.139.238:80@HTTP#[普匿]山东省潍坊市 联通
218.60.8.99:3129@HTTP#[透明]辽宁省沈阳市 联通
47.105.147.175:80@HTTP#[透明]浙江省杭州市 阿里云
39.135.11.94:80@HTTP#[普匿]北京市 移动
114.55.236.62:3128@HTTP#[透明]浙江省杭州市 阿里云BGP数据中心
88.99.149.188:31288@HTTP#[普匿]山东省滨州市 联通
27.154.240.222:8060@HTTP#[普匿]福建省厦门市 电信
39.135.10.163:8080@HTTP#[普匿]北京市 移动
119.180.128.249:8060@HTTP#[普匿]山东省 联通
60.217.140.18:8060@HTTP#[普匿]山东省威海市 联通
73.218.245.138:80@HTTP#[高匿]浙江省温州市 电信
118.144.149.206:3128@HTTP#[透明]北京市 鹏博士长城宽带
222.76.74.114:808@HTTP#[未知]福建省福州市 电信
60.217.140.86:8060@HTTP#[普匿]山东省威海市 联通
47.105.150.158:80@HTTP#[未知]浙江省杭州市 阿里云
47.95.34.224:9898@HTTP#[透明]北京市 阿里云
118.190.200.139:8080@HTTP#[普匿]北京市 八方电信工程(集团)有限公司
27.208.69.190:8060@HTTP#[普匿]山东省威海市荣成市 联通
140.143.96.216:80@HTTP#[透明]中国
39.135.9.102:80@HTTP#[普匿]北京市 移动
60.217.143.20:8060@HTTP#[普匿]山东省威海市 联通
183.230.179.157:8060@HTTP#[普匿]重庆市 移动
177.92.228.130:8090@HTTP#[透明]浙江省嘉兴市嘉善县 电信
123.57.76.102:80@HTTP#[普匿]北京市 阿里云BGP数据中心
111.38.88.218:53281@HTTP#[未知]安徽省 移动
222.186.45.117:63359@HTTP#[普匿]江苏省镇江市 电信
112.247.200.126:8060@HTTP#[普匿]山东省威海市 联通
39.134.68.10:80@HTTP#[透明]北京市 移动
27.203.214.192:8060@HTTP#[普匿]山东省威海市 联通
61.50.96.62:8080@HTTP#[未知]北京市 联通
219.157.147.115:8118@HTTP#[普匿]河南省郑州市 联通
183.230.179.164:8060@HTTP#[普匿]重庆市 移动
221.2.174.99:8060@HTTP#[普匿]山东省威海市 联通
61.167.82.196:80@HTTP#[普匿]黑龙江省绥化市 洋洋网吧
185.2.82.23:1080@HTTP#[未知]浙江省杭州市 阿里云
190.14.158.12:42703@HTTP#[高匿]河南省商丘市 电信
128.199.208.65:8080@HTTP#[透明]江苏省南京市 电信
119.190.187.120:8060@HTTP#[普匿]山东省 联通
210.1.58.213:8080@HTTP#[高匿]浙江省杭州市 阿里云
218.56.124.137:8060@HTTP#[普匿]山东省威海市 联通
120.78.215.151:808@HTTP#[普匿]浙江省杭州市 阿里云BGP数据中心
60.212.243.12:8060@HTTP#[普匿]山东省威海市 联通
89.37.56.138:8080@HTTP#[透明]浙江省 电信中心网络
123.114.203.109:8118@HTTP#[普匿]北京市 联通
119.180.174.221:8060@HTTP#[普匿]山东省 联通
47.105.150.239:80@HTTP#[未知]浙江省杭州市 阿里云
39.135.10.104:8080@HTTP#[普匿]北京市 移动
47.104.221.159:80@HTTP#[未知]山东省青岛市 阿里云
39.135.10.165:8080@HTTP#[普匿]北京市 移动
112.91.218.21:9000@HTTP#[未知]广东省广州市 联通
119.135.178.66:8060@HTTP#[普匿]广东省清远市 电信
222.140.53.63:8888@HTTP#[未知]河南省许昌市禹州市 联通
115.159.31.195:8080@HTTP#[普匿]上海市 腾讯云
111.11.98.58:9000@HTTP#[未知]河北省 移动
47.52.90.137:80@HTTP#[普匿]广东省东莞市 电信
39.135.11.165:8080@HTTP#[普匿]北京市 移动
"""
