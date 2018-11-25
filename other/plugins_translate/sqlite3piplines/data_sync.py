from sqlite3piplines.sqlite3_sql import Sql

class SyncData:

    def __init__(self):
        Sql.drop_blog_blogspost()
        #创建表blog_blogspost
        Sql.ctl_tb_blog_blogspost()
        #清空表blog_blogspost数据
        Sql.clr_blog_blogspost()
        #创建索引
        Sql.ctl_index_blog_blogspost()

        #创建表nvts_en 用于保存带翻译的英文数据
        Sql.drop_tb_nvts_en()
        Sql.ctl_tb_nvts_en()
        #清空表nvts_en数据
        #Sql.clr_nvts_en()

    def sqliteEscape(self, keyWord):
        return keyWord.replace("/", "//").replace("'", "''").replace("[", "/[").replace("]", "/]").replace("%", "/%").replace("&","/&").replace("_", "/_").replace("(", "/(").replace(")", "/)")

    def sync_data(self):
        Sql.sync_blog_blogspost_and_nvts()

    def data_to_dict(self, data, interval_kv, interval_dict):
        #将data转化为dict
        dict_tag = {}
        for item in data.split(interval_dict):
            list_item  = item.split(interval_kv)
            key = list_item[0]
            value = list_item[1]
            dict_tag[key] = value

        return dict_tag

    def update_tag(self):
        #更新tag数据
        count_set = 0
        result_tag = Sql.select_blog_blogspost_by_cn_ok('no')
        for info in result_tag:
            oid = info[0]
            name = info[1].replace('\'', '\'\'')
            tag_data = info[2]
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

            if tag_data != 'NOTAG':
                key_list = []
                dict_data = self.data_to_dict(tag_data, '=', '|')
                for key in dict_data:
                    key_list.append(key)
                if 'summary' in key_list:
                    summary = dict_data['summary'].replace('\'', '\'\'')
                if 'affected' in key_list:
                    affected = dict_data['affected'].replace('\'', '\'\'')
                if 'solution' in key_list:
                    solution = dict_data['solution'].replace('\'', '\'\'')
                if 'insight' in key_list:
                    insight = dict_data['insight'].replace('\'', '\'\'')
                if 'vuldetect' in key_list:
                    vuldetect = dict_data['vuldetect'].replace('\'', '\'\'')
                if 'impact' in key_list:
                    impact = dict_data['impact'].replace('\'', '\'\'')
                if 'synopsis' in key_list:
                    synopsis = dict_data['synopsis'].replace('\'', '\'\'')
                if 'description' in key_list:
                    description = dict_data['description'].replace('\'', '\'\'')
                if 'exploitability_ease' in key_list:
                    exploitability_ease = dict_data['exploitability_ease'].replace('\'', '\'\'')
                if 'risk_factor' in key_list:
                    risk_factor = dict_data['risk_factor'].replace('\'', '\'\'')
                if 'metasploit_name' in key_list:
                    metasploit_name = dict_data['metasploit_name'].replace('\'', '\'\'')
                if 'd2_elliot_name' in key_list:
                    d2_elliot_name = dict_data['d2_elliot_name'].replace('\'', '\'\'')
            
            count_set = count_set + 1
            print('##Update Progress##' + str(count_set))
            Sql.update_blog_blogspost(summary, affected, solution, insight, vuldetect, impact, synopsis, description, exploitability_ease, risk_factor, metasploit_name, d2_elliot_name, oid, name)

    #创建表 blog_blogspost 并插入数据
    def data_init(self, flag):
        #####创建表 blog_blogspost 并插入数据
        #只有入参为True，则需要重新构建 blog_blogspost 里面的数据
        print('flag=' + str(flag))
        if flag ==  True:
            print('first')
            #插入数据
            Sql.insert_blog_blogspost()

        #同步表nvts与blog_blogspost的数据
        #self.sync_data()
        #更新tag
        self.update_tag()

    def data_nvts_en(self):
        Sql.insert_nvts_en()
        Sql.ctl_index_nvts_en()
        #统计nvts_en数据量
        nvt_num_info = Sql.select_count_nvts_en_by_cn_ok('no')
        for info_n in nvt_num_info:
            count_nvts_numbers = info_n[0]

        return count_nvts_numbers