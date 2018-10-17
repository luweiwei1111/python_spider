#coding=utf-8
import urllib2
from HandleJs import Py4Js
import threading
import sqlite3
import sys
import time
from translate import Translator

"""
使用Google翻译nvts表中的
name, 
summary, 
affected, 
solution, 
insight, 
vuldetect, 
impact, 
synopsis, 
description, 
exploitability_ease, 
risk_factor, 
metasploit_name, 
d2_elliot_name
并保存到表blog_blogspost表中，用于Django网站显示，并修改对应的中文数据。
"""
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id <' + str(gl_proc_max_1)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_1) + ' and id <' + str(gl_proc_max_2)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_2) + ' and id <' + str(gl_proc_max_3)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_3) + ' and id <' + str(gl_proc_max_4)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_4) + ' and id <' + str(gl_proc_max_5)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_5) + ' and id <' + str(gl_proc_max_6)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_6) + ' and id <' + str(gl_proc_max_7)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_7) + ' and id <' + str(gl_proc_max_8)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_8) + ' and id <' + str(gl_proc_max_9)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_9) + ' and id <' + str(gl_proc_max_10)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_10) + ' and id <' + str(gl_proc_max_11)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_11) + ' and id <' + str(gl_proc_max_12)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_12) + ' and id <' + str(gl_proc_max_13)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_13) + ' and id <' + str(gl_proc_max_14)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_14) + ' and id <' + str(gl_proc_max_15)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_15) + ' and id <' + str(gl_proc_max_16)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_16) + ' and id <' + str(gl_proc_max_17)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_17) + ' and id <' + str(gl_proc_max_18)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_18) + ' and id <' + str(gl_proc_max_19)
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
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >= ' + str(gl_proc_max_19)
    print('proc_20 sql:' + sql)
    cur.execute(sql)
    results = cur.fetchall()
    data_process(results, cur)
    time.sleep(0.5)
    

#创建表 blog_blogspost 并插入数据
def crt_tbl_blog_blogspost(cu, flag):
    #####创建表 blog_blogspost 并插入数据
    #只有入参为True，则需要重新构建 blog_blogspost 里面的数据
    if flag ==  False:
        print('first')
        try:
            cu.execute('drop table if exists blog_blogspost')
        except:
            print('drop table blog_blogspost failed')
        #创建表 blog_blogspost
        ctl_nvts_cn = 'create table if not exists blog_blogspost( \
           id           INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT, \
           oid          VARCHAR( 150 )  NOT NULL, \
           name         VARCHAR( 500 )  NOT NULL, \
           name_cn      VARCHAR( 500 ), \
           tag          TEXT, \
           cn_ok        VARCHAR( 10 ) default \'0\', \
           summary      TEXT, \
           summary_cn   TEXT, \
           affected     TEXT, \
           affected_cn  TEXT, \
           solution     TEXT, \
           solution_cn  TEXT, \
           insight      TEXT, \
           insight_cn   TEXT, \
           vuldetect    TEXT, \
           vuldetect_cn TEXT, \
           impact       TEXT, \
           impact_cn    TEXT, \
           synopsis     TEXT, \
           synopsis_cn  TEXT, \
           description  TEXT, \
           description_cn          TEXT, \
           exploitability_ease     TEXT, \
           exploitability_ease_cn  TEXT, \
           risk_factor             TEXT, \
           risk_factor_cn          TEXT, \
           metasploit_name         TEXT, \
           metasploit_name_cn      TEXT, \
           d2_elliot_name          TEXT, \
           d2_elliot_name_cn       TEXT, \
           family                  TEXT);'
        print('##->1.Create Table blog_blogspost Success')
        cu.execute(ctl_nvts_cn)

        #插入数据
        insert_sql = 'insert into blog_blogspost(oid,name,tag,family) select oid,name,tag,family from nvts  ORDER BY id;'
        
        print('##->' + insert_sql)
        cu.execute(insert_sql)

        #更新tag数据
        select_sql = 'select  oid, tag from blog_blogspost;'
        summary_cn = ''
        affected_cn = ''
        solution_cn = ''
        insight_cn = ''
        vuldetect_cn = ''
        impact_cn = ''
        synopsis_cn = ''
        description_cn = ''
        exploitability_ease_cn = ''
        risk_factor_cn = ''
        metasploit_name_cn = ''
        d2_elliot_name_cn = ''
        count_set = 0
        cu.execute(select_sql)
        result_tag = cu.fetchall()
        for info in result_tag:
            oid = info[0]
            tag = info[1]
            if tag != 'NOTAG':
                tag_list = tag.split('|')
                for tag_info in tag_list:
                    #print('####tag:' + tag_info + '####')
                    tag_name_info = tag_info.split('=')[0]
                    tag_name_desc = tag_info.split('=')[1]
                    if tag_name_info == 'summary':
                        summary_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'affected':
                        affected_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'solution':
                        solution_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'insight':
                        insight_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'vuldetect':
                        vuldetect_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'impact':
                        impact_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'synopsis':
                        synopsis_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'description':
                        description_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'exploitability_ease':
                        exploitability_ease_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'risk_factor':
                        risk_factor_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'metasploit_name':
                        metasploit_name_cn = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'd2_elliot_name':
                        d2_elliot_name_cn = tag_name_desc.replace('\'', '\'\'')
            set_sql = 'update blog_blogspost set ' + \
                        ' summary = \'' + summary_cn + '\',' + \
                        ' affected = \'' + affected_cn + '\',' + \
                        ' solution = \'' + solution_cn + '\',' + \
                        ' insight = \'' + insight_cn + '\',' + \
                        ' vuldetect = \'' + vuldetect_cn + '\',' + \
                        ' impact = \'' + impact_cn + '\',' + \
                        ' synopsis = \'' + synopsis_cn + '\',' + \
                        ' description = \'' + description_cn + '\',' + \
                        ' exploitability_ease = \'' + exploitability_ease_cn + '\',' + \
                        ' risk_factor = \'' + risk_factor_cn + '\',' + \
                        ' metasploit_name = \'' + metasploit_name_cn + '\',' + \
                        ' d2_elliot_name = \'' + d2_elliot_name_cn + '\'' + \
                        ' where oid = \'' + oid + '\''
            try:
                count_set = count_set + 1
                cu.execute(set_sql)
                print('##Set Progress##' + str(count_set))
            except:
                sys.exit('#error##set sql:' + set_sql)

    #####创建表 nvts_en 并插入数据
    try:
        cu.execute('drop table if exists nvts_en')
    except:
        print('drop table nvts_en failed')
    #创建表 nvts_en
    ctl_nvts_en = 'create table if not exists nvts_en( \
           id        INTEGER PRIMARY KEY AUTOINCREMENT, \
           oid       TEXT, \
           name      TEXT, \
           tag       TEXT, \
           cn_ok     TEXT default \'0\', \
           summary   TEXT, \
           affected  TEXT, \
           solution  TEXT, \
           insight   TEXT, \
           vuldetect TEXT, \
           impact    TEXT, \
           synopsis  TEXT, \
           description  TEXT, \
           exploitability_ease  TEXT, \
           risk_factor      TEXT, \
           metasploit_name  TEXT, \
           d2_elliot_name   TEXT);'

    cu.execute(ctl_nvts_en)
    print('##->2.Create Table nvts_en Success')

    #插入数据
    insert_sql = 'insert into nvts_en select id, oid , name, tag, cn_ok, ' + \
        'summary, affected, solution, insight, vuldetect, impact, synopsis, description,' + \
        ' exploitability_ease, risk_factor, metasploit_name, d2_elliot_name ' + \
        'from blog_blogspost where cn_ok = \'0\' and family not in' + \
        '(\'IT-Grundschutz-11\',\'IT-Grundschutz-10\',\'IT-Grundschutz\',\'IT-Grundschutz-12\',\'IT-Grundschutz-15\', \'IT-Grundschutz-13\')  ORDER BY id ;'
    
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
    #db_path = './db/tasks.db'
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
    nvts_oid = ''
    for info_nvts in all_nvts:
        gl_count_nvts = gl_count_nvts + 1
        nvts_id = info_nvts[0]
        nvts_oid = info_nvts[1]
        nvts_name = info_nvts[2]#.replace('\n', '')
        nvts_summary = info_nvts[3]#.replace('\n', '')
        nvts_affected = info_nvts[4]#.replace('\n', '')
        nvts_solution = info_nvts[5]#.replace('\n', '') 
        nvts_insight = info_nvts[6]#.replace('\n', '')
        nvts_vuldetect = info_nvts[7]#.replace('\n', '')
        nvts_impact = info_nvts[8]#.replace('\n', '')
        nvts_synopsis = info_nvts[9]#.replace('\n', '')
        nvts_description = info_nvts[10]#.replace('\n', '')
        nvts_exploitability_ease = info_nvts[11]#.replace('\n', '')
        nvts_risk_factor = info_nvts[12]#.replace('\n', '')
        nvts_metasploit_name = info_nvts[13]#.replace('\n', '')
        nvts_d2_elliot_name = info_nvts[14]#.replace('\n', '')

        #1.name
        nvts_name_cn = ''
        if '' != nvts_name:
            try:
                nvts_name_cn = translate_cn(nvts_name).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi Name error:oid=' + nvts_oid + ', name=' + nvts_name)
                continue

        #2.summary
        nvts_summary_cn = ''
        if '' != nvts_summary:
            try:
                nvts_summary_cn = translate_cn(nvts_summary).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi summary error:oid=' + nvts_oid + ', summary=' + nvts_summary)
                continue

        #3.affected
        nvts_affected_cn = ''
        if '' != nvts_affected:
            try:
                nvts_affected_cn = translate_cn(nvts_affected).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi affected error:oid=' + nvts_oid + ', affected=' + nvts_affected)
                continue
        
        #4.solution
        nvts_solution_cn = ''
        if '' != nvts_solution:
            try:
                nvts_solution_cn = translate_cn(nvts_solution).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi solution error:oid=' + nvts_oid + ', solution=' + nvts_solution)
                continue

        #5.insight
        nvts_insight_cn = ''
        if '' != nvts_insight:
            try:
                nvts_insight_cn = translate_cn(nvts_insight).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi insight error:oid=' + nvts_oid + ', insight=' + nvts_insight)
                continue


        #6.vuldetect
        nvts_vuldetect_cn = ''
        if '' != nvts_vuldetect:
            try:
                nvts_vuldetect_cn = translate_cn(nvts_vuldetect).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi vuldetect error:oid=' + nvts_oid + ', vuldetect=' + nvts_vuldetect)
                continue

        #7.impact
        nvts_impact_cn = ''
        if '' != nvts_impact:
            try:
                nvts_impact_cn = translate_cn(nvts_impact).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi impact error:oid=' + nvts_oid + ', impact=' + nvts_impact)
                continue

        #8.synopsis
        nvts_synopsis_cn = ''
        if '' != nvts_synopsis:
            try:
                nvts_synopsis_cn = translate_cn(nvts_synopsis).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi synopsis error:oid=' + nvts_oid + ', synopsis=' + nvts_synopsis)
                continue

        #9.description
        nvts_description_cn = ''
        if '' != nvts_description:
            try:
                nvts_description_cn = translate_cn(nvts_description).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi description error:oid=' + nvts_oid + ', description=' + nvts_description)
                continue

        #10.exploitability_ease
        nvts_exploitability_ease_cn = ''
        if '' != nvts_exploitability_ease:
            try:
                nvts_exploitability_ease_cn = translate_cn(nvts_exploitability_ease).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi exploitability_ease error:oid=' + nvts_oid + ', exploitability_ease=' + nvts_exploitability_ease)
                continue

        #11.risk_factor
        nvts_risk_factor_cn = ''
        if '' != nvts_risk_factor:
            try:
                nvts_risk_factor_cn = translate_cn(nvts_risk_factor).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi risk_factor error:oid=' + nvts_oid + ', risk_factor=' + nvts_risk_factor)
                continue

        #12.metasploit_name
        nvts_metasploit_name_cn = ''
        if '' != nvts_metasploit_name:
            try:
                nvts_metasploit_name_cn = translate_cn(nvts_metasploit_name).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi metasploit_name error:oid=' + nvts_oid + ', metasploit_name=' + nvts_metasploit_name)
                continue

        #13.d2_elliot_name
        nvts_d2_elliot_name_cn = ''
        if '' != nvts_d2_elliot_name:
            try:
                nvts_d2_elliot_name_cn = translate_cn(nvts_d2_elliot_name).replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi d2_elliot_name error:oid=' + nvts_oid + ', d2_elliot_name=' + nvts_d2_elliot_name)
                continue

        cn_nvts_tag = nvts_tag.replace('\'', '\'\'').replace('"', '""')
        update_sql = 'update blog_blogspost set cn_ok = \'1\',' + \
                'name_cn = \'' + nvts_name_cn + '\', ' + \
                'summary_cn = \'' + nvts_summary_cn + '\', ' + \
                'affected_cn = \'' + nvts_affected_cn + '\', ' + \
                'solution_cn = \'' + nvts_solution_cn + '\', ' + \
                'insight_cn = \'' + nvts_insight_cn + '\', ' + \
                'vuldetect_cn = \'' + nvts_vuldetect_cn + '\', ' + \
                'impact_cn = \'' + nvts_impact_cn + '\', ' + \
                'synopsis_cn = \'' + nvts_synopsis_cn + '\', ' + \
                'description_cn = \'' + nvts_description_cn + '\', ' + \
                'exploitability_ease_cn = \'' + nvts_exploitability_ease_cn + '\', ' + \
                'risk_factor_cn = \'' + nvts_risk_factor_cn + '\', ' + \
                'metasploit_name_cn = \'' + nvts_metasploit_name_cn + '\', ' + \
                'd2_elliot_name_cn = \'' + nvts_d2_elliot_name_cn + '\'  ' + \
                'where cn_ok = \'0\' and oid =\'' + nvts_oid + '\';'

        #print('##->Update Sql:' + update_sql)
        try:
            print("##->progress=" + str(gl_count_nvts))
            cur.execute(update_sql)
        except:
            print('#ERROR#->update sql error:' + update_sql)
            continue


# Example: find_last('aaaa', 'a') returns 3
# Make sure your procedure has a return statement.
def find_last(string,str):
    last_position=-1
    while True:
        position=string.find(str,last_position+1)
        if position==-1:
            return last_position
        last_position=position

def open_url(url):    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
    req = urllib2.Request(url = url,headers=headers)    
    response = urllib2.urlopen(req)    
    data = response.read().decode('utf-8')    
    return data    

def translate_core(content,tk):    
    if len(content) > 4891:    
        print("#ERROR#too long byte >4891")
        return

    content = urllib2.quote(content)    

    url = "http://translate.google.cn/translate_a/single?client=t"+ "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"+"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"+"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(tk,content)    

    #result为json格式
    result = open_url(url)    
    #print('results:' + result)

    if len(content) < 10:
        end = result.find("\",")  
        if end > 4:
            return result[4:end]
    else:
        result_all = ''
        result_all = result.split(',null,"en",null,null,')[0].replace('[[', '').replace(']]', ']')[1:]
        #print('result_all:' + result_all)

        output_cn = ''
        #解析中文字段并拼接
        list = result_all.split('],[')
        for i in range(len(list)-1):
            end = list[i].find("\",")
            tmp_buf = list[i][1:end]
            output_cn = output_cn + tmp_buf
        return output_cn

def translate_normal(content):    
    js = Py4Js()    

    tk = js.getTk(content)
    #print('english:' + content)
    cn_buf = translate_core(content,tk)
    #print('Chinese:' + cn_buf)
    return cn_buf

def translate_cn(content):
    LEN_LIMIT = 4891
    all_len = len(content)
    #print('en:' + content)
    if all_len > LEN_LIMIT:
        content_cn = ''
        while True:
            content_limit = content[0:LEN_LIMIT]
            limit_end = find_last(content_limit, '.') + 1
            #print('limit_end:' + str(limit_end))
            if limit_end == 0:
                limit_end = find_last(content_limit, ' ') + 1
                if limit_end == 0:
                    limit_end = LEN_LIMIT
            content_en = content[0:limit_end]
            leave_len = all_len - limit_end
            if content_en == '':
                break;
            #print('content_en:' + content_en)
            content_cn = content_cn + translate_normal(content_en);
            content = content[limit_end:]
 
        return content_cn
    else:
        return translate_normal(content)

#google api, per 1000 words everyday
def translate_cn_api(content):
    translator= Translator(to_lang="zh")
    translation = translator.translate(content)
    return translation

def main_core(continue_flag, db_path):
    global gl_Tag_name_cn
    global gl_count_nvts

    #  copy data
    cx = sqlite3.connect(db_path)
    cu = cx.cursor()

    #1.创建表并插入数据
    crt_tbl_blog_blogspost(cu, continue_flag)

    #2.获取需要翻译的标签，并放入到全局变量数组gl_Tag_name_cn中
    #get_tag_info(cu)

    #统计nvts_en数据量
    ret_count = cu.execute('select count(*) from blog_blogspost where cn_ok = \'0\';')
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
    print('proc_18=' + str(gl_proc_max_18))
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




if __name__ == "__main__":
    param_len = len(sys.argv)
    if param_len != 3:
        sys.exit('input param need 2,useage:python2.7 ' +sys.argv[0] + ' continue/first tasks.db')
    else:
        if 'continue' == sys.argv[1]:
            print('continue')
            continue_flag = True
        elif 'first' == sys.argv[1]:
            print('first')
            continue_flag = False
        else:
            sys.exit('input param error,useage:python2.7 ' +sys.argv[0] + ' continue/first tasks.db')

    #print('param 1:' + str(continue_flag))
    print('param 2:' + sys.argv[2])
    #db = './db/tasks_split_1.db'
    db = sys.argv[2]

    gl_proc_max_1 = 0
    gl_proc_max_2 = 0
    gl_proc_max_3 = 0
    gl_proc_max_4 = 0
    gl_proc_max_5 = 0
    gl_proc_max_6 = 0
    gl_proc_max_7 = 0
    gl_proc_max_8 = 0
    gl_proc_max_9 = 0
    gl_proc_max_10 = 0
    gl_proc_max_11 = 0
    gl_proc_max_12 = 0
    gl_proc_max_13 = 0
    gl_proc_max_14 = 0
    gl_proc_max_15 = 0
    gl_proc_max_16 = 0
    gl_proc_max_17 = 0
    gl_proc_max_18 = 0
    gl_proc_max_19 = 0

    gl_count_nvts = 0
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

    main_core(continue_flag, db)
