from .sql import Sql

class data_proc:

    def __init__(self):
        print('data_sync init')

    def sqliteEscape(self, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")

    def sync_data(self):
        Sql.ctl_index_nvts_ness()
        Sql.sync_blog_blogspost_and_nvts()
        self.update_tag()

    def upgrate_tag(cu):
        #更新tag数据
        count_set = 0
        result_tag = Sql.select_blog_blogspost_by_cn_ok('yes')
        for info in result_tag:
            oid = info[0]
            name = info[1]
            tag = info[2]
            summary = ''
            affected = ''
            solution = ''
            insight = ''
            vuldetect = ''
            impact = ''
            synopsis = ''
            description = ''
            exploitability_ease = ''
            risk_factor = ''
            metasploit_name = ''
            d2_elliot_name = ''

            #print("#tag->%s" %(info))
            if tag != 'NOTAG':
                tag_list = tag.split('|')
                for tag_info in tag_list:
                    #print('####tag:' + tag_info + '####')
                    tag_name_info = tag_info.split('=')[0]
                    tag_name_desc = tag_info.split('=')[1]
                    if tag_name_info == 'summary':
                        summary = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'affected':
                        affected = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'solution':
                        solution = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'insight':
                        insight = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'vuldetect':
                        vuldetect = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'impact':
                        impact = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'synopsis':
                        synopsis = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'description':
                        description = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'exploitability_ease':
                        exploitability_ease = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'risk_factor':
                        risk_factor = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'metasploit_name':
                        metasploit_name = tag_name_desc.replace('\'', '\'\'')
                    elif tag_name_info == 'd2_elliot_name':
                        d2_elliot_name = tag_name_desc.replace('\'', '\'\'')
            
            count_set = count_set + 1
            print('##Update Progress##' + str(count_set))
            Sql.update_blog_blogspost(summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name, oid, name)

    