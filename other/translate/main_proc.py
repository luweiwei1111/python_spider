#coding=utf-8
from google_translate import GoogleTranslate
from sqlite3_sql import Sql
from plugins_data import Plugins

INSERT_FLAG = 'continue'

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

# 为线程定义一个函数
def nomal_data_proc(threadName, min, max):
    #counter = 0
    #conn.isolation_level = None
    #conn.row_factory = sqlite3.Row
    #cur = conn.cursor()
    sql = 'select id, oid, name, summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name from nvts_en where cn_ok = \'0\' and id >' + str(min) + ' and id <= ' + str(max)
    print(threadName + ' sql:' + sql)

    results = Sql.sql_execute(sql)
    data_process(results, cur, conn)
    #conn.commit()

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
        print("##->progress=" + str(gl_count_nvts))
        Sql.sql_execute(update_sql)

def continue_process():
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
    Sql.sql_execute(del_sql)
    Sql.sql_execute(add_sql)

def data_proc():
    if INSERT_FLAG == 'first':
        Sql.delete_tb_blog_blogspost()
        sql = 'insert into blog_blogspost(oid,name,tag,family) select oid,name,tag,family from nvts  ORDER BY id;'
        Sql.sql_execute(sql)
    else:
        #继续处理
        continue_process()
    
    #更新tag数据内容的英文信息
    Plugins.upgrate_tag()

if __name__ == "__main__":
    #创建表
    Sql.ctl_tb_blog_blogspost()

    #数据处理
    data_proc()

    data_proc()

    count_num = 10000
    while True:
        try:
            count_num = count_num + 1
            threadName = 'Thread-' + str(count_num)
            min = THTREA_LEN * (count_num -1)
            max = THTREA_LEN * count_num
            if min > count_nvts_number:
                break
            if max >= count_nvts_number:
                max = count_nvts_number
            # init thread
            data_proc = threading.Thread(target = nomal_data_proc, args = (threadName, min, max))
            #start thread
            data_proc.start()
            if max >= count_nvts_number:
                break
        except:
            print("Error: unable to start thread")

"""
    #update family
    family_cn = ''
    family_info = Sql.select_family()
    for familys in family_info:
        family = familys[0]
        print(family)
        family_cn = google_translate.translate_cn(family, 'en')
        print(family_cn)
        Sql.update_family_cn(family_cn, family)

    #对于不符合规范的翻译进行人工校准
    Sql.update_family_auth()
    """