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

    @classmethod
    def sql_execute(cls, sql):
        print(sql)
        cur.execute(sql)
        return cur.fetchall()

    @classmethod
    def select_nvts_ness_by_cve(cls, cve):
        sql = 'SELECT file from nvts_ness where cve like \'%%%s%%\'' % (cve)
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_nvts_topvas_by_cve(cls, cve):
        sql = 'SELECT file from nvts_nons where cve like \'%%%s%%\'' % (cve)
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_cve_detail_list(cls):
        # sql = 'SELECT product_id, product_name, year, vul_type, cve from cve_detail_list limit 5;'
        sql = 'SELECT product_id, product_name, year, vul_type, cve from cve_detail_list ;'
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_from_cve_report(cls):
        sql = 'SELECT * from cve_report ;'
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def ctl_tb_cve_report(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cve_report( \
            product_id          TEXT, \
            product_name        TEXT NOT NULL, \
            year                TEXT NOT NULL, \
            vul_type            TEXT NOT NULL, \
            cve                 TEXT NOT NULL, \
            openvas_file        TEXT, \
            openvas_exist       TEXT, \
            topvas_ness_file    TEXT, \
            nessus_file         TEXT, \
            nessus_exist        TEXT, \
            ts_file             TEXT, \
            ts_count            TEXT)'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def cls_tb_cve_report(cls):
        sql = 'delete from cve_report;'

        print(sql)
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def drop_tb_cve_report(cls):
        sql = 'drop table if exists cve_report;'

        print(sql)
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def ctl_index_nvts_ness(cls):
        index_list = {
            #'CREATE INDEX nvts_ness_by_creation_time ON nvts_ness (creation_time);',
            #'CREATE INDEX nvts_ness_by_cvss_base ON nvts_ness (cvss_base);',
            #'CREATE INDEX nvts_ness_by_family ON nvts_ness (family);',
            #'CREATE INDEX nvts_ness_by_modification_time ON nvts_ness (modification_time);'
            #'CREATE INDEX nvts_ness_by_name ON nvts_ness (name);',
            #'CREATE INDEX nvts_ness_by_oid ON nvts_ness (oid);',
            #'CREATE INDEX nvts_ness_by_solution_type ON nvts_ness (solution_type);',
            'CREATE INDEX nvts_ness_by_cve ON nvts_ness(cve);',
            'CREATE INDEX nvts_by_cve ON nvts(cve);',
            'CREATE INDEX nvts_by_file ON nvts (file );'
            }
        for sql in index_list:
            print(sql)
            try:
                cur.execute(sql)
            except:
                print('#ERROR#create index sql error:' + sql)
        cnx.commit()

    @classmethod
    def insert_cve_report(cls, product_id, product_name, year, vul_type, cve, openvas_file, openvas_exist, topvas_ness_file, nessus_file, nessus_exist, ts_file, ts_count):
        sql = ''
        sql = 'INSERT INTO cve_report VALUES( \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (product_id, product_name, year, vul_type, cve, openvas_file, openvas_exist, topvas_ness_file,  nessus_file, nessus_exist, ts_file, ts_count)

        #print('+++++++开始保存数据+++++++')
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cve_report sql error:' + sql)
        cnx.commit()

    @classmethod
    def select_tb_cve_report(cls, product_name):
        sql = 'select  nessus_file, topvas_file from cve_report where openvas_exist = \'no\' and nessus_exist= \'yes\' and product_name = \'%s\';' %(product_name)

        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_tb_cve_report_by_product_name(cls):
        sql = 'select distinct product_name from cve_report ;'

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def ctl_tb_settings(cls):
        crt_tb_sql = 'CREATE TABLE if not exists settings( \
            category          TEXT NOT NULL, \
            product_name      TEXT NOT NULL, \
            product_id        TEXT, \
            vendor_id         TEXT, \
            product_search    TEXT NOT NULL, \
            vendor_search     TEXT NOT NULL, \
            owner             TEXT NOT NULL)'

        print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def ctr_tb_settings(cls):
        sql = 'delete from settings'

        print(sql)
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def insert_tb_settings(cls, category, product_name, product_id, vendor_id, product_search, vendor_search, owner):
        sql = 'insert into settings VALUES(\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (category, product_name, product_id, vendor_id, product_search, vendor_search, owner)

        print(sql)
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def select_from_settings_by_product(cls):
        sql = 'select product_id from settings where product_search = \'no\' and vendor_search = \'no\' and product_id != \'None\';'
        #sql = 'select product_id from settings where product_search = \'no\' and vendor_search = \'no\' and product_id != \'None\' limit 1;'

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_from_settings_by_vendor(cls):
        sql = 'select vendor_id from settings where product_search = \'no\' and vendor_search = \'no\' and vendor_id != \'None\' and product_id = \'None\';'
        #sql = 'select vendor_id from settings where product_search = \'no\' and vendor_search = \'no\' and vendor_id != \'None\' and product_id = \'None\' limit 1;'

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_from_settings_by_s_product(cls):
        sql = 'select product_search from settings where product_search != \'no\' and vendor_search = \'no\';'
        #sql = 'select product_search from settings where product_search != \'no\' and vendor_search = \'no\' limit 1;'
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_from_settings_by_s_vendor(cls):
        sql = 'select vendor_search from settings where product_search = \'no\' and vendor_search != \'no\';'
        #sql = 'select vendor_search from settings where product_search = \'no\' and vendor_search != \'no\' limit 1;'

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def ctl_tb_nvts_nons(cls):
        crt_tb_sql = 'CREATE TABLE IF NOT EXISTS nvts_nons( \
                 "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
                 plugin_id       TEXT NOT NULL, \
                 cve             TEXT NOT NULL, \
                 file            TEXT NOT NULL);'

        print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()
    
    @classmethod
    def drop_tb_nvts_nons(cls):
        crt_tb_sql = 'drop table nvts_nons;'

        print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def ctl_index_nvts_nons(cls):
        index_list = {
            'CREATE INDEX nvts_nons_by_oid ON nvts_nons (oid);',
            'CREATE INDEX nvts_nons_by_cve ON nvts_nons(cve);',
            }
        for sql in index_list:
            print(sql)
            try:
                cur.execute(sql)
            except:
                print('#ERROR#create index sql error:' + sql)
        cnx.commit()
    
    @classmethod
    def insert_nvts_nons(cls):
        sql = 'insert into nvts_nons select * from nvts where file not like \'ns_%%.nasl\';'
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#create index sql error:' + sql)
        cnx.commit()

    @classmethod
    def select_nvts_by_file(cls, ns_file):
        sql = 'SELECT EXISTS(SELECT 1 FROM nvts WHERE file = \'%s\');' % (ns_file)
        #print(sql)
        cur.execute(sql)
        return cur.fetchall()[0]

    @classmethod
    def ctl_tb_plugins(cls, plugins_table):
        sql = 'CREATE TABLE IF NOT EXISTS %s( \
                 "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, \
                 plugin_id       TEXT NOT NULL, \
                 cve             TEXT NOT NULL, \
                 file            TEXT NOT NULL);' %(plugins_table)

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#create nvts sql error:' + sql)
        cnx.commit()

    @classmethod
    def cls_tb_plugins(cls, plugins_table):
        sql = 'delete from %s;' %(plugins_table)
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#delete sql error:' + sql)
        cnx.commit()

    @classmethod
    def insert_plugins(cls, plugins_table, plugin_id, cve, file):
        sql = 'insert into %s(plugin_id, cve, file) values(\'%s\', \'%s\', \'%s\');' %(plugins_table, plugin_id, cve, file)

        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert sql error:' + sql)
        cnx.commit()

    @classmethod
    def delete_XX_nasl(cls):
        del_sql = {
            'delete from nvts where file like \'XX_%%.nasl\';',
            'delete from nvts_ness where file like \'XX_%%.nasl\';'
            }
        for sql in del_sql:
            print(sql)
            try:
                cur.execute(sql)
            except:
                print('#ERROR#sql error:' + sql)
        cnx.commit()