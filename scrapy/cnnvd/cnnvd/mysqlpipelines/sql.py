#import pymysql.connector
#import pymysql
from cnnvd import settings
import sqlite3

"""
MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
"""
SQLITE3_DB = settings.SQLITE3_DB

#cnx = pymysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
#cnx = pymysql.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
#cur = cnx.cursor(buffered=True)
#cur = cnx.cursor()
cnx = sqlite3.connect(SQLITE3_DB, check_same_thread = False)
cur = cnx.cursor()
"""
CREATE TABLE cve_cnnvd_cn(
             cve              TEXT NOT NULL,  'cve'
             language         TEXT NOT NULL,  'cn/en'
             name             TEXT,   '标题'
             cnnvd            TEXT,   'cnnvd'
             publish_date     TEXT,   '发布时间'
             update_date      TEXT,   '更新时间'
             cvss_base        TEXT,   '危害等级'
             vuldetect        TEXT,   '危害类型'
             threat_type      TEXT,   '威胁类型'
             company          TEXT,   '厂商'
             summary          TEXT,   '漏洞简介'
             solution         TEXT,   '漏洞公告'
             xref             TEXT,   '参考网址'
             affected         TEXT,   '影响实体'
             patch         TEXT,
             PRIMARY KEY (cve));
"""

class Sql:
    @classmethod
    def ctl_tb_cve_cnnvd_cn(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cve_cnnvd_cn( \
             cve              TEXT NOT NULL,  \
             language         TEXT NOT NULL,  \
             name             TEXT,   \
             cnnvd            TEXT,   \
             publish_date     TEXT,   \
             update_date      TEXT,   \
             cvss_base        TEXT,   \
             vuldetect        TEXT,   \
             threat_type      TEXT,   \
             company          TEXT,   \
             summary          TEXT,   \
             solution         TEXT,   \
             xref             TEXT,   \
             affected         TEXT,   \
             patch            TEXT,   \
             PRIMARY KEY (cnnvd));'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()
    
    @classmethod
    def ctl_tb_cnnvd_url(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cnnvd_url( \
             cnnvd            TEXT NOT NULL,  \
             url              TEXT NOT NULL,  \
             ok               TEXT,   \
             PRIMARY KEY (url));'
        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def insert_cve_cnnvd_cn(cls, cve, language, name, cnnvd, publish_date, update_date, cvss_base, vuldetect, threat_type, company, summary, solution, xref, affected, patch):
        sql = ''
        #sql = "INSERT INTO cve_cnnvd_cn(cve, language, name, cnnvd, publish_date, update_date, cvss_base, vuldetect, threat_type, company, summary, solution, xref, affected, patch)  " + \
        sql = 'INSERT INTO cve_cnnvd_cn VALUES( \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (cve, language, name, cnnvd, publish_date, update_date, cvss_base, vuldetect, threat_type, company, summary, solution, xref, affected, patch)
        
        print('+++++++开始保存数据+++++++' + cnnvd)
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cve_cnnvd_cn sql error:' + sql)
        cnx.commit()

    @classmethod
    def insert_cnnvd_url(cls, cnnvd, url, ok):
        sql = "INSERT INTO cnnvd_url(cnnvd, url, ok)  VALUES(" + \
            "'" + cnnvd + "'," + \
            "'" + url + "'," + \
            "'" + ok + "');"
    
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cnnvd_url sql error:' + sql)
        cnx.commit()

    @classmethod
    def select_name(cls, name):
        sql = 'SELECT EXISTS(SELECT 1 FROM cve_cnnvd_cn WHERE name= \'' + name + '\');'
        print(sql)
        cur.execute(sql)
        return cur.fetchall()[0]

    @classmethod
    def select_cve(cls, cve):
        sql = 'SELECT EXISTS(SELECT 1 FROM cve_cnnvd_cn WHERE cve= \'' + cve + '\');'
        print(sql)
        cur.execute(sql)
        return cur.fetchall()[0]

    @classmethod
    def select_cnnvd(cls, cnnvd):
        sql = 'SELECT EXISTS(SELECT 1 FROM cve_cnnvd_cn WHERE cnnvd= \'' + cnnvd + '\');'
        #print(sql)
        cur.execute(sql)
        return cur.fetchall()[0]

    @classmethod
    def select_url(cls, url):
        sql = 'SELECT EXISTS(SELECT 1 FROM cnnvd_url WHERE url= \'' + url + '\');'
        #print(sql)
        cur.execute(sql)
        return cur.fetchall()[0]

    @classmethod
    def select_url_list(cls):
        #select t1.cnnvd_url from cnnvd_url t1 where not exists (select * from cve_cnnvd_cn t2 where t1.cnnvd = t2.cnnvd)
        #sql = 'select t1.url from cnnvd_url t1 where not exists (select * from cve_cnnvd_cn t2 where t1.cnnvd = t2.cnnvd);'
        #sql = 'select url from cnnvd_url order by url LIMIT 200;'
        sql = 'select url from cnnvd_url ;'#where cnnvd = \'CNNVD-201810-491\';'
        #print(sql)
        cur.execute(sql)
        return cur.fetchall()

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")