import pymysql
db = pymysql.connect("localhost", "root", "12345678", "topvas")
cursor = db.cursor()

class MySql:
    @classmethod
    def rename_nvts_cn(cls):
        sql_list = ['ALTER TABLE `nvts_cn` RENAME TO `nvts_cn_tmp`;', 
                    'CREATE TABLE `nvts_cn` LIKE `nvts_cn_tmp`;']
        for sql in sql_list:
            print(sql)
            try:
                cursor.execute(sql)
                db.commit()
            except:
                print('#ERROR:sql error:' + sql)
                db.rollback()
   
    @classmethod
    def clear_nvts_cn(cls):
        sql = 'delete from nvts_cn;'
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('#ERROR:sql error:' + sql)
            db.rollback()

    @classmethod
    def select_nvts_cn_tmp(cls, oid):
        sql = "SELECT name, tag, family_cn from nvts_cn_tmp where oid=%(oid)s"
        value = {
            'oid': oid
        }
        #print(sql)
        try:
            cursor.execute(sql, value)
        except:
            print('#ERROR:sql error:' + sql)
        return cursor.fetchall()

    @classmethod
    def insert_nvts_cn(cls, id, uuid, oid, version, name, comment, copyright, cve, bid, xref, tag, category, family, cvss_base, creation_time, modification_time, solution_type, qod, qod_type, family_cn):
        sql = 'INSERT INTO nvts_cn (`id`, `uuid`, `oid`, `version`, `name`, `comment`, `copyright`, `cve`, `bid`, `xref`, `tag`, `category`, `family`, `cvss_base`, `creation_time`, `modification_time`, `solution_type`, `qod`, `qod_type`, `family_cn`) VALUES (%(id)s, %(uuid)s, %(oid)s, %(version)s, %(name)s, %(comment)s, %(copyright)s, %(cve)s, %(bid)s, %(xref)s, %(tag)s, %(category)s, %(family)s, %(cvss_base)s, %(creation_time)s, %(modification_time)s, %(solution_type)s, %(qod)s, %(qod_type)s, %(family_cn)s)'
        value = {
            'id': id,
            'uuid': uuid,
            'oid': oid,
            'version': version,
            'name': name,
            'comment': comment,
            'copyright': copyright,
            'cve': cve,
            'bid': bid,
            'xref': xref,
            'tag': tag,
            'category': category,
            'family': family,
            'cvss_base': cvss_base,
            'creation_time': creation_time,
            'modification_time': modification_time, 
            'solution_type': solution_type, 
            'qod':qod, 
            'qod_type': qod_type, 
            'family_cn': family_cn
        }

        #print(sql)
        try:
            cursor.execute(sql, value)
            db.commit()
        except:
            print('#ERROR:sql error:' + sql)
            db.rollback()
    
    @classmethod 
    def select_family_nvts_cn_tmp(cls):
        sql = 'select distinct family from nvts_cn_tmp;'
        try:
            cursor.execute(sql)
        except:
            print('#ERROR:sql error:' + sql)
        return cursor.fetchall()

    @classmethod
    def select_family_cn_nvts_cn_tmp(cls, family):
        sql = 'select distinct family_cn from nvts_cn_tmp where family = \'%s\';' %(family)
        try:
            cursor.execute(sql)
        except:
            print('#ERROR:sql error:' + sql)
        return cursor.fetchall()

    @classmethod
    def update_family_nvts_cn(cls, family_cn, family):
        sql = 'update nvts_cn set family_cn=\'%s\' where family=\'%s\';' %(family_cn, family)
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('#ERROR:sql error:' + sql)
            db.rollback()