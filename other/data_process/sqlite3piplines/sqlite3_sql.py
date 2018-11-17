# coding=utf-8
import sqlite3

cnx = sqlite3.connect('topvas_nvts.db')
cur = cnx.cursor()

class Sql:
    @classmethod
    def sql_execute(cls, sql):
        print(sql)
        cur.execute(sql)
        return cur.fetchall()

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")

    @classmethod
    def select_nvts_ness_by_id(cls, nvt_id):
        sql = 'SELECT file from nvts_ness where oid = \'%s\'' % (nvt_id)
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_nvts_topvas_by_id(cls, nvt_id):
        sql = 'SELECT file from nvts where oid = \'%s\'' % (nvt_id)
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_cve_detail_list(cls):
        # sql = 'SELECT product_id, product_name, year, vul_type, cve from cve_detail_list limit 5;'
        sql = 'SELECT product_id, product_name, year, vul_type, cve from cve_detail_list;'
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_nvt_cves_by_cve(cls, cve_name):
        sql = 'SELECT oid from nvt_cves where cve_name = \'%s\'' % (cve_name)

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def select_nvt_ness_cves_by_cve(cls, cve_name):
        sql = 'SELECT oid from nvt_ness_cves where cve_name = \'%s\'' % (cve_name)

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def ctl_tb_cve_report(cls):
        crt_tb_sql = 'CREATE TABLE if not exists cve_report( \
            product_id          TEXT NOT NULL, \
            product_name        TEXT NOT NULL, \
            year                TEXT NOT NULL, \
            vul_type            TEXT NOT NULL, \
            cve                 TEXT NOT NULL, \
            topvas_file         TEXT, \
            topvas_exist        TEXT, \
            nessus_file         TEXT, \
            nessus_exist        TEXT, \
            PRIMARY KEY (product_name,year, vul_type,cve) )'

        print(crt_tb_sql)
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
            'CREATE INDEX nvts_ness_by_creation_time ON nvts_ness (creation_time);',
            'CREATE INDEX nvts_ness_by_cvss_base ON nvts_ness (cvss_base);',
            'CREATE INDEX nvts_ness_by_family ON nvts_ness (family);',
            'CREATE INDEX nvts_ness_by_modification_time ON nvts_ness (modification_time);'
            'CREATE INDEX nvts_ness_by_name ON nvts_ness (name);',
            'CREATE INDEX nvts_ness_by_oid ON nvts_ness (oid);',
            'CREATE INDEX nvts_ness_by_solution_type ON nvts_ness (solution_type);',
            }
        for sql in index_list:
            print(sql)
            try:
                cur.execute(sql)
            except:
                print('#ERROR#create index sql error:' + sql)
        cnx.commit()


    @classmethod
    def insert_cve_report(cls, product_id, product_name, year, vul_type, cve, topvas_file, topvas_exist, nessus_file, nessus_exist):
        sql = ''
        sql = 'INSERT INTO cve_report VALUES( \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (product_id, product_name, year, vul_type, cve, topvas_file, topvas_exist, nessus_file, nessus_exist)

        print('+++++++开始保存数据+++++++')
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert cve_report sql error:' + sql)
        cnx.commit()
    