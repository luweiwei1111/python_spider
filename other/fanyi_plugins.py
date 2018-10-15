from urllib  import request
from urllib  import parse
import json
import time
import threading
import sqlite3
import sys

def nomal_data_proc_1(conn):
    '''
    @summary: data1 defination
    '''
    counter = 0
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_1
    # select data
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id <' + str(gl_proc_max_1)
    print('proc_1 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5) 

def nomal_data_proc_2(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_1
    global gl_proc_max_2
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_1) + ' and id <' + str(gl_proc_max_2)
    print('proc_2 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_3(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_2
    global gl_proc_max_3
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_2) + ' and id <' + str(gl_proc_max_3)
    print('proc_3 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_4(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_3
    global gl_proc_max_4
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_3) + ' and id <' + str(gl_proc_max_4)
    print('proc_4 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_5(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_4
    global gl_proc_max_5
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_4) + ' and id <' + str(gl_proc_max_5)
    print('proc_5 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_6(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_5
    global gl_proc_max_6
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_5) + ' and id <' + str(gl_proc_max_6)
    print('proc_6 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_7(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_6
    global gl_proc_max_7
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_6) + ' and id <' + str(gl_proc_max_7)
    print('proc_7 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_8(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_7
    global gl_proc_max_8
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_7) + ' and id <' + str(gl_proc_max_8)
    print('proc_8 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_9(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_8
    global gl_proc_max_9
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_8) + ' and id <' + str(gl_proc_max_9)
    print('proc_9 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_10(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_9
    global gl_proc_max_10
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_9) + ' and id <' + str(gl_proc_max_10)
    print('proc_10 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_11(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_10
    global gl_proc_max_11
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_10) + ' and id <' + str(gl_proc_max_11)
    print('proc_11 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_12(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_11
    global gl_proc_max_12
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_11) + ' and id <' + str(gl_proc_max_12)
    print('proc_12 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_13(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_12
    global gl_proc_max_13
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_12) + ' and id <' + str(gl_proc_max_13)
    print('proc_13 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_14(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_13
    global gl_proc_max_14
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_13) + ' and id <' + str(gl_proc_max_14)
    print('proc_14 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_15(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_14
    global gl_proc_max_15
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_14) + ' and id <' + str(gl_proc_max_15)
    print('proc_15 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_16(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_15
    global gl_proc_max_16
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_15) + ' and id <' + str(gl_proc_max_16)
    print('proc_16 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_17(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_16
    global gl_proc_max_17
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_16) + ' and id <' + str(gl_proc_max_17)
    print('proc_17 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_18(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_17
    global gl_proc_max_18
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_17) + ' and id <' + str(gl_proc_max_18)
    print('proc_18 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_19(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_18
    global gl_proc_max_19
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_18) + ' and id <' + str(gl_proc_max_19)
    print('proc_19 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)

def nomal_data_proc_20(conn):
    '''
    @summary: data2 defination
    '''
    conn.isolation_level = None
    conn.row_factory = sqlite3.Row
    global gl_proc_max_19
    
    cur = conn.cursor()
    sql = 'select id, oid, name, tag from nvts_en where cn_ok = 0 and id >= ' + str(gl_proc_max_19)
    print('proc_20 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)
    

#创建表nvts_cn并插入数据
def crt_tbl_nvts_cn(cu, max_num, flag):
    #####创建表 nvts_cn 并插入数据
    #只有入参为True，则需要重新构建nvts_cn里面的数据
    print('flag=' + str(flag))
    if flag ==  False:
        print('first')
        try:
            cu.execute('drop table if exists nvts_cn')
        except:
            print('drop table nvts_cn failed')
        #创建表 nvts_cn
        ctl_nvts_cn = 'create table if not exists nvts_cn( \
           id        INTEGER PRIMARY KEY AUTOINCREMENT, \
           oid       TEXT, \
           name      TEXT, \
           tag       TEXT, \
           cn_ok     INTEGER default 0, \
           reserve1  TEXT, \
           reserve2  TEXT, \
           reserve3  TEXT);'

        print('##->1.Create Table nvts_cn Success')
        cu.execute(ctl_nvts_cn)
        

        #插入数据
        #insert_sql = 'insert into nvts_cn(oid,name,tag) select oid,name,tag from nvts  ORDER BY id LIMIT ' + str(max_num) + ';'
        insert_sql = 'insert into nvts_cn(oid,name,tag) select oid,name,tag from nvts  ORDER BY id ;'
        
        print('##->' + insert_sql)
        cu.execute(insert_sql)

    #####创建表 nvts_en 并插入数据
    try:
        cu.execute('drop table if exists nvts_en')
    except:
        print('drop table nvts_en failed')
    #创建表 nvts_en
    ctl_nvts_cn = 'create table if not exists nvts_en( \
       id        INTEGER PRIMARY KEY AUTOINCREMENT, \
       oid       TEXT, \
       name      TEXT, \
       tag       TEXT, \
       cn_ok     INTEGER default 0, \
       reserve1  TEXT, \
       reserve2  TEXT, \
       reserve3  TEXT);'

    cu.execute(ctl_nvts_cn)
    print('##->2.Create Table nvts_en Success')

    #插入数据
    insert_sql = 'insert into nvts_en(oid,name,tag) select oid,name,tag from nvts_cn where cn_ok = 0  ORDER BY id ;'
    
    print('##->' + insert_sql)
    cu.execute(insert_sql)

#获取需要翻译的标签，并放入到全局变量数组gl_Tag_name_cn中
def get_tag_info(cu):
    tag_name_en_list = ('cvss_base_vector',
                        'qod_type',
                        'solution_type',
                        'plugin_modification_date',
                        'cvss2_base_score',
                        'plugin_type',
                        'patch_publication_date',
                        'plugin_publication_date',
                        'cvss_temporal_vector',
                        'cvss_temporal_score',
                        'exploit_available',
                        'exploit_framework_core',
                        'vuln_publication_date',
                        'qod',
                        'deprecated',
                        'cpe',
                        'cvss3_vector',
                        'cvss3_temporal_vector',
                        'potential_vulnerability',
                        'exploited_by_malware',
                        'exploit_framework_metasploit',
                        'exploit_framework_canvas',
                        'canvas_package',
                        'stig_severity',
                        'unsupported_by_vendor',
                        'in_the_news',
                        'exploithub_sku',
                        'exploit_framework_exploithub',
                        'agent',
                        'exploited_by_nessus',
                        'exploit_framework_d2_elliot',
                        'default_account',
                        'see_also'
                        'NOTAG')

    nvts_select_sql = 'select oid, name,tag from nvts_en ;'
    print('##->' + nvts_select_sql)
    result_nvts = cu.execute(nvts_select_sql)
    all_nvts = result_nvts.fetchall()

    #用于保存tag的数据
    tag_name_tmp = []
    global gl_Tag_name_cn

    for info_nvts in all_nvts:
        nvts_tag = info_nvts[2]
        #此处需要解析标签
        tag_list = nvts_tag.split('|')
        for tag_info in tag_list:
            #print('####tag:' + tag_info + '####')
            tag_name_info = tag_info.split('=')[0]
            #print('##tag_name=' + tag_name_info + '##')
            if tag_name_info not in tag_name_en_list:
                tag_name_tmp.append(tag_name_info)

    #tag去重
    for tag in tag_name_tmp:
        if tag not in gl_Tag_name_cn:
            gl_Tag_name_cn.append(tag)

    #tag遍历
    for tag in gl_Tag_name_cn:
        print('cn tag:' + tag)

def fanyi_world_cn(string):
    url="https://fanyi.so.com/index/search"
    db_path = './db/tasks.db'
    Form_Data= {}
	
    #这里输入要翻译的英文
    Form_Data['query']= string
    Form_Data['eng']= '1'

    #用urlencode把字典变成字符串，#服务器不接受字典，只接受字符串和二进制
    data= parse.urlencode(Form_Data).encode('utf-8')

    #改成服务器可识别的数据后，请求，获取回应数据
    response= request.urlopen(url, data)

    html= response.read().decode("utf-8")#解码方式

    #java中的对象（集合）和数组（元素为集合）,loads可转Python字典
    result= json.loads(html)

    #字典调取键名data下的键名fanyi,获取其值
    translate_result= result["data"]["fanyi"]
    #print(translate_result)
    return translate_result

def fanyi_world(string):
    translate_result = '转码测试程序'
    return translate_result

def data_process(all_nvts, cur):
    nvts_tag = ''
    error_oid_list = []
    global gl_Tag_name_cn
    global gl_count_nvts
    for info_nvts in all_nvts:
        gl_count_nvts = gl_count_nvts + 1
        nvts_id = info_nvts[0]
        nvts_oid = info_nvts[1]
        nvts_name = info_nvts[2]
        nvts_tag_tmp = info_nvts[3]

        try:
            in_nvts_name = nvts_name.replace('\'', '\'\'').replace('"', '""')
            cn_nvts_name = fanyi_world_cn(in_nvts_name)
            #cn_nvts_name = fanyi_world(nvts_name)
        except:
            print('#->fanyi Name error:oid=' + nvts_oid + ', name=' + in_nvts_name)
            #保存翻译超时的oid列表
            error_oid_list.append(nvts_oid)
            pass
        #此处需要解析标签
        tag_list = nvts_tag_tmp.split('|')
        count_tag = 0
        #print('################ FANYI ######################')
        for tag_info in tag_list:
            #print('#tag:' + tag_info)
            tag_name_info = tag_info.split('=')[0]
            tag_name_desc_en = tag_info.split('=')[1]
            #print('###tag_name=' + tag_name_info + '###')
            if tag_name_info not in gl_Tag_name_cn:
                if count_tag == 0:
                    nvts_tag = tag_info
                else:
                    nvts_tag = nvts_tag + '|' + tag_info
                
            else:
                #需要翻译
                try:
                    tag_name_desc_cn = fanyi_world_cn(tag_name_desc_en)
                    #tag_name_desc_cn = fanyi_world(tag_name_desc_en)
                #except OSError:
                except:
                    print('#->fanyi tag_desc error:oid=' + nvts_oid + ', ' + tag_name_info + '=' + tag_name_desc_en)
                    #保存翻译超时的oid列表
                    error_oid_list.append(nvts_oid)
                    pass
                tag_info_cn = tag_name_info + '=' + tag_name_desc_cn
                if count_tag == 0:
                    nvts_tag = tag_info_cn
                else:
                    nvts_tag = nvts_tag + '|' + tag_info_cn
            count_tag = count_tag + 1

        #print('####TAG CN->' + nvts_tag)
        cn_nvts_tag = nvts_tag.replace('\'', '\'\'').replace('"', '""')
        update_sql = 'update nvts_cn set cn_ok = 1, name = \'' + cn_nvts_name + \
                            '\', tag = \'' + cn_nvts_tag + '\'  ' + \
                            'where cn_ok = 0 and oid =\'' + nvts_oid + '\';'

        #print('##->Update Sql' + update_sql)
        try:
            print("##->progress=" + str(gl_count_nvts))
            cur.execute(update_sql)
        except:
            print('#ERROR#->update sql error:' + update_sql)


if __name__ == "__main__":
    gl_Tag_name_cn = []
    gl_count_nvts = 0
    max_num = 200

    param_len = len(sys.argv)
    if param_len != 2:
        sys.exit('input param need 2,useage:python3 ' +sys.argv[0] + ' continue/first')
    else:
        if 'continue' == sys.argv[1]:
            print('continue')
            continue_flag = True
        elif 'first' == sys.argv[1]:
            print('first')
            continue_flag = False
        else:
            sys.exit('input param error,useage:python3 ' +sys.argv[0] + ' continue/first')

    #  copy data
    db_path = './db/tasks.db'
    cx = sqlite3.connect(db_path)
    cu = cx.cursor()

    #1.创建表并插入数据
    crt_tbl_nvts_cn(cu, max_num, continue_flag)
    #2.获取需要翻译的标签，并放入到全局变量数组gl_Tag_name_cn中
    get_tag_info(cu)

    #统计nvts_en数据量
    ret_count = cu.execute('select count(*) from nvts_en where cn_ok = 0;')
    nvt_num_info = ret_count.fetchall()
    for info_n in nvt_num_info:
        count_nvts_number = info_n[0]

    Max_Process = 20
    #count_nvts_number = 40
    tmp = int(count_nvts_number/Max_Process)
    gl_proc_max_1 = tmp
    gl_proc_max_2 = gl_proc_max_1 + tmp
    gl_proc_max_3 = gl_proc_max_2 + tmp
    gl_proc_max_4 = gl_proc_max_3 + tmp
    gl_proc_max_5 = gl_proc_max_4 + tmp
    gl_proc_max_6 = gl_proc_max_5 + tmp
    gl_proc_max_7 = gl_proc_max_6 + tmp
    gl_proc_max_8 = gl_proc_max_7 + tmp
    gl_proc_max_9 = gl_proc_max_8 + tmp
    gl_proc_max_10 = gl_proc_max_9 + tmp
    gl_proc_max_11 = gl_proc_max_10 + tmp
    gl_proc_max_12 = gl_proc_max_11 + tmp
    gl_proc_max_13 = gl_proc_max_12 + tmp
    gl_proc_max_14 = gl_proc_max_13 + tmp
    gl_proc_max_15 = gl_proc_max_14 + tmp
    gl_proc_max_16 = gl_proc_max_15 + tmp
    gl_proc_max_17 = gl_proc_max_16 + tmp
    gl_proc_max_18 = gl_proc_max_17 + tmp
    gl_proc_max_19 = gl_proc_max_18 + tmp
    
    #gl_proc_max_10 = gl_proc_max_9 + tmp

    print('###Max Num=' + str(count_nvts_number))
    print('###Process Num=' + str(Max_Process))
    print('proc_1=' + str(gl_proc_max_1))
    print('proc_2=' + str(gl_proc_max_2))
    print('proc_3=' + str(gl_proc_max_3))
    print('proc_4=' + str(gl_proc_max_4))
    print('proc_5=' + str(gl_proc_max_5))
    print('proc_6=' + str(gl_proc_max_6))
    print('proc_7=' + str(gl_proc_max_7))
    print('proc_8=' + str(gl_proc_max_8))
    print('proc_9=' + str(gl_proc_max_9))
    print('proc_10=' + str(gl_proc_max_10))
    print('proc_11=' + str(gl_proc_max_11))
    print('proc_12=' + str(gl_proc_max_12))
    print('proc_13=' + str(gl_proc_max_3))
    print('proc_14=' + str(gl_proc_max_14))
    print('proc_15=' + str(gl_proc_max_15))
    print('proc_16=' + str(gl_proc_max_16))
    print('proc_17=' + str(gl_proc_max_17))
    print('proc_18=' + str(gl_proc_max_8))
    print('proc_19=' + str(gl_proc_max_19))

    #关闭游标
    cu.close()
    #事务提交
    cx.commit()
    #关闭数据库
    cx.close()

    # 3.init db
    conn = sqlite3.connect(db_path, check_same_thread = False)

    # init thread
    data_proc_1 = threading.Thread(target = nomal_data_proc_1, args = (conn,))
    data_proc_2 = threading.Thread(target = nomal_data_proc_2, args = (conn,))
    data_proc_3 = threading.Thread(target = nomal_data_proc_3, args = (conn,))
    data_proc_4 = threading.Thread(target = nomal_data_proc_4, args = (conn,))
    data_proc_5 = threading.Thread(target = nomal_data_proc_5, args = (conn,))
    data_proc_6 = threading.Thread(target = nomal_data_proc_6, args = (conn,))
    data_proc_7 = threading.Thread(target = nomal_data_proc_7, args = (conn,))
    data_proc_8 = threading.Thread(target = nomal_data_proc_8, args = (conn,))
    data_proc_9 = threading.Thread(target = nomal_data_proc_9, args = (conn,))
    data_proc_10 = threading.Thread(target = nomal_data_proc_10, args = (conn,))
    data_proc_11 = threading.Thread(target = nomal_data_proc_11, args = (conn,))
    data_proc_12 = threading.Thread(target = nomal_data_proc_12, args = (conn,))
    data_proc_13 = threading.Thread(target = nomal_data_proc_13, args = (conn,))
    data_proc_14 = threading.Thread(target = nomal_data_proc_14, args = (conn,))
    data_proc_15 = threading.Thread(target = nomal_data_proc_15, args = (conn,))
    data_proc_16 = threading.Thread(target = nomal_data_proc_16, args = (conn,))
    data_proc_17 = threading.Thread(target = nomal_data_proc_17, args = (conn,))
    data_proc_18 = threading.Thread(target = nomal_data_proc_18, args = (conn,))
    data_proc_19 = threading.Thread(target = nomal_data_proc_19, args = (conn,))
    data_proc_20 = threading.Thread(target = nomal_data_proc_20, args = (conn,))

    #start threads
    data_proc_1.start()
    data_proc_2.start()        
    data_proc_3.start()
    data_proc_4.start()
    data_proc_5.start()
    data_proc_6.start()        
    data_proc_7.start()
    data_proc_8.start()
    data_proc_9.start()
    data_proc_10.start()
    data_proc_11.start()
    data_proc_12.start()        
    data_proc_13.start()
    data_proc_14.start()
    data_proc_15.start()
    data_proc_16.start()        
    data_proc_17.start()
    data_proc_18.start()
    data_proc_19.start()
    data_proc_20.start()
    
