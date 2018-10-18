import sqlite3

DB_PATH = 'plugins_info.db'

cnx = sqlite3.connect(DB_PATH, check_same_thread = False)
cur = cnx.cursor()

class Sql:
    @classmethod
    def ctl_tb_blog_blogspost(cls):
        #创建表 blog_blogspost
        sql = """
        CREATE TABLE if not exists blog_blogspost ( 
            id                     INTEGER         NOT NULL
                                                   PRIMARY KEY AUTOINCREMENT,
            oid                    VARCHAR( 150 )  NOT NULL,
            name                   VARCHAR( 500 )  NOT NULL,
            name_cn                VARCHAR( 500 ),
            tag                    TEXT,
            cn_ok                  VARCHAR( 10 )   DEFAULT '0',
            summary                TEXT,
            summary_cn             TEXT,
            affected               TEXT,
            affected_cn            TEXT,
            solution               TEXT,
            solution_cn            TEXT,
            insight                TEXT,
            insight_cn             TEXT,
            vuldetect              TEXT,
            vuldetect_cn           TEXT,
            impact                 TEXT,
            impact_cn              TEXT,
            synopsis               TEXT,
            synopsis_cn            TEXT,
            description            TEXT,
            description_cn         TEXT,
            exploitability_ease    TEXT,
            exploitability_ease_cn TEXT,
            risk_factor            TEXT,
            risk_factor_cn         TEXT,
            metasploit_name        TEXT,
            metasploit_name_cn     TEXT,
            d2_elliot_name         TEXT,
            d2_elliot_name_cn      TEXT,
            family                 TEXT,
            family_cn              TEXT );
        """

        #print(sql)
        cur.execute(sql)

        index_sql_list = ('CREATE INDEX oid_idx_1 ON blog_blogspost (oid );',
                          'CREATE INDEX cn_ok_idx_1 ON blog_blogspost (cn_ok );',
                          'CREATE INDEX oid_cn_ok_idx_1 ON blog_blogspost (oid,cn_ok );')
        for index_sql in index_sql_list:
            try:
                cur.execute(index_sql)
            except:
                print('#ERROR#create index failed:%s' % (index_sql))

        cnx.commit()

    @classmethod
    def delete_tb_blog_blogspost(cls):
        sql = 'delete from blog_blogspost where 1=1;'
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert sql failed:%s' % (sql))

    @classmethod
    def sql_execute(cls, sql):
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#sql failed:%s' % (sql))

    @classmethod
    def update_family_cn(cls, family_cn, family):
        sql = 'update blog_blogspost set family_cn = \'%s\' where family= \'%s\' ;' % (family_cn, family)
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#update family_cn error:%s' %(sql))
        cnx.commit()

    @classmethod
    def select_family(cls):
        sql = 'SELECT distinct family from blog_blogspost;'
        print(sql)
        cur.execute(sql)
        return cur.fetchall()

    @classmethod
    def select_blog_blogspost_ok(cls):
        sql = 'SELECT  * from blog_blogspost where cn_ok = \'0\';'
        sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from blog_blogspost where cn_ok = \'0\' ;'
        print(sql)
        cur.execute(sql)
        return cur.fetchall()


    #修改翻译
    @classmethod
    def update_family_auth(cls):
        sql_list = ('update blog_blogspost set family_cn = \'思科\' where family= \'CISCO\' ; ',
                    'update blog_blogspost set family_cn = \'Windows\' where family= \'Windows\' ; ',
                    'update blog_blogspost set family_cn = \'Nmap NSE net\' where family= \'Nmap NSE net\' ; ',
                    'update blog_blogspost set family_cn = \'Finger滥用\' where family= \'Finger abuses\' ; ',
                    'update blog_blogspost set family_cn = \'凭证\' where family= \'Credentials\' ; ',                                                 
                    'update blog_blogspost set family_cn = \'杂项\' where family= \'Misc.\' ; ',
                    'update blog_blogspost set family_cn = \'合规\' where family= \'Compliance\' ;')
        for sql in sql_list:
            print(sql)
            try:
                cur.execute(sql)
            except:
                print('#ERROR#update family_cn error:%s' %(sql))
            cnx.commit()

    @classmethod
    def select_tag_oid(cls):
        sql = 'select  oid, tag from blog_blogspost where cn_ok =\'0\';'
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#sqlite failed:%s' %(sql))
        return cur.fetchall()

    @classmethod
    def update_blog_blogspost_en(cls, oid, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name):
        sql = 'update blog_blogspost set summary = \'%s\',affected = \'%s\', solution = \'%s\', insight = \'%s\', vuldetect = \'%s\', impact = \'%s\', synopsis = \'%s\', description = \'%s\', exploitability_ease = \'%s\', risk_factor = \'%s\', metasploit_name = \'%s\', d2_elliot_name = \'%s\' where oid=\'%s\';' % (summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name, oid)
        #print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#update blog_blogspost error:%s' %(sql))
        cnx.commit()

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")