import sqlite3
import os

conn = sqlite3.connect('/usr/local/openvas-src/src/db/topvas_plugins.db')
cursor = conn.cursor()


insert_sql = [\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(1, \'常用操作系统\', \'windows\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(2, \'常用操作系统\', \'centos\', \'CentOS Local Security Checks\', \'CentOS Local Security Checks\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(3, \'常用操作系统\', \'ubuntu\', \'Ubuntu Local Security Checks\', \'Ubuntu Local Security Checks\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(4, \'常用操作系统\', \'suse\',   \'SuSE Local Security Checks\',   \'SuSE Local Security Checks\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(5, \'大数据组件\', \'hadoop\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(6, \'大数据组件\', \'zookeeper\', \'Fedora Local Security Checks\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(7, \'虚拟化平台\', \'vmware\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(8, \'虚拟化平台\', \'esxi\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(9, \'虚拟化平台\', \'xen\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(10, \'虚拟化平台\', \'xenserver\', \'Citrix Xenserver Local Security Checks\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(11, \'虚拟化平台\', \'hyper_v\', \'Windows : Microsoft Bulletins\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(12, \'应用中间件\', \'apache\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(13, \'应用中间件\', \'iis\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(14, \'应用中间件\', \'weblogic\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(15, \'应用中间件\', \'websphere\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(16, \'应用中间件\', \'tomcat\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(17, \'应用中间件\', \'nginx\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(18, \'数据库\', \'mysql\', \'Databases\', \'Databases\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(19, \'数据库\', \'mssql\', \'Databases\', \'Databases\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(20, \'数据库\', \'db2\', \'Databases\', \'Databases\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(21, \'国产数据库\', \'dameng\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(22, \'国产数据库\', \'gbase\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(23, \'网络设备\', \'h3c\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(24, \'网络设备\', \'cisco\', \'cisco\', \'cisco\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(25, \'网络设备\', \'juniper\', \'General\', \'Junos Local Security Checks\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(26, \'网络设备\', \'huawei\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(27, \'网络设备\', \'maipu\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(28, \'网络设备\', \'zte\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(29, \'网络设备\', \'f5\', \'F5 Local Security Checks\', \'F5 Networks Local Security Checks\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(30, \'网络设备\', \'checkpoint\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(31, \'国产安全设备\', \'启明\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(32, \'国产安全设备\', \'nsfocus\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(33, \'国产安全设备\', \'360 safe\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(34, \'国产安全设备\', \'山石\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(35, \'国产安全设备\', \'深信服\', \'\', \'\')',\
    'insert into count_info(id, type, file_name, family_topvas, family_ness) values(36, \'国产安全设备\', \'topsec\', \'\', \'\')'\
    ]

ctb_results = 'create table if not exists count_info ( \
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
cursor.execute(ctb_results)
cursor.execute('delete from count_info where 1=1;')
print('create table count_info Success!')

ctb_results = 'create table if not exists count_results ( \
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

#创建表ness_results
cursor.execute(ctb_results)
cursor.execute('delete from count_results where 1=1;')
print('create table count_results Success!')

for k in range(0, len(insert_sql)):
    #print('insert sql:' + insert_sql[k])
    try:
        cursor.execute(insert_sql[k])
    except:
        print('insert sql error:' + insert_sql[k])

print('insert data to  table count_info Success!')

result_count = cursor.execute('select type, file_name, family_topvas, family_ness from count_info order by id;')
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
    results = cursor.execute(app_topvas_plugins_sql + where_sql_topvas)
    all_info = results.fetchall()
    for info in all_info:
        app_topvas_plugins = info[0]
        print('topvas num:' + str(app_topvas_plugins))
    result_cve = cursor.execute(app_topvas_cve + where_sql_topvas)
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
    results_ness = cursor.execute(app_ness_plugins_sql + where_sql_ness)
    all_info_ness = results_ness.fetchall()
    for info_ness in all_info_ness:
        app_ness_plugins = info_ness[0]
        print('ness nums:' + str(app_ness_plugins))
    result_cve_ness = cursor.execute(app_ness_cve + where_sql_ness)
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
    insert_sql = 'insert into count_results(id, type, app_name, app_topvas_plugins, app_topvas_cves, app_ness_plugins, app_ness_cves) \
        values(' + str(id) + ',\'' + app_type + '\',\'' + app_name + '\',' + str(app_topvas_plugins) + ',\'' + app_topvas_cves + '\',' + str(app_ness_plugins) + ',\'' + app_ness_cves + '\');'
    #print('sql:' + insert_sql)
    try:
        cursor.execute(insert_sql)
    except:
        print('sql error:' + insert_sql)
        



#关闭游标
cursor.close()

#事务提交
conn.commit()

#关闭数据库
conn.close()

print("insert data to count_results OK!")

