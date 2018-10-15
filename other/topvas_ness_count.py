# coding=utf-8

import os
import sqlite3
import sys
import re
import os.path
import codecs

NESS_SCRIPT_ID_DEF  = 'script_id'
NESS_SCRIPT_NAME_DEF = 'script_name'
NESS_SCRIPT_CATEGORY_DEF = 'script_category'
NESS_SCRIPT_FAMILY_DEF = 'script_family'

#获取ness插件信息
def get_ness_script_info(file_name , fr_open, id_sqlite3):
    script_cve_id = ''
    script_cve_id_temp = ''
    script_id = ''
    script_name = ''
    script_category = ''
    script_family = ''
    pattern = re.compile('"(CVE-.*[0-9])"')
    cve_count = 0

    for line in fr_open.readlines():
        if NESS_SCRIPT_ID_DEF in line:
            script_id = line.replace('script_id', '').replace('(', '').replace(')', '').replace(';', '').replace('\n', '')
            #print('script_id:' + script_id)
        elif '\"CVE-' in line:
            patt_list = pattern.findall(line)
            cve_temp = ''
            if len(patt_list):
                cve_count = cve_count + 1
                cve_list = patt_list[0].replace('"', '').replace(' ', '').split(',')
                if len(cve_list):
                    for ii in range(0, len(cve_list)):
                        if ii == 0:
                            cve_temp = cve_list[0]
                        else:
                            cve_temp = cve_temp + ',' + cve_list[ii]
                if cve_count == 1:
                    script_cve_id = cve_temp
                else:
                    script_cve_id = script_cve_id + ',' + cve_temp
            #print('cve:' + str(script_cve_id)
        elif NESS_SCRIPT_NAME_DEF in line:
            script_name = line.replace('script_name', '').replace('(', '').replace(')', '').replace('"', '').replace(';', '').replace('\'', '\'\'').replace('\n', '').lstrip()
            #print('script_name:' + script_name)
        elif NESS_SCRIPT_CATEGORY_DEF in line:
            script_category = line.replace('script_category', '').replace('(', '').replace(')', '').replace('"', '').replace(' ', '').replace(';', '').replace('\n', '')
            #print('script_category:' + script_category)
        elif 'family[\"english\"]' in line and '=' in line:
            script_family = line.replace('family[\"english\"]', '').replace('=', '').replace('"', '').replace('\'', '').replace(';', '').replace('\n', '')
            #print('script_family1:###' + script_family + '#####' + file_name)
        elif NESS_SCRIPT_FAMILY_DEF in line:
            if script_family == '':
                script_family = line.replace('script_family', '').replace('(', '').replace(')', '').replace('"', '').replace('\'', '').replace(';', '').replace('\n', '')
                #print('script_family2:###' + script_family + '#####')
    id = str(id_sqlite3)
    insert_script_info = 'insert into ness_info(id, file_name, script_id, script_name, script_category, script_family, script_cve_id) values('+ \
                                 '\'' + id + '\',' +  \
                                 '\'' + file_name + '\',' +  \
                                 '\'' + script_id + '\',' +  \
                                 '\'' + script_name + '\',' +  \
                                 '\'' + script_category + '\',' +  \
                                 '\'' + script_family + '\',' +  \
                                 '\'' + script_cve_id + '\');'
    #print('sql:' + insert_script_info) 
    return insert_script_info


TOPVAS_SCRIPT_ID_DEF  = 'script_oid'
TOPVAS_SCRIPT_NAME_DEF = 'script_name'
TOPVAS_SCRIPT_CATEGORY_DEF = 'script_category'
TOPVAS_SCRIPT_FAMILY_DEF = 'script_family'

#获取topvas插件信息
def get_topvas_script_info(file_name , fr_open, id_sqlite3):
    script_cve_id = ''
    script_cve_id_temp = ''
    script_id = ''
    script_name = ''
    script_category = ''
    script_family = ''
    pattern = re.compile('"(CVE-.*[0-9])"')
    cve_count = 0

    for line in fr_open.readlines():
        if not line:
            break;
        else:
            line.encode('gb18030')
            if TOPVAS_SCRIPT_ID_DEF in line:
                script_id = line.replace('script_oid', '').replace('(', '').replace(')', '').replace(';', '').replace('\n', '').replace('"', '')
                #print('script_id:' + script_id)
            elif '\"CVE-' in line:
                patt_list = pattern.findall(line)
                cve_temp = ''
                if len(patt_list):
                    cve_count = cve_count + 1
                    cve_list = patt_list[0].replace('"', '').replace(' ', '').split(',')
                    if len(cve_list):
                        for ii in range(0, len(cve_list)):
                            if ii == 0:
                                cve_temp = cve_list[0]
                            else:
                                cve_temp = cve_temp + ',' + cve_list[ii]
                    if cve_count == 1:
                        script_cve_id = cve_temp
                    else:
                        script_cve_id = script_cve_id + ',' + cve_temp
            elif TOPVAS_SCRIPT_NAME_DEF in line:
                script_name = line.replace('script_name', '').replace('(', '').replace(')', '').replace('"', '').replace(';', '').replace('\'', '\'\'').replace('\n', '')
                #print('script_name:' + script_name)
            elif TOPVAS_SCRIPT_CATEGORY_DEF in line:
                script_category = line.replace('script_category', '').replace('(', '').replace(')', '').replace('"', '').replace(' ', '').replace(';', '').replace('\n', '')
                #print('script_category:' + script_category)
            elif 'family =' in line:
                script_family = line.replace('family =', '').replace('=', '').replace('"', '').replace('\'', '').replace(';', '').replace('\n', '')
                #print('script_family1:###' + script_family + '#####' + file_name)
            elif TOPVAS_SCRIPT_FAMILY_DEF in line:
                if script_family == '':
                    script_family = line.replace('script_family', '').replace('(', '').replace(')', '').replace('"', '').replace('\'', '').replace(';', '').replace('\n', '')
 
    #print('file_name:' + file_name +  '\nscript_id:' + script_id + '\nscript_cve_id:' + script_cve_id + '\nscript_category:' + script_category + '\nscript_family:' + script_family)
    id = str(id_sqlite3)
    insert_script_info = 'insert into topvas_info(oid, file_name, script_id, script_name, script_category, script_family, script_cve_id) values('+ \
                         '\'' + id + '\',' +  \
                         '\'' + file_name + '\',' +  \
                         '\'' + script_id + '\',' +  \
                         '\'' + script_name + '\',' +  \
                         '\'' + script_category + '\',' +  \
                         '\'' + script_family + '\',' +  \
                         '\'' + script_cve_id + '\');'

    #print('sql:' + insert_script_info) 
    return insert_script_info

def search_file(dir,sname, cu): 
    if sname in os.path.split(dir)[1]: #检验文件名里是否包含sname 
        global case_total_num  # global声明
        case_total_num = case_total_num + 1;
        if case_total_num%1000 == 0:
            print('topvas id = ' + str(case_total_num))
        #相对路径
        script_file = os.path.relpath(dir)
        filename = script_file.split('/')[-1]
        fr_nasl = codecs.open(script_file, 'r',encoding= u'utf-8',errors='ignore')
        insert_sql = get_topvas_script_info(filename , fr_nasl, case_total_num)
        #print("sql:" + insert_sql)
        try:
            cu.execute(insert_sql)
        except :
            print('error id=' + str(count) + ' file=' + filename)
        fr_nasl.close()
        
    if os.path.isfile(dir):   # 如果传入的dir直接是一个文件目录 他就没有子目录，就不用再遍历它的子目录了
        return 

    for dire in os.listdir(dir): # 遍历子目录  这里的dire为当前文件名 
        search_file(os.path.join(dir,dire),sname, cu) #jion一下就变成了当前文件的绝对路径

case_total_num = 0

#将数据插入到base_info表中
def insert_data_base_info(cu):
    #base_info保存重要设备信息
    #根据文件名和family来筛选
    insert_sql_family = [\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(1, \'常用操作系统\', \'windows\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(2, \'常用操作系统\', \'centos\', \'CentOS Local Security Checks\', \'CentOS Local Security Checks\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(3, \'常用操作系统\', \'ubuntu\', \'Ubuntu Local Security Checks\', \'Ubuntu Local Security Checks\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(4, \'常用操作系统\', \'suse\',   \'SuSE Local Security Checks\',   \'SuSE Local Security Checks\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(5, \'大数据组件\', \'hadoop\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(6, \'大数据组件\', \'zookeeper\', \'Fedora Local Security Checks\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(7, \'虚拟化平台\', \'vmware\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(8, \'虚拟化平台\', \'esxi\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(9, \'虚拟化平台\', \'xen\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(10, \'虚拟化平台\', \'xenserver\', \'Citrix Xenserver Local Security Checks\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(11, \'虚拟化平台\', \'hyper_v\', \'Windows : Microsoft Bulletins\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(12, \'应用中间件\', \'apache\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(13, \'应用中间件\', \'iis\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(14, \'应用中间件\', \'weblogic\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(15, \'应用中间件\', \'websphere\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(16, \'应用中间件\', \'tomcat\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(17, \'应用中间件\', \'nginx\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(18, \'数据库\', \'mysql\', \'Databases\', \'Databases\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(19, \'数据库\', \'mssql\', \'Databases\', \'Databases\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(20, \'数据库\', \'db2\', \'Databases\', \'Databases\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(21, \'国产数据库\', \'dameng\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(22, \'国产数据库\', \'gbase\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(23, \'网络设备\', \'h3c\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(24, \'网络设备\', \'cisco\', \'cisco\', \'cisco\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(25, \'网络设备\', \'juniper\', \'General\', \'Junos Local Security Checks\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(26, \'网络设备\', \'huawei\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(27, \'网络设备\', \'maipu\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(28, \'网络设备\', \'zte\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(29, \'网络设备\', \'f5\', \'F5 Local Security Checks\', \'F5 Networks Local Security Checks\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(30, \'网络设备\', \'checkpoint\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(31, \'国产安全设备\', \'启明\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(32, \'国产安全设备\', \'nsfocus\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(33, \'国产安全设备\', \'360 safe\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(34, \'国产安全设备\', \'山石\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(35, \'国产安全设备\', \'深信服\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(36, \'国产安全设备\', \'topsec\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(37, \'弱口令检测\', \'hydra\', \'\', \'\')'\
    ]

    #根据文件名来筛选
    insert_sql = [\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(1, \'常用操作系统\', \'windows\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(2, \'常用操作系统\', \'centos\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(3, \'常用操作系统\', \'ubuntu\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(4, \'常用操作系统\', \'suse\',   \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(5, \'大数据组件\', \'hadoop\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(6, \'大数据组件\', \'zookeeper\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(7, \'虚拟化平台\', \'vmware\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(8, \'虚拟化平台\', \'esxi\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(9, \'虚拟化平台\', \'xen\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(10, \'虚拟化平台\', \'xenserver\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(11, \'虚拟化平台\', \'hyper_v\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(12, \'应用中间件\', \'apache\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(13, \'应用中间件\', \'iis\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(14, \'应用中间件\', \'weblogic\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(15, \'应用中间件\', \'websphere\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(16, \'应用中间件\', \'tomcat\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(17, \'应用中间件\', \'nginx\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(18, \'数据库\', \'mysql\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(19, \'数据库\', \'mssql\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(20, \'数据库\', \'db2\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(21, \'国产数据库\', \'dameng\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(22, \'国产数据库\', \'gbase\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(23, \'网络设备\', \'h3c\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(24, \'网络设备\', \'cisco\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(25, \'网络设备\', \'juniper\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(26, \'网络设备\', \'huawei\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(27, \'网络设备\', \'maipu\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(28, \'网络设备\', \'zte\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(29, \'网络设备\', \'f5\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(30, \'网络设备\', \'checkpoint\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(31, \'国产安全设备\', \'启明\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(32, \'国产安全设备\', \'nsfocus\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(33, \'国产安全设备\', \'360 safe\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(34, \'国产安全设备\', \'山石\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(35, \'国产安全设备\', \'深信服\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(36, \'国产安全设备\', \'topsec\', \'\', \'\')',\
    'insert into base_info(id, type, file_name, family_topvas, family_ness) values(37, \'弱口令检测\', \'hydra\', \'\', \'\')'\
    ]

    #1 创建基本配置表base_info
    ctb_base_info = 'create table if not exists base_info ( \
    id              INTEGER, \
    type            TEXT, \
    plugins_type    TEXT, \
    file_name       TEXT, \
    family_topvas   TEXT, \
    family_ness     TEXT, \
    reserve1        TEXT, \
    reserve2        TEXT, \
    reserve3        TEXT, \
    PRIMARY KEY ( id, file_name ) );'
    cu.execute(ctb_base_info)
    cu.execute('delete from base_info where 1=1;')
    print("##Create Table base_info Success!!!")
    
    ctb_import_plugins_cves = 'create table if not exists count_import_plugins_cves ( \
    id              INTEGER, \
    type                TEXT, \
    app_name            TEXT, \
    app_topvas_plugins  INTEGER, \
    app_topvas_cves     TEXT, \
    app_topvas_version  TEXT, \
    app_ness_plugins    INTEGER, \
    app_ness_cves       TEXT, \
    app_ness_version    TEXT, \
    reserve1        TEXT, \
    reserve2        TEXT, \
    reserve3        TEXT, \
    PRIMARY KEY ( id, app_name ) );'

    #2 创建根据cve统计出来的结果表count_import_plugins_cves
    cu.execute(ctb_import_plugins_cves)
    cu.execute('delete from count_import_plugins_cves where 1=1;')
    print("##Create Table count_import_plugins_cves Success!!!")
    #3 将基本配置数据插入到表base_info中
    for k in range(0, len(insert_sql)):
        #print('insert sql:' + insert_sql[k])
        try:
            cu.execute(insert_sql[k])
        except:
            print('insert sql error:' + insert_sql[k])

    print("##Insert data to count_import_plugins_cves Success!!!")

    #4 根据文件名或family统计需要移植的插件
    result_count = cu.execute('select type, file_name, family_topvas, family_ness from base_info order by id;')
    all_info_rt = result_count.fetchall()
    id = 0
    for info_rt in all_info_rt:
        id = id + 1
        app_type = info_rt[0]
        app_name = info_rt[1]
        family_topvas = info_rt[2]
        family_ness = info_rt[3]
        print('############################################################################################')
        print('type:' + app_type + ',  file:' + app_name + ',  family_topvas:' + family_topvas + ',  family_ness:' + family_ness)
        #########for topvas
        if app_name == 'windows':
            where_sql_topvas = 'where script_family like \'%' + app_name + '%\''
        elif family_topvas == '':
            where_sql_topvas = 'where file_name like \'%' + app_name + '%\''
        else:
            where_sql_topvas = 'where file_name like \'%' + app_name + '%\' and ' + 'script_family = \'' + family_topvas + '\''
        app_topvas_plugins_sql = 'select count(*) from topvas_info '
        app_topvas_cve = 'select script_cve_id from topvas_info '
        print('##TOPVAS SQL##:' + app_topvas_plugins_sql + where_sql_topvas)
        results = cu.execute(app_topvas_plugins_sql + where_sql_topvas)
        all_info = results.fetchall()
        for info in all_info:
            app_topvas_plugins = info[0]
            print('topvas num:' + str(app_topvas_plugins))
        result_cve = cu.execute(app_topvas_cve + where_sql_topvas)
        all_info_cve = result_cve.fetchall()
        count = 0
        app_topvas_cves = ''
        for info_cve in all_info_cve:
            app_topvas_cves_list = info_cve[0].replace(' ', '').replace('\t', '')
            #print('list:' + app_topvas_cves_list)
            if app_topvas_cves_list == '':
                continue
            else:
                count = count + 1
                if count == 1:
                    app_topvas_cves = app_topvas_cves_list
                else:
                    if ',' in app_topvas_cves_list:
                        cves = app_topvas_cves_list.split(',')
                        for j in range(0, len(cves)):
                            if cves[j] not in app_topvas_cves:
                                app_topvas_cves = app_topvas_cves + ',' + cves[j]
                    elif app_topvas_cves_list not in app_topvas_cves:
                        app_topvas_cves = app_topvas_cves + ',' + app_topvas_cves_list
        #print('##########topvas###########\nid=' + str(id) + ',app_name:' + app_name+ ',plugins_count:' + str(app_topvas_plugins) + ',cves:' + app_topvas_cves)
    
        #########for ness
        if app_name == 'windows':
            where_sql_ness = 'where script_family like \'%' + app_name + '%\''
        elif family_ness == '':
            where_sql_ness = 'where file_name like \'%' + app_name + '%\''
        else:
            where_sql_ness = 'where file_name like \'%' + app_name + '%\' and ' + 'script_family = \'' + family_ness + '\''
        app_ness_plugins_sql = 'select count(*) from ness_results '
        app_ness_cve = 'select script_cve_id from ness_results '
        print('##NESS SQL##:' + app_ness_plugins_sql + where_sql_ness)
        results_ness = cu.execute(app_ness_plugins_sql + where_sql_ness)
        all_info_ness = results_ness.fetchall()
        for info_ness in all_info_ness:
            app_ness_plugins = info_ness[0]
            print('ness nums:' + str(app_ness_plugins))
        result_cve_ness = cu.execute(app_ness_cve + where_sql_ness)
        all_info_cve_ness = result_cve_ness.fetchall()
        count = 0
        app_ness_cves = ''
        for info_cve_ness in all_info_cve_ness:
            app_ness_cves_list = info_cve_ness[0].replace(' ', '').replace('\t', '')
            #print('list:' + app_ness_cves_list)
            if app_ness_cves_list == '':
                continue
            else:
                count = count + 1
                if count == 1:
                    app_ness_cves = app_ness_cves_list
                else:
                    if ',' in app_ness_cves_list:
                        cves = app_ness_cves_list.split(',')
                        for j in range(0, len(cves)):
                            if cves[j] not in app_ness_cves:
                                app_ness_cves = app_ness_cves + ',' + cves[j]
                    elif app_ness_cves_list not in app_ness_cves:
                        app_ness_cves = app_ness_cves + ',' + app_ness_cves_list
        #print('##########ness###########\nid=' + str(id) + ',app_name:' + app_name+ ',plugins_count:' + str(app_ness_plugins) + ',cves:' + app_ness_cves)
        insert_sql = 'insert into count_import_plugins_cves(id, type, app_name, app_topvas_plugins, app_topvas_cves, app_ness_plugins, app_ness_cves) \
            values(' + str(id) + ',\'' + app_type + '\',\'' + app_name + '\',' + str(app_topvas_plugins) + ',\'' + app_topvas_cves + '\',' + str(app_ness_plugins) + ',\'' + app_ness_cves + '\');'
        #print('sql:' + insert_sql)
        try:
            cu.execute(insert_sql)
        except:
            print('sql error:' + insert_sql)
 

#将数据插入到base_info表中
def count_import_plugins_func(cu):
    result_count = cu.execute('select type, file_name, family_topvas, family_ness from base_info order by id;')
    all_info_rt = result_count.fetchall()
    id = 0
    for info_rt in all_info_rt:
        id = id + 1
        app_type = info_rt[0]
        app_name = info_rt[1]
        family_topvas = info_rt[2]
        family_ness = info_rt[3]
        print('############################################################################################')
        print('type:' + app_type + ',  file:' + app_name + ',  family_topvas:' + family_topvas + ',  family_ness:' + family_ness)
        #########for topvas
        if app_name == 'windows':
            where_sql_topvas = 'where script_family like \'%' + app_name + '%\''
        elif family_topvas == '':
            where_sql_topvas = 'where file_name like \'%' + app_name + '%\''
        else:
            where_sql_topvas = 'where file_name like \'%' + app_name + '%\' and ' + 'script_family = \'' + family_topvas + '\''
        app_topvas_plugins_sql = 'select count(*) from topvas_info '
        app_topvas_file_name = 'select file_name from topvas_info '
        print('##TOPVAS SQL##:' + app_topvas_plugins_sql + where_sql_topvas)
        results = cu.execute(app_topvas_plugins_sql + where_sql_topvas)
        all_info = results.fetchall()
        for info in all_info:
            app_topvas_plugins = info[0]
            print('topvas num:' + str(app_topvas_plugins))
        result_file_name = cu.execute(app_topvas_file_name + where_sql_topvas)
        all_info_file = result_file_name.fetchall()
        count = 0
        app_topvas_file = ''
        for info_file in all_info_file:
            app_topvas_file_list = info_file[0].replace(' ', '').replace('\t', '')
            #print('list:' + app_topvas_cves_list)
            app_topvas_file = app_topvas_file + '  ' + app_topvas_file_list
        #print('##########topvas###########\nid=' + str(id) + ',app_name:' + app_name+ ',plugins_count:' + str(app_topvas_plugins) + ',cves:' + app_topvas_cves)

        #########for ness
        if app_name == 'windows':
            where_sql_ness = 'where script_family like \'%' + app_name + '%\''
        elif family_ness == '':
            where_sql_ness = 'where file_name like \'%' + app_name + '%\''
        else:
            where_sql_ness = 'where file_name like \'%' + app_name + '%\' and ' + 'script_family = \'' + family_ness + '\''
        app_ness_plugins_sql = 'select count(*) from ness_results '
        app_ness_file = 'select file_name from ness_results '
        print('##NESS SQL##:' + app_ness_plugins_sql + where_sql_ness)
        results_ness = cu.execute(app_ness_plugins_sql + where_sql_ness)
        all_info_ness = results_ness.fetchall()
        for info_ness in all_info_ness:
            app_ness_plugins = info_ness[0]
            print('ness nums:' + str(app_ness_plugins))
        result_cve_file = cu.execute(app_ness_file + where_sql_ness)
        all_info_file_ness = result_cve_file.fetchall()
        count = 0
        app_ness_file = ''
        for info_file_ness in all_info_file_ness:
            app_ness_file_list = info_file_ness[0].replace(' ', '').replace('\t', '')
            #print('list:' + app_ness_cves_list)
            app_ness_file = app_ness_file + '  ' + app_ness_file_list
        #print('##########ness###########\nid=' + str(id) + ',app_name:' + app_name+ ',plugins_count:' + str(app_ness_plugins) + ',cves:' + app_ness_cves)
        insert_sql = 'insert into count_import_plugins_files(id, type, app_name, app_topvas_plugins, app_topvas_files, app_ness_plugins, app_ness_files) \
            values(' + str(id) + ',\'' + app_type + '\',\'' + app_name + '\',' + str(app_topvas_plugins) + ',\'' + app_topvas_file + '\',' + str(app_ness_plugins) + ',\'' + app_ness_file + '\');'
        #print('sql:' + insert_sql)
        try:
            cu.execute(insert_sql)
        except:
            print('sql error:' + insert_sql)

    print("#############insert data to topvas_transfer_info OK!##########")


def transfer_plugins_func(cu):
    #qry_sql = 'select app_name, app_ness_files, app_ness_plugins from count_import_plugins_files where id in(8,23);'
    qry_sql = 'select app_name, app_ness_files, app_ness_plugins  from count_import_plugins_files where 1=1;'

    os.system('mkdir -p /usr/local/nessus_plugin/bak/ &&rm -rf /usr/local/nessus_plugin/bak/*')

    qry_results = cu.execute(qry_sql)
    all_info_file = qry_results.fetchall()
    for info_ness in all_info_file:
        app_names = info_ness[0]
        ness_files = info_ness[1]
        ness_files_count = info_ness[2]
        #1.创建app目录
        NESS_PATH = '/usr/local/nessus_plugin/bak/ns_' + app_names
        cmd_mkdir = 'mkdir -p ' + NESS_PATH
        os.system(cmd_mkdir)
        NESS_PATH_INC = NESS_PATH + '/inc'
        cmd_mkdir_inc = 'mkdir -p ' + NESS_PATH_INC
        os.system(cmd_mkdir_inc)
        if ness_files_count == 0:
            continue
        #2.拷贝ness插件到对应目录
        cmd_cp_ness = 'cd /usr/local/nessus_plugin/ness_plugins && cp ' + ness_files + ' ' + NESS_PATH
        os.system(cmd_cp_ness)
        #3.目录备份
        cmd_cp_bak = 'cp -rf ' + NESS_PATH + ' ' + NESS_PATH + '_bak'
        print('bak:' + cmd_cp_bak)
        os.system(cmd_cp_bak)
        #4.插件头文件替换
        #cmd_cd = "cd " + NESS_PATH
        #cmd_sed_inc = cmd_cd + "&& grep -rl \"include(\\\"compat.inc\\\");\" ./ | xargs sed -i 's/include(\"compat.inc\");/include(\"ns_compat.inc\");/g'"
        #print('cmd_inc:' + cmd_sed_inc)
        #os.system(cmd_sed_inc)
        #4.1 查找头文件
        inc_array = []  #用于保存头文件数组
        cmd_find_inc = 'find ' + NESS_PATH + ' -name *.nasl|xargs grep \"include(\"'
        print('find:' + cmd_find_inc)
        r_find = os.popen(cmd_find_inc) #执行该命令
        info_find = r_find.readlines()  #读取命令行的输出到一个list
        find_inc_temp = ''
        for line in info_find:  #按行遍历
            #print('line:' + line)
            list = line.split('"')
            if len(list) == 1:
                continue
            find_inc_temp = list[1]
            #print('inc:' + find_inc_temp)
            inc_array.append(find_inc_temp)

        #4.2 数组去重
        inc_array_new = []
        for inc_str in inc_array:
            if inc_str not in inc_array_new and inc_str != 'global_settings.inc':
                inc_array_new.append(inc_str)
        print(inc_array_new)

        #4.3 拷贝头文件并修改头文件
        cmd_cd = "cd " + NESS_PATH
        for inc_str in inc_array_new:
            cmd_cp_inc = 'cp /usr/local/nessus_plugin/ness_plugins/' + inc_str + ' ' + NESS_PATH_INC + '/ns_' + inc_str
            #print('sed cmd:' +cmd_cp_inc)
            os.system(cmd_cp_inc)
            cmd_sed_inc = cmd_cd + "&& grep -rl " + inc_str + " ./ | xargs sed -i 's/" + inc_str + "/" + "ns_" + inc_str + "/g'"
            print('sed cmd:' +cmd_sed_inc)
            os.system(cmd_sed_inc)
    
        #4.4 修改函数
        cmd_func1 = cmd_cd + " && grep -rl \"audit(\" ./ | xargs sed -i 's/audit(/audit_ns(/g'"
        cmd_func2 = cmd_cd + " && grep -rl \"exit(0,\" ./ | xargs sed -i 's/exit(0,/exit_ns(exit_code:0, msg:/g'"
        cmd_func3 = cmd_cd + " && grep -rl \"exit(1,\" ./ | xargs sed -i 's/exit(1,/exit_ns(exit_code:1, msg:/g'"
        cmd_func4 = cmd_cd + " && grep -rl \"get_service(\" ./ | xargs sed -i 's/get_service(/get_service_ns(/g'"
        cmd_func5 = cmd_cd + " && grep -rl \"english:\" ./ | xargs sed -i 's/english://g'"
        cmd_func6 = cmd_cd + " && grep -rl \"script_dependencie(\" ./ | xargs sed -i 's/script_dependencie(/script_dependencies(/g'"        
        
        os.system(cmd_func1)
        os.system(cmd_func2)
        os.system(cmd_func3)
        os.system(cmd_func4)
        os.system(cmd_func5)
        os.system(cmd_func6)

    print("#############plugins transfer OK!##########")


if __name__=="__main__": 
    #####0. 打开数据库
    cx = sqlite3.connect('/usr/local/openvas-src/src/db/topvas_plugins.db')
    cu = cx.cursor()
    print("########0.Open DB OK!!!")

    #####1. 解析ness插件(ness_info)
    print("########1.Analysis nessus plugins Info Begin")
    #1.1 新建表ness_info
    ctb_script_info = 'create table if not exists ness_info  \
    ( \
    id                  INTEGER, \
    file_name           TEXT NOT NULL, \
    file_type           TEXT, \
    script_id           TEXT NOT NULL,  \
    script_name         TEXT NOT NULL, \
    script_category     TEXT NOT NULL,   \
    script_family       TEXT, \
    script_cve_id       TEXT, \
    transplant          TEXT default(1), \
    reserve1             TEXT, \
    reserve2             TEXT, \
    reserve3             TEXT, \
    PRIMARY KEY (id,file_name) \
    )'
    cu.execute(ctb_script_info)
    print("##Create Table ness_info Success!!!")

    #cu.execute('CREATE INDEX file_name_index ON ness_info(id,file_name);')
    #cu.execute('CREATE INDEX family_index ON ness_info(script_family);')
    #cu.execute('CREATE INDEX cve_index ON ness_info(script_cve_id);')
    #cu.execute('CREATE INDEX category_index ON ness_info(script_category);')

    #NESS_PATH = '/usr/local/nessus_plugin/mysql/'
    #NESS_PATH = '/usr/local/temp/'
    NESS_PATH = '/usr/local/nessus_plugin/ness_plugins/'

    #1.2 统计ness目录下的nasl插件数量
    cmd_find_ness = 'cd ' + NESS_PATH + "  && find . -name \"*.nasl\"|wc -l"
    r_find_count = os.popen(cmd_find_ness) #执行该命令
    info_find = r_find_count.readlines()  #读取命令行的输出到一个list
    find_inc_temp = ''
    for line in info_find:  #按行遍历
        count_ness_files = line;
    print('count Dir Ness plugins numbers:' + count_ness_files)

    #1.3 统计数据库中ness_info表总数
    ness_results = cu.execute("select count(*) from ness_info where 1=1;")
    all_info_ness = ness_results.fetchall()
    for info_ne in all_info_ness:
        sql_ness_plugins_count = info_ne[0]
    print('count DB Ness plugins numbers:' + str(sql_ness_plugins_count))

    NESS_FLAGS = False
    #1.4 作比较，判断是否需要重新解析插件信息到db中
    #如果ness目录下的插件数和db数据库中的插件数相同，则不需要重新解析插件信息到db中
    
    if sql_ness_plugins_count != int(count_ness_files):
        print('not equal')
        NESS_FLAGS = True
        cu.execute("delete from ness_info where 1=1;")
        count_ness = 0
        for filename in os.listdir(NESS_PATH):
            if os.path.splitext(filename)[1] == '.nasl':
                count_ness = count_ness + 1
                script_file = NESS_PATH + filename
                if count_ness%1000 == 0:
                    print('ness id=' + str(count_ness))
                fr_nasl = open(script_file)
                #获取ness插件数据，并组成insert sql语句
                insert_sql = get_ness_script_info(filename , fr_nasl, count_ness)
                try:
                    cu.execute(insert_sql)
                except:
                    print("error:" + insert_sql)
                fr_nasl.close()
        cu.execute('update ness_info  set script_family = trim(script_family) where 1=1;')
    else:
        print('ness plugins files is equal with DB counts;')  

    
    print("########1.Analysis nessus plugins Info End")
    
    #####2. 解析topvas插件(topvas_info)
    print("########2.Analysis topvas plugins Info Begin")
    #2.1 创建表topvas_info
    ctb_script_info = 'create table if not exists topvas_info  \
    ( \
    oid                  INTEGER, \
    file_name           TEXT NOT NULL, \
    file_type           TEXT, \
    script_id           TEXT NOT NULL,  \
    script_name         TEXT NOT NULL, \
    script_category     TEXT NOT NULL,   \
    script_family       TEXT, \
    script_cve_id       TEXT, \
    transplant          TEXT default(1), \
    reserve1             TEXT, \
    reserve2             TEXT, \
    reserve3             TEXT, \
    PRIMARY KEY (oid,file_name) \
    )'
    cu.execute(ctb_script_info)
    print("##Create Table topvas_info Success!!!")
    #cu.execute('CREATE INDEX file_name_index2 ON topvas_info(oid,file_name);')
    #cu.execute('CREATE INDEX family_index2 ON topvas_info(script_family);')
    #cu.execute('CREATE INDEX cve_index2 ON topvas_info(script_cve_id);')
    #cu.execute('CREATE INDEX category_index2 ON topvas_info(script_category);')

    #TOPVAS_PATH = '/usr/local/nessus_plugin/mysql/'
    #TOPVAS_PATH = '/usr/local/temp/'
    TOPVAS_PATH = '/usr/local/topvas_base_20180705/'

    #2.2 统计topvas目录下的nasl插件数量
    cmd_find_topvas = 'cd ' + TOPVAS_PATH + "  && find . -name \"*.nasl\"|wc -l"
    r_find_count = os.popen(cmd_find_topvas) #执行该命令
    info_find = r_find_count.readlines()  #读取命令行的输出到一个list
    find_inc_temp = ''
    for line in info_find:  #按行遍历
        count_topvas_files = line;
    print('count Dir topvas plugins numbers:' + count_topvas_files)

    #2.3 统计数据库中ness_info表总数
    topvas_results = cu.execute("select count(*) from topvas_info where 1=1;")
    all_info_topvas = topvas_results.fetchall()
    for info_top in all_info_topvas:
        sql_topvas_count = info_top[0]
    print('count DB topvas plugins numbers:' + str(sql_topvas_count))

    #2.4 作比较，判断是否需要重新解析插件信息到db中
    #如果ness目录下的插件数和db数据库中的插件数相同，则不需要重新解析插件信息到db中
    TOPVAS_FLAGS = False
    if sql_topvas_count != int(count_topvas_files):
        TOPVAS_FLAGS = True
        cu.execute("delete from topvas_info where 1=1;")
        search_file(TOPVAS_PATH, '.nasl', cu)
    else:
        print('topvas plugins files is equal with DB counts;')  
        

    cu.execute('update topvas_info  set script_family = trim(script_family) where 1=1;')
    cu.execute('update topvas_info  set script_family = \'FTP\' where script_family = \"	 FTP\";')
    print("########2.Analysis topvas plugins Info End")

    #####3. 通过cve获取需要移植的ness插件(ness_results)
    print("########3.Compare CVE by ness && topvas plugins Info Gegin")
    #3.1 创建表ness_results
    ctb_ness_results = 'create table if not exists ness_results  \
    ( \
    id                  INTEGER, \
    file_name           TEXT NOT NULL, \
    script_cve_id       TEXT, \
    script_id           INTEGER, \
    script_name         TEXT, \
    script_category     TEXT, \
    script_family       TEXT, \
    reserve1            TEXT, \
    reserve2            TEXT, \
    reserve3            TEXT, \
    PRIMARY KEY (id,file_name) \
    );'
    cu.execute(ctb_ness_results)
    print("##Create Table ness_results Success!!!")

    #3.2 判断是否需要重新更新需要移植的插件内容ness_results
    if NESS_FLAGS == True and TOPVAS_FLAGS == True:
        cu.execute('delete from ness_results where 1=1;')
        # 执行语句
        sql_select_ness_results = "select id,  \
              file_name,  \
              script_cve_id,  \
              script_id, \
              script_name, \
              script_category, \
              script_family from ness_info \
              where 1=1;"
        results = cu.execute(sql_select_ness_results)
        # 遍历打印输出
        count_ness_results = 0
        all_info = results.fetchall()
        for info in all_info:
            id = info[0]
            file_name = info[1]
            script_id = info[3]
            script_name = info[4]
            script_category = info[5]
            script_family = info[6]
            cve = info[2].replace(' ', '')
            list = cve.split(',')
            #print(list)
            where_cve_in = ''
            insert_flag = 0
            for i in range(0, len(list)):
                sql_select = 'select count(*) from nvt_cves where cve_name = \'' + list[i] + '\''
                #print("sql_select:" + sql_select)
                ret = cu.execute(sql_select)
                all_info_1 = ret.fetchall()
                for info_1 in all_info_1:
                    if info_1[0] == 0:
                        insert_flag = 1
                        break
            if insert_flag == 1:
                count_ness_results = count_ness_results + 1
                sql_insert_head = 'insert into ness_results(id, file_name, script_cve_id, script_id, script_name, script_category, script_family) values('
                insert_script_name = script_name.replace('\'', '\'\'')
                sql_insert_value = str(count_ness_results) + ',\'' + file_name + '\',\'' + cve + '\',\'' + script_id + '\',\'' + insert_script_name + '\',\'' + script_category + '\',\'' + script_family +'\');'
                sql_insert = sql_insert_head + sql_insert_value
                if count_ness_results%100 == 0:
                    print("ness results=" + str(count_ness_results))
                try:
                    cu.execute(sql_insert)
                except:
                    print("insert error:" + sql_insert) 
    else:
        print('No need to update table ness_results')

    print("########3.Compare CVE by ness && topvas plugins Info End")

    #####4. 统计重要插件移植(base_info , count_import_plugins_cves)
    print("########4.Count Import Plugins by file_name Begin")
    insert_data_base_info(cu)
    print("########4.Count Import Plugins by file_name End")

    #####5. 自动化移植重要插件(base_info, count_import_plugins_files)
    print("########5.Auto Transter Import Plugins Begin")
    ctb_count_import_plugins_files = 'create table if not exists count_import_plugins_files ( \
    id              INTEGER, \
    type                TEXT, \
    app_name            TEXT, \
    app_topvas_plugins  INTEGER, \
    app_topvas_files     TEXT, \
    app_topvas_version  TEXT, \
    app_ness_plugins    INTEGER, \
    app_ness_files       TEXT, \
    app_ness_version    TEXT, \
    reserve1        TEXT, \
    reserve2        TEXT, \
    reserve3        TEXT, \
    PRIMARY KEY ( id, app_name ) );'

    #5.1 创建表count_import_plugins_files
    cu.execute(ctb_count_import_plugins_files)
    cu.execute('delete from count_import_plugins_files where 1=1;')
    print('create table count_import_plugins_files Success!')

    #5.2 统计文件
    count_import_plugins_func(cu)

    #5.3 开始移植插件
    transfer_plugins_func(cu)
    print("########5.Auto Transter Import Plugins End")
    
#关闭游标
    cu.close()

#事务提交
    cx.commit()

#关闭数据库
    cx.close()

    print("All Success!")
