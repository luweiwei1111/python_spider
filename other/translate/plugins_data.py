#coding=utf-8
from HandleJs import Py4Js
from sqlite3_sql import Sql
import sys
import importlib
importlib.reload(sys)

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
        count = 0
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

            count = count + 1
            print('#progress:' + str(count))
            #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            #print("#oid->%s ,tag->%s" %(oid, tag))
            if tag != 'NOTAG':
                tag_list = tag.split('|')
                for tag_info in tag_list:
                    #print('####tag:' + tag_info + '####')
                    tag_name_info = tag_info.split('=')[0]
                    tag_name_desc = tag_info.split('=')[1]
                    if tag_name_info == 'summary':
                        summary_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('summary=%s' %(summary_cn) )
                    elif tag_name_info == 'affected':
                        affected_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('affected=%s' %(affected_cn) )
                    elif tag_name_info == 'solution':
                        solution_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('solution=%s' %(solution_cn) )
                    elif tag_name_info == 'insight':
                        insight_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('insight=%s' %(insight_cn) )
                    elif tag_name_info == 'vuldetect':
                        vuldetect_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('vuldetect=%s' %(vuldetect_cn) )
                    elif tag_name_info == 'impact':
                        impact_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('impact=%s' %(impact_cn) )
                    elif tag_name_info == 'synopsis':
                        synopsis_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('synopsis=%s' %(synopsis_cn) )
                    elif tag_name_info == 'description':
                        description_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('description=%s' %(description_cn) )
                    elif tag_name_info == 'exploitability_ease':
                        exploitability_ease_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('exploitability_ease=%s' %(exploitability_ease_cn) )
                    elif tag_name_info == 'risk_factor':
                        risk_factor_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('risk_factor=%s' %(risk_factor_cn) )
                    elif tag_name_info == 'metasploit_name':
                        metasploit_name_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('metasploit_name=%s' %(metasploit_name_cn) )
                    elif tag_name_info == 'd2_elliot_name':
                        d2_elliot_name_cn = tag_name_desc.replace('\'', '\'\'')
                        #print('d2_elliot_name=%s' %(d2_elliot_name_cn) )
                #print('begin update')
                Sql.update_blog_blogspost_en(oid, summary_cn, affected_cn, solution_cn, insight_cn, vuldetect_cn, impact_cn, synopsis_cn, description_cn, exploitability_ease_cn, risk_factor_cn, metasploit_name_cn, d2_elliot_name_cn)
