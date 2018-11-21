from sqlite3piplines.sqlite3_sql import Sql
#解析topvas与nessus的数据，并导出报告

"""
需要表信息
openvas数据   --> nvts
nessus数据    --> nvts_ness
product数据   --> cve_detail_list
最后生成报告   --> cve_report
              --> ness_report_dist
"""

class TopVAS:
    """
    cve_list_rp = {'CVE-2016-0638', 'CVE-2016-3510', 'CVE-2016-1181', 'CVE-2017-3506', 'CVE-2017-3531', 
                'CVE-2017-5638', 'CVE-2018-2628', 'CVE-2013-1768', 'CVE-2017-5645', 'CVE-2014-0107',
                'CVE-2013-2027', 'CVE-2016-5601', 'CVE-2015-7501', 'CVE-2013-2186', 'CVE-2014-6569',
                'CVE-2014-2470', 'CVE-2013-1504', 'CVE-2013-2390', 'CVE-2014-3566', 'CVE-2015-0449', 
                'CVE-2015-0482', 'CVE-2013-5855', 'CVE-2015-2623', 'CVE-2015-4744', 'CVE-2013-1739', 
                'CVE-2013-1740', 'CVE-2013-5605', 'CVE-2013-5606', 'CVE-2014-1490', 'CVE-2014-1491', 
                'CVE-2014-1492', 'CVE-2014-6499', 'CVE-2014-0114', 'CVE-2014-6534'}
    """
    def __init__(self):
        #Sql.drop_tb_cve_report()
        Sql.ctl_tb_cve_report()
        Sql.cls_tb_cve_report()
        Sql.ctl_index_nvts_ness()
        Sql.ctl_tb_ness_report()
        Sql.cls_tb_ness_report()
        Sql.ctl_tb_ness_report_dist()
        Sql.cls_tb_ness_report_dist()

    def cve_report(self):
        #cve topvas
        cve_detail_list = Sql.select_cve_detail_list()
        
        for cve_info in cve_detail_list:
            product_id = cve_info[0]
            product_name = cve_info[1]
            year = cve_info[2]
            vul_type = cve_info[3]
            cve = cve_info[4]

            topvas_file_tmp = ''

            #topvas
            nvt_topvas_list = Sql.select_nvts_topvas_by_cve(cve)
            topvas_exist = 'no'
            topvas_file = ''
            if len(nvt_topvas_list) != 0:
                topvas_exist = 'yes'
                topvas_file = ''
                count = 0
                for file in nvt_topvas_list:
                    count = count + 1
                    if count == 1:
                        topvas_file = file[0]
                    else:
                        topvas_file = topvas_file + ',' + file[0]

            #nessus
            nvt_ness_list = Sql.select_nvts_ness_by_cve(cve)
            nessus_file = ''
            nessus_exist = 'no'
            if len(nvt_ness_list) != 0:
                nessus_exist = 'yes'
                nessus_file = ''
                count = 0
                for file in nvt_ness_list:
                    count = count + 1
                    if count == 1:
                        nessus_file = file[0]
                    else:
                        nessus_file = nessus_file + ',' + file[0]
            #生成报告
            Sql.insert_cve_report(product_id, product_name, year, vul_type, cve, topvas_file, topvas_exist, nessus_file, nessus_exist)

    def get_ness_report(self):
        cve_detail_list = self.cve_list_rp
        for cve in cve_detail_list:
            #topvas
            nvt_topvas_list = Sql.select_nvts_topvas_by_cve(cve)
            topvas_exist = 'no'
            topvas_file = ''
            if len(nvt_topvas_list) != 0:
                topvas_exist = 'yes'
                topvas_file = ''
                count = 0
                for file in nvt_topvas_list:
                    count = count + 1
                    if count == 1:
                        topvas_file = file[0]
                    else:
                        topvas_file = topvas_file + ',' + file[0]

            #nessus
            nvt_ness_list = Sql.select_nvts_ness_by_cve(cve)
            nessus_file = ''
            nessus_exist = 'no'
            if len(nvt_ness_list) != 0:
                nessus_exist = 'yes'
                nessus_file = ''
                count = 0
                for file in nvt_ness_list:
                    count = count + 1
                    if count == 1:
                        nessus_file = file[0]
                    else:
                        nessus_file = nessus_file + ',' + file[0]
            Sql.insert_ness_report(cve, topvas_file, topvas_exist, nessus_file, nessus_exist)

    def get_cve_report_files(self):
        file_list = []
        product_name_list = Sql.select_tb_cve_report_by_product_name()
        for product_name_info in product_name_list:
            product_name = product_name_info[0]
            print('###product_name=' + product_name)
            result_file = Sql.select_tb_cve_report(product_name)
            file_count = 0
            ness_file = ''
            for item in result_file:
                #file_tmp_list = item[0]
                #print(file_tmp_list)
                file_tmp_list = item[0].split(',')
                for file in file_tmp_list:
                   if file not in file_list:
                       #print('ness file:' + file)
                       file_count = file_count + 1
                       ness_file = ness_file + ' ' + file
                       #file_list.append(file)
            print('file_count=' + str(file_count))
            print('ness_file=' + ness_file)
            Sql.insert_ness_report_dist(product_name, file_count, ness_file)

if __name__ == '__main__':
    topvas = TopVAS()
    topvas.cve_report()
    print('#############文件去重#############')
    topvas.get_cve_report_files()
    #topvas.get_ness_report()
