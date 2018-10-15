import os
import sqlite3
import sys
import re
import datetime

starttime = datetime.datetime.now()

cx = sqlite3.connect('/usr/local/zy/db.sqlite3')
cu = cx.cursor()

#查找服务到数组
service_list = []
select_service_sql = 'select distinct name from port_names'
try:
    result_svc = cu.execute(select_service_sql)
    all_info_svc = result_svc.fetchall()
    for info_cve in all_info_svc:
        svc = info_cve[0].lower()
        service_list.append(svc)
except:
    print('sql error:' + select_service_sql)


#select 搜索
#select_cve_sql = 'select oid, name, summary, affected, cve from cve_cve_info where language =\'CN\' and id < 50'
select_cve_sql = 'select oid, name, summary, affected, cve from cve_cve_info where language =\'CN\';'
update_svc_sql = []
update_svc_count = 0

try:
    cve_name_ok_list = []
    cve_summary_ok_list = []
    cve_affected_ok_list = []
    result_cve = cu.execute(select_cve_sql)
    all_info_cve = result_cve.fetchall()
    for info_cve in all_info_cve:
        file_oid = info_cve[0]
        #1.name
        cve_name = info_cve[1].lower()
        cve_name_list = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])"," ", cve_name).split(' ')
        for name_new in cve_name_list:
            if name_new not in cve_name_ok_list:
                #print('cve_name:' + name_new)
                cve_name_ok_list.append(name_new)

        #2.summary
        cve_summary = info_cve[2].lower()
        cve_summary_list = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])"," ", cve_summary).split(' ')
        for summary_new in cve_summary_list:
            if summary_new not in cve_summary_ok_list:
                #print('summary:' + summary_new)
                cve_summary_ok_list.append(summary_new)

        #3.affected
        cve_affected = info_cve[3].lower()
        cve_affected_list = re.sub(u"([^\u0030-\u0039\u0041-\u005a\u0061-\u007a])"," ", cve_affected).split(' ')
        for affected_new in cve_affected_list:
            if affected_new not in cve_affected_ok_list:
                #print('affected:' + affected_new)
                cve_affected_ok_list.append(affected_new)

        cve_cve = info_cve[4]
        #print('###############################################################')
        #遍历查找
        service_set = ''
        count_ok = 0
        for svc in service_list:
            if count_ok > 5:
                #print('count >5, service = ' + service_set)
                break;
            if svc in cve_name:
                #print('##' + svc+ ' svc in name:' + cve_name + ', oid:' + file_oid)
                tmp_count = 0
                for buf_name in cve_name_ok_list:
                    count_ok = count_ok + 1
                    if svc in buf_name:
                        if tmp_count > 5:
                            break;
                        if tmp_count == 0:
                            service_set = '[' + svc + ']' + buf_name
                            tmp_count = tmp_count + 1
                        else:
                            service_set = service_set + ',' + buf_name
                            tmp_count = tmp_count + 1
            elif svc in cve_summary:
                #print('##' + svc+ ' svc in summary:' + cve_summary + ', oid:' + file_oid)
                tmp_count = 0
                for buf_summary in cve_name_ok_list:
                    count_ok = count_ok + 1
                    if svc in buf_summary:
                        if tmp_count > 5:
                            break;
                        if tmp_count == 0:
                            service_set = '[' + svc + ']' + buf_summary
                            tmp_count = tmp_count + 1
                        else:
                            service_set = service_set + ',' + buf_summary
                            tmp_count = tmp_count + 1
            elif svc in cve_affected:
                #print('##' + svc+ ' svc in affected:' + cve_affected + ', oid:' + file_oid)
                tmp_count = 0
                for buf_affected in cve_name_ok_list:
                    count_ok = count_ok + 1
                    if svc in buf_affected:
                        if tmp_count > 5:
                            break;
                        if tmp_count == 0:
                            service_set = '[' + svc + ']' + buf_affected
                            tmp_count = tmp_count + 1
                        else:
                            service_set = service_set + ',' + buf_affected
                            tmp_count = tmp_count + 1
        #print('service set:' + service_set)
        if service_set != '':
            set_sql = 'update cve_cve_info set service = \'' + service_set + '\'' + ' where oid = \'' + file_oid + '\''
            #print('service set sql:' + set_sql)
            if update_svc_count%100 == 0:
                print('Get progress:' + str(update_svc_count))
            update_svc_sql.append(set_sql)
            update_svc_count = update_svc_count + 1
        #else:
        #    print('service set NULL')

except:
    print('sql error:' + select_cve_sql)

print('Get Update Sql num[' + str(update_svc_count) + '] OK!!')
count_up = 0
for sql in update_svc_sql:
    try:
        cu.execute(sql)
        count_up = count_up + 1
        if count_up%100 == 0:
            print('count:' + str(count_up))
    except:
        print('update sql error:' + sql)

print('Update cve_cve_info service OK!! num[' + str(update_svc_count) + ']')

#long running
endtime = datetime.datetime.now()
print('cost time: ' + str((endtime - starttime).seconds) + ' seconds')

#关闭游标
cu.close()

#事务提交
cx.commit()

#关闭数据库
cx.close()

