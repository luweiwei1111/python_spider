#coding=utf-8
import urllib.request
from HandleJs import Py4Js
import threading
import sqlite3
import time
from google_translate import GoogleTranslate
from sqlite3_sql import Sql
import sys
import importlib
importlib.reload(sys)
#sys.setdefaultencoding('utf8')

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

class Plugins(object):
    """docstring for Plugins"""
    Tag_name_en = ('summary',
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
    def __init__(self, Tag_name_en):
        super(Plugins, self).__init__()
        self.Tag_name_en = Tag_name_en
        

    def upgrate_tag():
        #更新tag数据
        result_tag = Sql.select_tag_oid()
        for info in result_tag:
            oid = info[0]
            tag = info[1]
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

            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("#oid->%s ,tag->%s" %(oid, tag))
            if tag != 'NOTAG':
                tag_list = tag.split('|')
                for tag_info in tag_list:
                    #print('####tag:' + tag_info + '####')
                    tag_name_info = tag_info.split('=')[0]
                    tag_name_desc = tag_info.split('=')[1]
                    if tag_name_info == 'summary':
                        summary_cn = tag_name_desc.replace('\'', '\'\'')
                        print('summary=%s' %(summary_cn) )
                    elif tag_name_info == 'affected':
                        affected_cn = tag_name_desc.replace('\'', '\'\'')
                        print('affected=%s' %(affected_cn) )
                    elif tag_name_info == 'solution':
                        solution_cn = tag_name_desc.replace('\'', '\'\'')
                        print('solution=%s' %(solution_cn) )
                    elif tag_name_info == 'insight':
                        insight_cn = tag_name_desc.replace('\'', '\'\'')
                        print('insight=%s' %(insight_cn) )
                    elif tag_name_info == 'vuldetect':
                        vuldetect_cn = tag_name_desc.replace('\'', '\'\'')
                        print('vuldetect=%s' %(vuldetect_cn) )
                    elif tag_name_info == 'impact':
                        impact_cn = tag_name_desc.replace('\'', '\'\'')
                        print('impact=%s' %(impact_cn) )
                    elif tag_name_info == 'synopsis':
                        synopsis_cn = tag_name_desc.replace('\'', '\'\'')
                        print('synopsis=%s' %(synopsis_cn) )
                    elif tag_name_info == 'description':
                        description_cn = tag_name_desc.replace('\'', '\'\'')
                        print('description=%s' %(description_cn) )
                    elif tag_name_info == 'exploitability_ease':
                        exploitability_ease_cn = tag_name_desc.replace('\'', '\'\'')
                        print('exploitability_ease=%s' %(exploitability_ease_cn) )
                    elif tag_name_info == 'risk_factor':
                        risk_factor_cn = tag_name_desc.replace('\'', '\'\'')
                        print('risk_factor=%s' %(risk_factor_cn) )
                    elif tag_name_info == 'metasploit_name':
                        metasploit_name_cn = tag_name_desc.replace('\'', '\'\'')
                        print('metasploit_name=%s' %(metasploit_name_cn) )
                    elif tag_name_info == 'd2_elliot_name':
                        d2_elliot_name_cn = tag_name_desc.replace('\'', '\'\'')
                        print('d2_elliot_name=%s' %(d2_elliot_name_cn) )
                print('begin update')
                Sql.update_blog_blogspost_en(cls, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name)

    
#创建表 blog_blogspost 并插入数据
def crt_tbl_blog_blogspost(cu, max_num, flag, all_data_flag):
    #创建索引
    index_oid = 'CREATE INDEX oid_idx_1 ON blog_blogspost (oid );'
    index_cn_ok = 'CREATE INDEX cn_ok_idx_1 ON blog_blogspost (cn_ok );'
    index_oid_cn_ok = 'CREATE INDEX oid_cn_ok_idx_1 ON blog_blogspost (oid,cn_ok );'

    #####创建表 blog_blogspost 并插入数据
    #只有入参为True，则需要重新构建 blog_blogspost 里面的数据
    print('flag=' + str(flag))
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
           family                  TEXT, \
           family_cn               TEXT);'
        print('##->1.Create Table blog_blogspost Success')
        cu.execute(ctl_nvts_cn)
        #索引
        cu.execute(index_oid)
        cu.execute(index_cn_ok)
        cu.execute(index_oid_cn_ok)

        #插入数据
        all_data_flag = True
        if all_data_flag == True:
            insert_sql = 'insert into blog_blogspost(oid,name,tag,family) select oid,name,tag,family from nvts  ORDER BY id;'
        else:
            insert_sql = 'insert into blog_blogspost(oid,name,tag,family) select oid,name,tag,family from nvts  ORDER BY id LIMIT ' + str(max_num) + ';'  

        print('##->' + insert_sql)
        cu.execute(insert_sql)

        #更新tag数据
        upgrate_tag(cu)

    
    """
    1.对比blog_blogspost表和nvts表，将blog_blogspost存在，但是nvts表不存在的数据删除;
    2.将nvts表中存在，但是blog_blogspost存在的数据插入到blog_blogpost
    此操作目的是再与nvts表更新后，blogs_blogspost与之不匹配，作为数据统一同步的功能
    """
    nvts_oid_index = 'CREATE INDEX nvts_by_oid on nvts(oid);'
    del_sql = 'delete  from blog_blogspost  where not exists (select * from nvts  where nvts.oid =blog_blogspost.oid);'
    add_sql = 'insert into blog_blogspost(oid,name,tag,family) select t1.oid,t1.name,t1.tag,t1.family from nvts t1 where not exists (select * from blog_blogspost t2 where t1.oid = t2.oid)'
    #创建oid的索引
    print('#############update###############')
    try:
        print(nvts_oid_index)
        cu.execute(nvts_oid_index)
    except:
        print('create index error:' + nvts_oid_index)
        pass

    try:
        print(del_sql)
        cu.execute(del_sql)
    except:
        cu.execute('delete data sql failed:' + del_sql)

    try:
        print(add_sql)
        cu.execute(add_sql)
    except:
        cu.execute('add data sql failed:' + add_sql)
    #####创建表 nvts_en 并插入数据
    try:
        cu.execute('drop table if exists nvts_en')
    except:
        print('drop table nvts_en failed')

    print('############update################')
    #数据更新完落后，更新tag
    upgrate_tag(cu)
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
    insert_sql = 'insert into nvts_en(oid , name, tag, cn_ok,\
        summary, affected, solution, insight, vuldetect, impact, synopsis, description,\
        exploitability_ease, risk_factor, metasploit_name, d2_elliot_name) select oid , name, tag, cn_ok, ' + \
        'summary, affected, solution, insight, vuldetect, impact, synopsis, description,' + \
        ' exploitability_ease, risk_factor, metasploit_name, d2_elliot_name ' + \
        'from blog_blogspost where cn_ok = \'0\'' #and family not in' + \
        #'(\'IT-Grundschutz-11\',\'IT-Grundschutz-10\',\'IT-Grundschutz\',\'IT-Grundschutz-12\',\'IT-Grundschutz-15\', \'IT-Grundschutz-13\')  ORDER BY id ;'
    
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

def data_process(all_nvts, cur, conn):
    nvts_tag = ''
    error_oid_list = []
    global gl_Tag_name_cn
    global gl_count_nvts
    nvts_oid = ''
    google_translate = GoogleTranslate()
    for info_nvts in all_nvts:
        gl_count_nvts = gl_count_nvts + 1
        nvts_id = info_nvts[0]
        nvts_oid = info_nvts[1]
        nvts_name = info_nvts[2]
        nvts_summary = info_nvts[3]
        nvts_affected = info_nvts[4]
        nvts_solution = info_nvts[5]
        nvts_insight = info_nvts[6]
        nvts_vuldetect = info_nvts[7]
        nvts_impact = info_nvts[8]
        nvts_synopsis = info_nvts[9]
        nvts_description = info_nvts[10]
        nvts_exploitability_ease = info_nvts[11]
        nvts_risk_factor = info_nvts[12]
        nvts_metasploit_name = info_nvts[13]
        nvts_d2_elliot_name = info_nvts[14]

        #1.name
        nvts_name_cn = ''
        if '' != nvts_name:
            try:
                nvts_name_cn = google_translate.translate_cn(nvts_name, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi Name error:oid=' + nvts_oid + ', name=' + nvts_name)
                continue

        #2.summary
        nvts_summary_cn = ''
        if '' != nvts_summary:
            try:
                nvts_summary_cn = google_translate.translate_cn(nvts_summary, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi summary error:oid=' + nvts_oid + ', summary=' + nvts_summary)
                continue

        #3.affected
        nvts_affected_cn = ''
        if '' != nvts_affected:
            try:
                nvts_affected_cn = google_translate.translate_cn(nvts_affected, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi affected error:oid=' + nvts_oid + ', affected=' + nvts_affected)
                continue
        
        #4.solution
        nvts_solution_cn = ''
        if '' != nvts_solution:
            try:
                nvts_solution_cn = google_translate.translate_cn(nvts_solution, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi solution error:oid=' + nvts_oid + ', solution=' + nvts_solution)
                continue

        #5.insight
        nvts_insight_cn = ''
        if '' != nvts_insight:
            try:
                #text.decode("utf-8").
                nvts_insight_cn = google_translate.translate_cn(nvts_insight, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi insight error:oid=' + nvts_oid + ', insight=' + nvts_insight)
                continue


        #6.vuldetect
        nvts_vuldetect_cn = ''
        if '' != nvts_vuldetect:
            try:
                nvts_vuldetect_cn = google_translate.translate_cn(nvts_vuldetect, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi vuldetect error:oid=' + nvts_oid + ', vuldetect=' + nvts_vuldetect)
                continue

        #7.impact
        nvts_impact_cn = ''
        if '' != nvts_impact:
            try:
                nvts_impact_cn = google_translate.translate_cn(nvts_impact, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi impact error:oid=' + nvts_oid + ', impact=' + nvts_impact)
                continue

        #8.synopsis
        nvts_synopsis_cn = ''
        if '' != nvts_synopsis:
            try:
                nvts_synopsis_cn = google_translate.translate_cn(nvts_synopsis, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi synopsis error:oid=' + nvts_oid + ', synopsis=' + nvts_synopsis)
                continue

        #9.description
        nvts_description_cn = ''
        if '' != nvts_description:
            try:
                nvts_description_cn = google_translate.translate_cn(nvts_description, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi description error:oid=' + nvts_oid + ', description=' + nvts_description)
                continue

        #10.exploitability_ease
        nvts_exploitability_ease_cn = ''
        if '' != nvts_exploitability_ease:
            try:
                nvts_exploitability_ease_cn = google_translate.translate_cn(nvts_exploitability_ease, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi exploitability_ease error:oid=' + nvts_oid + ', exploitability_ease=' + nvts_exploitability_ease)
                continue

        #11.risk_factor
        nvts_risk_factor_cn = ''
        if '' != nvts_risk_factor:
            try:
                nvts_risk_factor_cn = google_translate.translate_cn(nvts_risk_factor, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi risk_factor error:oid=' + nvts_oid + ', risk_factor=' + nvts_risk_factor)
                continue

        #12.metasploit_name
        nvts_metasploit_name_cn = ''
        if '' != nvts_metasploit_name:
            try:
                nvts_metasploit_name_cn = google_translate.translate_cn(nvts_metasploit_name, 'en').replace('\'', '\'\'').replace('\\n', '\n')
            except:
                print('#->fanyi metasploit_name error:oid=' + nvts_oid + ', metasploit_name=' + nvts_metasploit_name)
                continue

        #13.d2_elliot_name
        nvts_d2_elliot_name_cn = ''
        if '' != nvts_d2_elliot_name:
            try:
                nvts_d2_elliot_name_cn = google_translate.translate_cn(nvts_d2_elliot_name, 'de').replace('\'', '\'\'').replace('\\n', '\n')
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
            conn.commit()
        except:
            print('#ERROR#->update sql error:' + update_sql)
            continue

if __name__ == "__main__":
    #2.获取需要翻译的标签，并放入到全局变量数组gl_Tag_name_cn中
    #get_tag_info(cu)
    

    #统计nvts_en数据量
    ret_count = cu.execute('select count(*) from blog_blogspost where cn_ok = \'0\';')
    nvt_num_info = ret_count.fetchall()
    for info_n in nvt_num_info:
        count_nvts_number = info_n[0]

    #关闭游标
    cu.close()
    #事务提交
    cx.commit()
    #关闭数据库
    cx.close()
