import sqlite3


SQLITE3_DB = 'tasks.db'

cnx = sqlite3.connect(SQLITE3_DB, check_same_thread = False)
cur = cnx.cursor()

class Sql:
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
    def sqliteEscape(cls, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")