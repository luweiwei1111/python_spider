from securityfocus import settings
import sqlite3

SQLITE3_DB = settings.SQLITE3_DB

cnx = sqlite3.connect(SQLITE3_DB, check_same_thread = False)
cur = cnx.cursor()

class Sql:
    @classmethod
    def ctl_tb_bid_cve(cls):
        crt_tb_sql = 'CREATE TABLE if not exists bid_cve( \
             bid        TEXT NOT NULL,  \
             cve        TEXT);'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def insert_bid_cve(cls, bid, cve):
        sql = ''
        sql = 'INSERT INTO bid_cve(bid, cve) VALUES( \'%s\', \'%s\');' % (bid, cve)

        print('+++++++开始保存数据+++++++')
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert bid_cve sql error:' + sql)
        cnx.commit()

    @classmethod
    def select_ip_port_random(cls):
        sql = 'SELECT ip_port from ip_port_pool ORDER BY RANDOM () LIMIT 1;'
        #print(sql)
        cur.execute(sql)
        return cur.fetchall()[0]

    @classmethod
    def select_bid_cve_by_bid(cls, bid):
        sql = 'SELECT EXISTS(SELECT 1 FROM bid_cve WHERE bid= \'' + bid + '\');'
        print(sql)
        cur.execute(sql)
        return cur.fetchall()[0]

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")