from cvedetails import settings
import sqlite3

SQLITE3_DB = settings.SQLITE3_DB

cnx = sqlite3.connect(SQLITE3_DB, check_same_thread = False)
cur = cnx.cursor()

class Sql:
    @classmethod
    def ctl_tb_cve_details(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cve_details( \
             name        TEXT NOT NULL,  \
             year        TEXT NOT NULL,  \
             vul_type    TEXT,   \
             cve         TEXT NOT NULL);'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def ctl_tb_cve_detail_list(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cve_detail_list( \
             name        TEXT NOT NULL,  \
             year        TEXT NOT NULL,  \
             vul_type    TEXT,   \
             cve         TEXT NOT NULL);'

        print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def insert_cve_details(cls, name, year, vul_type, cve):
        sql = ''
        sql = 'INSERT INTO cve_details(name, year, vul_type, cve) VALUES( \'%s\', \'%s\', \'%s\', \'%s\');' % (name, year, vul_type, cve)

        print('+++++++开始保存数据+++++++')
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cve_details sql error:' + sql)
        cnx.commit()

    @classmethod
    def insert_cve_detail_list(cls, name, year, vul_type, cve):
        sql = ''
        sql = 'INSERT INTO cve_detail_list(name, year, vul_type, cve) VALUES( \'%s\', \'%s\', \'%s\', \'%s\');' % (name, year, vul_type, cve)

        print('+++++++开始保存数据+++++++')
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cve_detail_list sql error:' + sql)
        cnx.commit()

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")