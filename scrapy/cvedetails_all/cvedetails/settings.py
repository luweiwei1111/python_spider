# -*- coding: utf-8 -*-

# Scrapy settings for cvedetails project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'cvedetails'

SPIDER_MODULES = ['cvedetails.spiders']
NEWSPIDER_MODULE = 'cvedetails.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cvedetails (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.randint(3, 5)
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'cvedetails.middlewares.CvedetailsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
    #'cvedetails.middlewares.MyCustomDownloaderMiddleware': 543,
    #'cvedetails.middlewares.middleware.JavaScriptMiddleware': 543, #键为中间件类的路径，值为中间件的顺序
    #'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None, #禁止内置的中间件
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    #'cvedetails.pipelines.CvedetailsPipeline': 300,
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'cvedetails.middlewares.middleware.MyUserAgentMiddleware': 400,
    'cvedetails.sqlitepiplines.pipelines.CvedetailsPipeline': 1,
}


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MY_USER_AGENT = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]


#for sqlite3 db settings
SQLITE3_DB = 'cvedetails.db'

#for input excel data
ExcelSettingsFileName = 'cvedetails/plugins_data/excel/重点应用分类.xlsx'

#for output excel report data
ExcelReportFileName = 'cvedetails/plugins_data/excel/插件移植报告.xls'
ExcelReportSheetName = '移植详情'

#for plugins path
Topvas_PATH = 'cvedetails/plugins_data/topvas'
Nessus_PATH = 'cvedetails/plugins_data/ness_desc'

#for cvedetails dict
TYPE_DICT_CN = {
            'opdos': '1拒绝服务',
            'opec': '2代码执行',
            'opov': '3溢出',
            'opmemc': '4内存崩溃',
            'opsqli': '5sql注入',
            'opxss': '6跨站脚本攻击',
            'opdirt': '7目录遍历',
            'ophttprs': '8http拆分攻击',
            'opbyp': '9绕过',
            'opginf': 'a信息收集',
            'opgpriv': 'b权限获取',
            'opcsrf': 'c跨站请求伪造',
            'opfileinc': 'd文件包含',
            'of exploits': 'e漏洞利用量'
            }

TYPE_DICT_EN = {
            'opdos': '1opdos',
            'opec': '2opec',
            'opov': '3opov',
            'opmemc': '4opmemc',
            'opsqli': '5opsqli',
            'opxss': '6opxss',
            'opdirt': '7opdirt',
            'ophttprs': '8ophttprs',
            'opbyp': '9opbyp',
            'opginf': 'aopginf',
            'opgpriv': 'bopgpriv',
            'opcsrf': 'copcsrf',
            'opfileinc': 'dopfileinc',
            'of exploits': 'eof exploits'
            }

TYPE_LIST =[
            'dos',
            'Code Execution',
            'Overflow',
            'Memory Corruption',
            'Sql Injection',
            'XSS',
            'Directory Traversal',
            'Http Response Splitting',
            'Bypass something',
            'Gain Information',
            'Gain Privileges',
            'CSRF',
            'File Inclusion',
            'of exploits',
            ]
    
#漏洞类型列表
TYPE_DICT = {
            'dos': 'Denial of service vulnerabilities for',                                   #1.拒绝服务
            'Code Execution': 'Code execution vulnerabilities for',                           #2.代码执行
            'Overflow': 'Overflow vulnerabilities for',                                       #3.溢出
            'Memory Corruption': 'Memory corruption vulnerabilities for',                     #4.内存崩溃
            'Sql Injection': 'Sql injection vulnerabilities for',                             #sql注入
            'XSS': 'Cross site scripting vulnerabilities for',                                #5.跨站脚本攻击
            'Directory Traversal': 'Directory traversal vulnerabilities for',                 #6.目录遍历
            'Http Response Splitting': 'Http response splitting vulnerabilities for',         #http拆分攻击
            'Bypass something': 'By pass a restriction or similar type vulnerabilities for',  #7.绕过
            'Gain Information': 'Information gain, leak vulnerabilities for',                 #8.信息收集
            'Gain Privileges': 'Privilege gain, elevation vulnerabilities for',               #9,权限获取
            'CSRF': 'Cross site request forgery, CSRF, vulnerabilities for',                  #10.跨站请求伪造
            'File Inclusion': 'File inclusion vulnerabilities for',                           #文件包含
            'of exploits': 'Total number of public exploits'                                  #11.漏洞利用量
            }



WIN_LIST = {
            '11366',		#windows server 2008
            '17153',		#windows 7
            '9591',			#windows vista
            '23546',		#windows server 2012
            '739',			#windows xp
            '26434',		#windows 8.1
            '32238',		#windows 10
            '26435',		#windows Rt8.1
            '107',			#windows 2000
            '34965',		#windows server 2016
            '2594',			#woindows 2003 server
           }


LINUX_LIST = {
        #########SUSE
            '92',		    #Suse Linux
            '18579',		#Linux Enterprise Server
            '9575',	        #Linux Enterprise Desktop
            '34242',		#Linux Enterprise
            '33566',        #Linux Enterprise Software Development Kit
            '11168',        #Opensuse
        #########MAC OS X
            '9325',         #MAC OS X
        #########FreeBAS
            '7',            #FreeBSD
        #########Debian
            '1251',         #Debian
        #########RedHat
            '79',           #Enterprise Linux Desktop
            '78',           #Enterprise Linux
            '24639',        #Enterprise Linux Server
            '24640',        #Enterprise Linux Workstation
            '25167',        #Enterprise Linux Server Eus
            '38',           #Linux
            '25627',        #Openstack
        ########OpenSuse
            '14195',        #OpenSuse
            '40865',        #Leap
            '33567',        #Evergreen
        ########Ubuntu
            '20550',        #Canonical Ubuntu Linux
            '80',           #Ubuntu Ubuntu Linux
        ########CentOS
            '18131',        #CentOS
           }

DB_LIST = {
            '3671',		    #Oracle 10g
            '404',		    #Oracle 8i
            '1427',			#Oracle 9i
            '14516',		#Oracle Database
            '3424',			#DB2
            '251',		    #Sql Server
            '316',		    #Mysql
            '21801',		#MySQL
           }

Openssh_LIST = {
            '585',          #Openssh
            '383',          #Openssl-Openssl
            '3966',         #readhat-Openssl
            '13982',        #openssl project-Openssl
            '30688',        #libressl
            }

Virtualization_LIST = {
        #########Hadoop
            '22215',         #Apache-Hadoop
            '22217',         #Cloudera-Hadoop
        #########Zookeeper
            '27453',         #Apache-Zookeeper
        #########Esxi
            '14180',         #Vmware-Esxi-App
            '22134',         #Vmware-Esxi-Os
        #########Xen
            '12196',         #Xensource-Inc-XEN
            '12750',         #XEN-XEN-App
            '14092',         #Xensource-XEN
            '15065',         #Citrix-XEN
            '23463',         #XEN-XEN-Os 
        #########Xenserver
            '14577',         #Citrix-Xenserver-App 
            '48142',         #Citrix-Xenserver-Os
        ########Vmware
            '6560',          #Vmware-ACE
            '14181',         #Vmware-ESX-App 
            '22176',         #Vmware-ESX-Os 
            '14147',         #Vmware-Fusion
            '35455',         #Vmware-Horizon
            '6561',          #Vmware-Player
            '7928',          #Vmware-Server
            '28398',         #Vmware-Tools
            '20517',         #Vmware-Vcenter-Server 
            '23748',         #Vmware-Vcenter-Server-Appliance
            '22135',         #Vmware-View
            '9264',          #Vmware-Virtualcenter
            '12342',         #Vmware-Vmware-Player
            '12343',         #Vmware-Vmware-Server
            '12155',         #Vmware-Vmware-Workstation 
            '33501',         #Vmware-Vrealize-Automation
            '436',           #Vmware-Workstation
            '34392',         #Vmware-Workstation-Player
            '34391',         #Vmware-Workstation-Pro
           }

Vendor_LIST = {
            '16',            #cicso
            '874',           #Juniper
            '5979',          #Huawei
            '315',           #q=F5
            '11971',         #q=ZTE
            '136',           #q=Checkpoint
            '3080',          #Fortinet
            '15054',         #q=Hillstone+Software
             }


DEVICES_LIST = {
            '25464',         #HP-H3c-High-Performance
            '25334',         #Huawei-H3c-Ar
            '25461',         #HP-H3c-Ethernet
            '24230',         #HP-A7506-Switch-Chassis
            '25463',         #HP-H3c-Processing
            '25465',         #HP-H3c-Processor-
            '25462',         #HP-H3c-Router
            '25459',         #HP-H3c-Routing
            '25460',         #HP-H3c-Switch
            '24530',         #HP-Msr5040
            '24549',         #HP-Rt-msr2020-ac
            }

APPS_P_LIST = {
            '3436',         #IIS
            }

APPS_V_LIST = {
            '45',            #Apache
            }

#https://www.cvedetails.com/vendor-search.php?search=%25apache%25
#https://www.cvedetails.com/product-search.php?vendor_id=0&search=%25weblogic%25
APPS_SPD_LIST = {
            #'weblogic',         #weblogic
            #'websphere',        #websphere
            #'tomcat',           #tomcat
            'adobe',            #adobe
            #'screenos',         #screenos
            #'sendmail',         #sendmail
            #'silverlight',      #Silverlight
            #'skype',            #skype
            'firefox',          #firefox
            }

DEVICES_SVD_LIST = {
            'cisco',            #cisco
            }

PRODUCT_DICT = {
            #'product-os_win': WIN_LIST,              #windows操作系统(左世涛)
            #'product-os_linux': LINUX_LIST,          #linux操作系统(裴杰)
            #'product-bigdata': Virtualization_LIST,  #大数据组件(唐逸群)
            #'product-apps': APPS_P_LIST,             #应用中间件(卢伟伟)product
            #'vendor-apps': APPS_V_LIST,              #应用中间件(卢伟伟)vendor
            'search-pd-apps': APPS_SPD_LIST,          #应用中间件(卢伟伟) 关键字搜索(根据product产品搜索)
            #'product-db': DB_LIST,                   #数据库(裴杰)
            #'product-devices': DEVICES_LIST,         #网络设备(廖成杰)
            'search-vd-devices': DEVICES_SVD_LIST,    #应用中间件(卢伟伟) 关键字搜索(根据product产品搜索)
            #'vendor-device': Vendor_LIST,            #Cisco
            }