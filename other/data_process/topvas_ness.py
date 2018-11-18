from sqlite3piplines.sqlite3_sql import Sql
#解析topvas与nessus的数据，并导出报告

"""
需要表信息
openvas数据   --> nvts
nessus数据    --> nvts_ness
product数据   --> cve_detail_list
最后生成报告   --> cve_report
"""

class TopVAS:
    def __init__(self):
        #Sql.drop_tb_cve_report()
        Sql.ctl_tb_cve_report()
        Sql.cls_tb_cve_report()
        Sql.ctl_index_nvts_ness()

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

if __name__ == '__main__':
    topvas = TopVAS()
    topvas.cve_report()
