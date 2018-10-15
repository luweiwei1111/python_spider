#coding=utf-8
#!/usr/bin/env bash

import threading
import sqlite3
import sys
import os
import time

"""
将Django里面的数据导出到表nvts_cn，用于中文显示
"""

"""
.output nvts_cn.sql
.dump nvts 
.output stdout
"""
#创建表 nvts_cn 并插入数据
def crt_tbl_nvts_cn(cu, max_num):
    #####创建表 nvts_cn 并插入数据
    try:
        cu.execute('drop table if exists nvts_cn')
    except:
        print('drop table nvts_cn failed')
    #创建表 blog_blogspost
    ctl_nvts_cn = 'create table if not exists nvts_cn( \
            id         INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT, \
            uuid       TEXT, \
            oid        TEXT, \
            version    TEXT, \
            name       TEXT, \
            comment    TEXT, \
            copyright  TEXT, \
            cve        TEXT, \
            bid        TEXT, \
            xref       TEXT, \
            tag        TEXT, \
            category   INT, \
            family     TEXT, \
            cvss_base  TEXT, \
            creation_time     TEXT, \
            modification_time TEXT, \
            solution_type     TEXT, \
            qod               INT, \
            qod_type          TEXT);'
    print('##->1.Create Table nvts_cn Success')
    cu.execute(ctl_nvts_cn)

    #创建索引
    #cu.execute('CREATE INDEX oid_idx_11 ON nvts (oid);')
    #插入数据
    #all_data_flag = True
    #insert_sql = 'insert into nvts_cn(uuid, oid, version, name, comment, copyright, cve, bid, xref, \
    #    tag, category, family, cvss_base, creation_time, modification_time, solution_type, qod, qod_type)  \
    #    select t1.oid,t1.oid,t2.version,t1.name_cn,t2.comment, t2.copyright, t2.cve, t2.bid, t2.xref, \
    #    t1.tag, t2.category, t1.family,t2.cvss_base, t2.creation_time, t2.modification_time, t2.solution_type, t2.qod, t2.qod_type \
    #    from blog_blogspost t1, nvts t2 where t1.oid = t2.oid  ORDER BY t1.id;'
    #insert_sql = 'insert into nvts_cn(uuid,oid,name,tag) select oid,oid,name_cn,tag from blog_blogspost ORDER BY id LIMIT ' + str(max_num) + ';'  
    insert_sql = 'insert into nvts_cn select * from nvts where 1=1;'

    print('##->' + insert_sql)
    try:
        cu.execute(insert_sql)
    except:
        print('#ERROR#insert sql error:' + insert_sql)

    #创建索引
    cu.execute('CREATE INDEX nvts_cn_by_oid on nvts_cn(oid);')
    cu.execute('CREATE INDEX nvts_cn_by_name on nvts_cn(name);')
    cu.execute('CREATE INDEX nvts_cn_by_family on nvts_cn(family);')
    cu.execute('CREATE INDEX nvts_cn_by_creation_time on nvts_cn(creation_time);')
    cu.execute('CREATE INDEX nvts_cn_by_modifycation_time on nvts_cn(modification_time);')
    cu.execute('CREATE INDEX nvts_cn_by_cvss_base on nvts_cn(cvss_base);')
    cu.execute('CREATE INDEX nvts_cn_by_solution_type on nvts_cn(solution_type);')
    print('##->2.Insert data into nvts_cn Success')

def nomal_data_proc(conn, max_num):    
    cur = conn.cursor()
    sql = 'select oid,tag, summary_cn, affected_cn, solution_cn, insight_cn, vuldetect_cn, impact_cn, synopsis_cn,' + \
        'description_cn, exploitability_ease_cn, risk_factor_cn, metasploit_name_cn, d2_elliot_name_cn, name_cn ' + \
        'from blog_blogspost where cn_ok = \'1\' ORDER BY id;'
    print('sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)

    #关闭游标
    cur.close()
    #事务提交
    conn.commit()
    #关闭数据库
    conn.close()

def data_process(all_nvts, cur):
    nvts_tag = ''
    error_oid_list = []
    gl_Tag_name_cn = ('summary',
                      'affected',
                      'solution',
                      'insight',
                      'vuldetect',
                      'impact',
                      'synopsis'
                      'description',
                      'exploitability_ease',
                      'risk_factor',
                      'metasploit_name',
                      'd2_elliot_name')
    count = 0
    count_oid_failed = 0
    nvts_failed = []
    for info_nvts in all_nvts:
        count = count + 1
        nvts_oid = info_nvts[0]
        nvts_tag = info_nvts[1]
        summary_cn = info_nvts[2]
        affected_cn = info_nvts[3]
        solution_cn = info_nvts[4]
        insight_cn = info_nvts[5]
        vuldetect_cn = info_nvts[6]
        impact_cn = info_nvts[7]
        synopsis_cn = info_nvts[8]
        description_cn = info_nvts[9]
        exploitability_ease_cn = info_nvts[10]
        risk_factor_cn = info_nvts[11]
        metasploit_name_cn = info_nvts[12]
        d2_elliot_name_cn = info_nvts[13]
        name_src = info_nvts[14]
        name_cn = name_src.replace('\'', '\'\'')
        #if str(summary_cn) == 'None':
        #    #print('Source data NULL,continue, oid=' + nvts_oid)
        #    print('progress->' + str(count))
        #    count_oid_failed = count_oid_failed + 1
        #    nvts_failed.append(nvts_oid)
        #    continue;

        cn_nvts_tag = ''
        if nvts_tag != 'NOTAG':
            #解析tag
            tag_list = nvts_tag.split('|')
            tag_name_desc = ''
            for tag_info in tag_list:
                tag_name = tag_info.split('=')[0]
                if tag_name not in gl_Tag_name_cn:
                    cn_nvts_tag = cn_nvts_tag + '|' + tag_info.replace('\'', '\'\'')
                else:
                    if tag_name == 'summary':
                        cn_nvts_tag = cn_nvts_tag + '|summary=' + summary_cn.replace('\'', '\'\'')
                    if tag_name == 'affected':
                        cn_nvts_tag = cn_nvts_tag + '|affected=' + affected_cn.replace('\'', '\'\'')
                    if tag_name == 'solution':
                        cn_nvts_tag = cn_nvts_tag + '|solution=' + solution_cn.replace('\'', '\'\'')
                    if tag_name == 'insight':
                        cn_nvts_tag = cn_nvts_tag + '|insight=' + insight_cn.replace('\'', '\'\'')
                    if tag_name == 'vuldetect':
                        cn_nvts_tag = cn_nvts_tag + '|vuldetect=' + vuldetect_cn.replace('\'', '\'\'')
                    if tag_name == 'impact':
                        cn_nvts_tag = cn_nvts_tag + '|impact=' + impact_cn.replace('\'', '\'\'')
                    if tag_name == 'synopsis':
                        cn_nvts_tag = cn_nvts_tag + '|synopsis=' + synopsis_cn.replace('\'', '\'\'')
                    if tag_name == 'description':
                        cn_nvts_tag = cn_nvts_tag + '|description=' + description_cn.replace('\'', '\'\'')
                    if tag_name == 'exploitability_ease':
                        cn_nvts_tag = cn_nvts_tag + '|exploitability_ease=' + exploitability_ease_cn.replace('\'', '\'\'')
                    if tag_name == 'risk_factor':
                        cn_nvts_tag = cn_nvts_tag + '|risk_factor=' + risk_factor_cn.replace('\'', '\'\'')
                    if tag_name == 'metasploit_name':
                        cn_nvts_tag = cn_nvts_tag + '|metasploit_name=' + metasploit_name_cn.replace('\'', '\'\'')
                    if tag_name == 'd2_elliot_name':
                        cn_nvts_tag = cn_nvts_tag + '|d2_elliot_name=' + d2_elliot_name_cn.replace('\'', '\'\'')    

            print('progress->' + str(count))
            #print('#english tag:' + nvts_tag)
            cn_nvts_tag_sql = cn_nvts_tag[1:]
            #print('#chinese tag:' + cn_nvts_tag)
            #print('\n')
            update_sql = 'update nvts_cn set tag = \'' + cn_nvts_tag_sql + '\', name = \'' + name_cn + '\' where oid = \'' + nvts_oid + '\''
            try:
                #print('update sql:' + update_sql)
                cur.execute(update_sql)
            except:
                print('#ERROR# sql:' + update_sql)
                continue

    for oid_info in nvts_failed:
        print('update failed oid:' + oid_info)
    print('update failed oid count:' + str(count_oid_failed))

def import_nvts(path):
    #删除nvts表
    try:
        cu.execute('drop table if exists nvts')
    except:
        print('drop table nvts failed')

    #导入数据到tasks.db
    try:
        attach_sql = 'attach  \"' + path + '\"  as t1;'
        print(attach_sql)
        cu.execute(attach_sql)
    except:
        print('attach sql error:' + attach_sql)

    import_sql = 'create table nvts as select * from t1.nvts;'
    print('import sql:' + import_sql)
    try:
        print(import_sql)
        cu.execute(import_sql)
    except:
        print('import sql error:' + import_sql)
        pass
    print('import nvts data ok!!!')

def topvas_upgrade_nvts(flag):
    #topvassd更新插件库
    #清空redis-server数据
    redis_cmd = '/usr/bin/redis-cli flushall'
    os.system(redis_cmd)

    if flag == 'topvas':
        ps_topvassd = 'ps -ef|grep topvassd|grep -v "grep --color=auto"'
        #topvas_rebuild_cmd = '/usr/local/scanner/bin/topvasmd --rebuild'
        topvas_rebuild_cmd = 'sh topvas_rebuild.sh'
    else:
        ps_topvassd = 'ps -ef|grep openvassd|grep -v "grep --color=auto"'
        topvas_rebuild_cmd = '/usr/local/sbin/topvasmd --rebuild'
    count = 0
    while True:
        time.sleep(20)
        count = count + 1
        print('##process:' + str(count))
        if get_upgrade_res(ps_topvassd):
            break

    #rebuild nvts
	print(topvas_rebuild_cmd)
    os.system(topvas_rebuild_cmd)
    print('##rebuild success')

def get_upgrade_res(cmd_line):
    process = ''
    res = os.popen(cmd_line) 
    info = res.readlines()
    list_len = len(info)
    if list_len == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    gl_Tag_name_cn = []
    gl_count_nvts = 0

    max_num = 100

    param_len = len(sys.argv)
    if param_len != 2:
        sys.exit('input param need 1,useage:python2.7 ' +sys.argv[0] + ' openvas/topvas')   
    else:
        cmd_flag = sys.argv[1]
        if cmd_flag != 'openvas' and cmd_flag != 'topvas':
            sys.exit('input param need 1,useage:python2.7 ' +sys.argv[0] + ' openvas/topvas') 

    print('Run Mode:' + cmd_flag)

    flag_in = True
    if flag_in == True:
        #插件数据更新到nvts表中
        topvas_upgrade_nvts(cmd_flag)
        #sys.exit('exit')

    #2.导出/usr/local/var/lib/openvas/mgr/tasks.db里面的数据到本地的tasks.db
    if cmd_flag == 'topvas':
        db_path_topvas_src = '/usr/local/scanner/var/lib/topvas/mgr/tasks.db'
    else:
        db_path_topvas_src = '/usr/local/var/lib/openvas/mgr/tasks.db'

    db_path = 'tasks.db'
    cx = sqlite3.connect(db_path)
    cu = cx.cursor()

    import_nvts(db_path_topvas_src)

    #1.创建表并插入数据
    crt_tbl_nvts_cn(cu, max_num)
    
    #关闭游标
    cu.close()
    #事务提交
    cx.commit()
    #关闭数据库
    cx.close()

    # 2.数据处理
    conn = sqlite3.connect(db_path)
    nomal_data_proc(conn, max_num)

    readme = """
Please dump nvts_cn data:
##############################
sqlite3 tasks.db
sqlite>.output nvts_cn.sql
sqlite>.dump nvts_cn
sqlite>.output stdout
mv nvts_cn.sql ../../data/
##############################"""
    print(readme)
