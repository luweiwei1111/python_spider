from cvedetails import settings
import sqlite3

SQLITE3_DB = settings.SQLITE3_DB

cnx = sqlite3.connect(SQLITE3_DB, check_same_thread = False)
cur = cnx.cursor()

class Sql:
    @classmethod
    def ctl_tb_cve_details(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cve_details( \
             product_id     TEXT NOT NULL,  \
             product_name   TEXT NOT NULL,  \
             year           TEXT NOT NULL,  \
             vul_type       TEXT,   \
             cve            TEXT NOT NULL);'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def ctl_tb_cve_detail_list(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cve_detail_list( \
             product_id     TEXT NOT NULL,  \
             product_name   TEXT NOT NULL,  \
             year           TEXT NOT NULL,  \
             vul_type       TEXT,   \
             cve            TEXT NOT NULL);'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def ctl_tb_product_details(cls):
        crt_tb_sql = 'CREATE TABLE if not exists product_details( \
             product_id        TEXT NOT NULL,  \
             product_name      TEXT NOT NULL,  \
             vendor_id         TEXT,   \
             PRIMARY KEY (product_id));'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def clr_cve_details(cls):
        clr_sql = 'delete from cve_details;'

        print(clr_sql)
        cur.execute(clr_sql)
        cnx.commit()

    @classmethod
    def clr_cve_detail_list(cls):
        clr_sql = 'delete from cve_detail_list;'

        print(clr_sql)
        cur.execute(clr_sql)
        cnx.commit()

    @classmethod
    def insert_cve_details(cls, product_id, product_name, year, vul_type, cve):
        sql = ''
        sql = 'INSERT INTO cve_details(product_id, product_name, year, vul_type, cve) VALUES( \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (product_id, product_name, year, vul_type, cve)

        print('+++++++开始保存数据+++++++')
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cve_details sql error:' + sql)
        cnx.commit()

    @classmethod
    def insert_cve_detail_list(cls, product_id, product_name, year, vul_type, cve):
        sql = ''
        sql = 'INSERT INTO cve_detail_list(product_id, product_name, year, vul_type, cve) VALUES( \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (product_id, product_name, year, vul_type, cve)

        print('+++++++开始保存数据+++++++')
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cve_detail_list sql error:' + sql)
        cnx.commit()

    @classmethod
    def insert_product_details(cls, product_id, product_name, vendor_id):
        sql = ''
        sql = 'INSERT INTO product_details(product_id, product_name, vendor_id) VALUES( \'%s\', \'%s\', \'%s\');' % (product_id, product_name, vendor_id)

        print('+++++++开始保存数据+++++++')
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert product_details sql error:' + sql)
        cnx.commit()

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")