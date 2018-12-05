#coding=utf-8
import urllib.request
import threading
import sqlite3
import time
from Google_translate.GoogleTS import GoogleTranslate
from sqlite3piplines.data_sync import SyncData
from sqlite3piplines.sqlite3_sql import Sql


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
class PluginsThread:
    def __init__(self):
        self.count_progress = 0
        self.Tag_all_name_en = []
        self.Tag_name_en = ('summary',
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

    def nomal_data_proc(self, threadName, min, max, google_translate):
        results = Sql.select_nvts_en_limit(min, max)
        self.data_process(results, google_translate)

    #获取需要翻译的标签，并放入到全局变量数组Tag_all_name_en中
    def get_tag_info(self, sync_data):
        all_nvts = Sql.select_tag_from_nvts()

        for info_nvts in all_nvts:
            tag_data = info_nvts[0]
            if tag_data != 'NOTAG':
                dict_data = sync_data.data_to_dict(tag_data, '=', '|')
                for key in dict_data:
                    if key not in self.Tag_all_name_en:
                        self.Tag_all_name_en.append(key)

        for tag in self.Tag_all_name_en:
            print('#nvts tag:' + tag)

    def translate_family(self, google_translate):
        #翻译family
        results_family = Sql.select_family_from_blog_blogspost()
        for family_info in results_family:
            family = family_info[0]
            print('##family:' + family)
            try:
                family_cn = google_translate.translate_cn(family)
            except:
                print('#->fanyi family error:family=%s' %(family))
                continue
            Sql.update_blog_blogspost_by_family(family_cn, family)

    def data_process(self, all_nvts, google_translate):
        for info_nvts in all_nvts:
            self.count_progress = self.count_progress + 1
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
                    nvts_name_cn = google_translate.translate_cn(nvts_name).replace('\'', '\'\'').replace('\\n', '\n')
                    nvts_name = nvts_name.replace('\'', '\'\'')
                except:
                    print('#->fanyi Name error:oid=' + nvts_oid + ', name=' + nvts_name)
                    continue

            #2.summary
            nvts_summary_cn = ''
            if '' != nvts_summary:
                try:
                    nvts_summary_cn = google_translate.translate_cn(nvts_summary).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi summary error:oid=' + nvts_oid + ', summary=' + nvts_summary)
                    continue

            #3.affected
            nvts_affected_cn = ''
            if '' != nvts_affected:
                try:
                    nvts_affected_cn = google_translate.translate_cn(nvts_affected).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi affected error:oid=' + nvts_oid + ', affected=' + nvts_affected)
                    continue
            
            #4.solution
            nvts_solution_cn = ''
            if '' != nvts_solution:
                try:
                    nvts_solution_cn = google_translate.translate_cn(nvts_solution).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi solution error:oid=' + nvts_oid + ', solution=' + nvts_solution)
                    continue

            #5.insight
            nvts_insight_cn = ''
            if '' != nvts_insight:
                try:
                    #text.decode("utf-8").
                    nvts_insight_cn = google_translate.translate_cn(nvts_insight).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi insight error:oid=' + nvts_oid + ', insight=' + nvts_insight)
                    continue

            #6.vuldetect
            nvts_vuldetect_cn = ''
            if '' != nvts_vuldetect:
                try:
                    nvts_vuldetect_cn = google_translate.translate_cn(nvts_vuldetect).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi vuldetect error:oid=' + nvts_oid + ', vuldetect=' + nvts_vuldetect)
                    continue

            #7.impact
            nvts_impact_cn = ''
            if '' != nvts_impact:
                try:
                    nvts_impact_cn = google_translate.translate_cn(nvts_impact).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi impact error:oid=' + nvts_oid + ', impact=' + nvts_impact)
                    continue

            #8.synopsis
            nvts_synopsis_cn = ''
            if '' != nvts_synopsis:
                try:
                    nvts_synopsis_cn = google_translate.translate_cn(nvts_synopsis).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi synopsis error:oid=' + nvts_oid + ', synopsis=' + nvts_synopsis)
                    continue

            #9.description
            nvts_description_cn = ''
            if '' != nvts_description:
                try:
                    nvts_description_cn = google_translate.translate_cn(nvts_description).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi description error:oid=' + nvts_oid + ', description=' + nvts_description)
                    continue

            #10.exploitability_ease
            nvts_exploitability_ease_cn = ''
            if '' != nvts_exploitability_ease:
                try:
                    nvts_exploitability_ease_cn = google_translate.translate_cn(nvts_exploitability_ease).replace('\'', '\'\'').replace('\\n', '\n')
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
                    nvts_d2_elliot_name_cn = google_translate.translate_cn(nvts_d2_elliot_name).replace('\'', '\'\'').replace('\\n', '\n')
                except:
                    print('#->fanyi d2_elliot_name error:oid=' + nvts_oid + ', d2_elliot_name=' + nvts_d2_elliot_name)
                    continue

            print("##->progress=" + str(self.count_progress))

            Sql.update_blog_blogspost_cn(nvts_name_cn, nvts_summary_cn, nvts_affected_cn, nvts_solution_cn, nvts_insight_cn, nvts_vuldetect_cn, nvts_impact_cn, nvts_synopsis_cn, nvts_description_cn, nvts_exploitability_ease_cn, nvts_risk_factor_cn, nvts_metasploit_name_cn, nvts_d2_elliot_name_cn, nvts_oid, nvts_name)

    def start_thread(self, max_thread, all_numbers, google_translate):
        THTREA_LEN = int(all_numbers/max_thread)
        print('THTREA_LEN=' + str(THTREA_LEN))

        # 创建两个线程
        count_num = 0
        while True:
            count_num = count_num + 1
            threadName = 'Thread-' + str(count_num)
            min = THTREA_LEN * (count_num -1)
            max = THTREA_LEN * count_num
            if min > all_numbers:
                break
            if max >= all_numbers:
                max = all_numbers
            
            # init thread
            print('threadName=%s, min=%d, max=%d' %(threadName, min, max))
            try:
                #thread init
                data_proc_t = threading.Thread(target = self.nomal_data_proc, args = (threadName, min, max, google_translate))
                #start thread
                data_proc_t.start()
            except:
                print("Error: unable to start thread")

            if max >= all_numbers:
                    break

if __name__ == "__main__":
    #1.创建表并插入数据
    sync_data = SyncData()
    flag = True
    sync_data.data_init(flag)

    #2.获取需要翻译的标签，并放入到全局变量数组中
    plugins_thread = PluginsThread()
    #plugins_thread.get_tag_info(sync_data)

    #3.先单独翻译family
    google_translate = GoogleTranslate()
    plugins_thread.translate_family(google_translate)

    #3.插入待翻译的数据到nvts_en
    """
    nvts_en_numbers = sync_data.data_nvts_en()
    max_thread = 2
    print('max_thread= %d, nvt_nvts_number=%d' % (max_thread, nvts_en_numbers))
    plugins_thread.start_thread(max_thread, nvts_en_numbers, google_translate)
    """
