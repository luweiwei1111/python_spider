from fanyi import settings
import sqlite3

SQLITE3_DB = settings.SQLITE3_DB

cnx = sqlite3.connect(SQLITE3_DB, check_same_thread = False)
cur = cnx.cursor()

class Sql:
    @classmethod
    def ctl_tb_blog_blogspost(cls):
        crt_tb_sql = 'create table if not exists blog_blogspost( \
           id                      INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT, \
           oid                     VARCHAR( 150 )  NOT NULL, \
           name                    VARCHAR( 500 )  NOT NULL, \
           name_cn                 VARCHAR( 500 ), \
           tag                     TEXT, \
           cn_ok                   VARCHAR( 10 ) default \'no\', \
           summary                 TEXT, \
           summary_cn              TEXT, \
           affected                TEXT, \
           affected_cn             TEXT, \
           solution                TEXT, \
           solution_cn             TEXT, \
           insight                 TEXT, \
           insight_cn              TEXT, \
           vuldetect               TEXT, \
           vuldetect_cn            TEXT, \
           impact                  TEXT, \
           impact_cn               TEXT, \
           synopsis                TEXT, \
           synopsis_cn             TEXT, \
           description             TEXT, \
           description_cn          TEXT, \
           exploitability_ease     TEXT, \
           exploitability_ease_cn  TEXT, \
           risk_factor             TEXT, \
           risk_factor_cn          TEXT, \
           metasploit_name         TEXT, \
           metasploit_name_cn      TEXT, \
           d2_elliot_name          TEXT, \
           d2_elliot_name_cn       TEXT, \
           family                  TEXT, \
           family_cn               TEXT);'

        #print(crt_tb_sql)
        cur.execute(crt_tb_sql)
        cnx.commit()

    @classmethod
    def clr_blog_blogspost(cls):
        sql = 'delete from blog_blogspost;'

        print(sql)
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def drop_blog_blogspost(cls):
        sql = 'drop table blog_blogspost;'

        print(sql)
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def ctl_index_nvts_ness(cls):
        #为nvts表创建索引
        index_list = {
            'CREATE INDEX nvts_by_creation_time ON nvts(creation_time);',
            'CREATE INDEX nvts_by_cvss_base ON nvts(cvss_base);',
            'CREATE INDEX nvts_by_family ON nvts(family);',
            'CREATE INDEX nvts_by_modification_time ON nvts(modification_time);'
            'CREATE INDEX nvts_by_name ON nvts(name);',
            'CREATE INDEX nvts_by_oid ON nvts(oid);',
            'CREATE INDEX nvts_by_oid_name ON nvts(oid, name);',
            'CREATE INDEX nvts_by_solution_type ON nvts(solution_type);',
            }
        for sql in index_list:
            print(sql)
            try:
                cur.execute(sql)
            except:
                print('#ERROR#create index sql error:' + sql)
        cnx.commit()

    @classmethod
    def sync_blog_blogspost_and_nvts(cls):
        """
        1.对比blog_blogspost表和nvts表，将blog_blogspost存在，但是nvts表不存在的数据删除;
        2.将nvts表中存在，但是blog_blogspost存在的数据插入到blog_blogpost
        此操作目的是再与nvts表更新后，blogs_blogspost与之不匹配，作为数据统一同步的功能
        """
        index_list = {
            'delete  from blog_blogspost  where not exists (select * from nvts  where nvts.oid =blog_blogspost.oid);',
            'insert into blog_blogspost(oid,name,tag,family) select t1.oid,t1.name,t1.tag,t1.family from nvts t1 where not exists (select * from blog_blogspost t2 where t1.oid = t2.oid)',
            }
        for sql in index_list:
            print(sql)
            try:
                cur.execute(sql)
            except:
                print('#ERROR#create index sql error:' + sql)
        cnx.commit()

    @classmethod
    def select_blog_blogspost_by_cn_ok(cls, cn_ok):
        sql = 'select  oid, name, tag from blog_blogspost where cn_ok =\'%s\'' % (cn_ok)

        print(sql)
        cur.execute(sql)
        cnx.commit()

    def insert_blog_blogspost(cls):
        sql = 'insert into blog_blogspost(oid,name,tag,family) select oid,name,tag,family from nvts  ORDER BY id LIMIT 10'
        
        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#insert blog_blogspost sql error:' + sql)
        cnx.commit()

    def update_blog_blogspost(cls, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name, oid, name):
        sql = """update blog_blogspost set  
            summary = \'%s\',
            affected = \'%s\',
            solution = \'%s\',
            insight = \'%s\',
            vuldetect = \'%s\',
            impact = \'%s\',
            synopsis = \'%s\',
            description = \'%s\',
            exploitability_ease = \'%s\',
            risk_factor = \'%s\',
            metasploit_name = \'%s\',
            d2_elliot_name = \'%s\'  
            where oid = \'%s\' and name = \'%s\';""" % (summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name, oid, name)

        print(sql)
        try:
            cur.execute(sql)
        except:
            print('#ERROR#update sql error:' + sql)
        cnx.commit()

    @classmethod
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")