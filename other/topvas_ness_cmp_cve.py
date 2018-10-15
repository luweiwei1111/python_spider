import sqlite3
import os

conn = sqlite3.connect('/usr/local/openvas-src/src/db/topvas_plugins.db')
cursor = conn.cursor()

ctb_results = 'create table if not exists ness_results  \
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
#创建表ness_results
cursor.execute(ctb_results)
cursor.execute('delete from ness_results where 1=1;')

# 执行语句
sql = "select id,  \
              file_name,  \
              script_cve_id,  \
              script_id, \
              script_name, \
              script_category, \
              script_family from script_info \
              where 1=1;"
results = cursor.execute(sql)

# 遍历打印输出
count = 0

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
      ret = cursor.execute(sql_select)
      all_info_1 = ret.fetchall()
      for info_1 in all_info_1:
        if info_1[0] == 0:
            insert_flag = 1
            break
    if insert_flag == 1:
        count = count + 1
        sql_insert_head = 'insert into ness_results(id, file_name, script_cve_id, script_id, script_name, script_category, script_family) values('
        insert_script_name = script_name.replace('\'', '\'\'')
        sql_insert_value = str(count) + ',\'' + file_name + '\',\'' + cve + '\',\'' + script_id + '\',\'' + insert_script_name + '\',\'' + script_category + '\',\'' + script_family +'\');'
        sql_insert = sql_insert_head + sql_insert_value
        print("count=" + str(count))
        try:
            cursor.execute(sql_insert)
        except:
            print("insert error:" + sql_insert) 

#关闭游标
cursor.close()

#事务提交
conn.commit()

#关闭数据库
conn.close()

print("insert ness_results data OK!")

