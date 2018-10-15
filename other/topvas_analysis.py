# coding=utf-8

import os
import sqlite3
import sys
import re
import os.path
import codecs


SCRIPT_ID_DEF  = 'script_oid'
SCRIPT_NAME_DEF = 'script_name'
SCRIPT_CATEGORY_DEF = 'script_category'
SCRIPT_FAMILY_DEF = 'script_family'

def get_script_info(file_name , fr_open, id_sqlite3):
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
            if SCRIPT_ID_DEF in line:
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
            elif SCRIPT_NAME_DEF in line:
                script_name = line.replace('script_name', '').replace('(', '').replace(')', '').replace('"', '').replace(';', '').replace('\'', '\'\'').replace('\n', '')
                #print('script_name:' + script_name)
            elif SCRIPT_CATEGORY_DEF in line:
                script_category = line.replace('script_category', '').replace('(', '').replace(')', '').replace('"', '').replace(' ', '').replace(';', '').replace('\n', '')
                #print('script_category:' + script_category)
            elif 'family =' in line:
                script_family = line.replace('family =', '').replace('=', '').replace('"', '').replace('\'', '').replace(';', '').replace('\n', '')
                #print('script_family1:###' + script_family + '#####' + file_name)
            elif SCRIPT_FAMILY_DEF in line:
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
        print('case_total_num = ' + str(case_total_num))
        #相对路径
        script_file = os.path.relpath(dir)
        filename = script_file.split('/')[-1]
        fr_nasl = codecs.open(script_file, 'r',encoding= u'utf-8',errors='ignore')
        insert_sql = get_script_info(filename , fr_nasl, case_total_num)
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
                                          # 对每个子目录路劲执行同样的操作
case_total_num = 0

if __name__=="__main__": 
    cx = sqlite3.connect('/usr/local/openvas-src/src/db/topvas_plugins.db')
    cu = cx.cursor()

#创建表
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
    #cu.execute('CREATE INDEX file_name_index2 ON topvas_info(oid,file_name);')
    #cu.execute('CREATE INDEX family_index2 ON topvas_info(script_family);')
    #cu.execute('CREATE INDEX cve_index2 ON topvas_info(script_cve_id);')
    #cu.execute('CREATE INDEX category_index2 ON topvas_info(script_category);')
    cu.execute("delete from topvas_info where 1=1;")

    #NESS_PATH = '/usr/local/nessus_plugin/mysql/'
    #NESS_PATH = '/usr/local/temp/'
    NESS_PATH = '/usr/local/topvas_base_20180705/'

    search_file(NESS_PATH, '.nasl', cu)
                
    cu.execute('update topvas_info  set script_family = trim(script_family) where 1=1;')
    cu.execute('update topvas_info  set script_family = \'FTP\' where script_family = \"	 FTP\";')
#关闭游标
    cu.close()

#事务提交
    cx.commit()

#关闭数据库
    cx.close()

    print("insert data OK!")
