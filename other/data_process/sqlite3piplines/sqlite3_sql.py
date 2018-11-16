# coding=utf-8
import sqlite3

cnx = sqlite3.connect('plugins_all.db')
cur = cnx.cursor()

class Sql:
    @classmethod
    def ctl_tb_ness_info(cls):
        crt_tb_sql = 'CREATE TABLE if not exists ness_info( \
            id                  INTEGER, \
            file_name           TEXT NOT NULL, \
            line_desc           TEXT, \
            line_all            TEXT, \
            PRIMARY KEY (id,file_name) )'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def insert_ness_info(cls, id, file_name, line_desc, line_all):
        sql = ''
        sql = 'INSERT INTO ness_info VALUES( \'%s\', \'%s\', \'%s\', \'%s\');' % (id, file_name, line_desc, line_all)

        #print('+++++++开始保存数据+++++++')
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert ness_info sql error:' + sql)
        cnx.commit()

    @classmethod
    def sql_execute(cls, sql):
        print(sql)
        cur.execute(sql)
        return cur.fetchall()

    @classmethod
    def select_ness_info_line(cls):
        sql = 'SELECT file_name, line_desc, line_all from ness_info;'
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#select sql error:' + sql)
        return cur.fetchall()

    @classmethod
    def ctl_tb_topvas_oid_info(cls):
        crt_tb_sql = 'CREATE TABLE if not exists topvas_oid_info( \
            oid           TEXT NOT NULL, \
            file_name     TEXT NOT NULL);'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def insert_topvas_oid_info(cls, oid, file_name):
        sql = ''
        sql = 'INSERT INTO topvas_oid_info VALUES( \'%s\', \'%s\');' % (oid, file_name)
        #print('+++++++开始保存数据+++++++')
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert topvas_oid_info sql error:' + sql)
        cnx.commit()

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")