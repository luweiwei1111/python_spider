from mysqlpiplines.mysql import MySql
from sqlite3piplines.sqlite3_sql import Sql

class TS_Sync:
    def __init__(self):
        print('test')
        #MySql.clear_nvts_cn()
        #MySql.rename_nvts_cn()

    def main(self):
        progress = 0
        sr_nvts_list = Sql.select_nvts()
        for nvts_info in sr_nvts_list:
            id = nvts_info[0]
            uuid = nvts_info[1]
            oid = nvts_info[2] 
            version = nvts_info[3] 
            name = nvts_info[4] 
            comment = nvts_info[5] 
            copyright = nvts_info[6]
            cve = nvts_info[7] 
            bid = nvts_info[8] 
            xref = nvts_info[9] 
            tag = nvts_info[10]
            category = nvts_info[11]
            family = nvts_info[12] 
            cvss_base = nvts_info[13]
            creation_time = nvts_info[14]
            modification_time = nvts_info[15]
            solution_type = nvts_info[16]
            qod = nvts_info[17]
            qod_type = nvts_info[18]
            family_cn = ''
            #根据oid查找对应的中文信息
            nvts_cn_list = MySql.select_nvts_cn_tmp(oid)
            for nvts_cn_info in nvts_cn_list:
                name = nvts_cn_info[0]
                tag = nvts_cn_info[1]
                family_cn = nvts_cn_info[2]
            progress = progress + 1
            if progress%100 == 0:
                print('progress:%d' %(progress))
            MySql.insert_nvts_cn(id, uuid, oid, version, name, comment, copyright, cve, bid, xref, tag, category, family, cvss_base, creation_time, modification_time, solution_type, qod, qod_type, family_cn)

    def update_family(self):
        family_list = MySql.select_family_nvts_cn_tmp()
        for family_info in family_list:
            family = family_info[0]
            family_cn_list = MySql.select_family_cn_nvts_cn_tmp(family)
            family_cn = family
            for family_cn_info in family_cn_list:
                family_cn = family_cn_info[0]
            MySql.update_family_nvts_cn(family_cn, family)

if __name__ == '__main__':
    ts_sync = TS_Sync()
    #ts_sync.main()
    ts_sync.update_family()
	