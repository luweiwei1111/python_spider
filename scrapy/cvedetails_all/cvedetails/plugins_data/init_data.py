# -*- coding: utf-8 -*-
from cvedetails.sqlitepiplines.sql import Sql
import openpyxl

class ExcelRead:
    def __init__(self):
        Sql.ctl_tb_settings()
        Sql.ctr_tb_settings()

    def read_excel_to_db(self):
        wb = openpyxl.load_workbook('cvedetails/plugins_data/excel/重点应用分类.xlsx')

        # 获取workbook中所有的表格
        sheets = wb.sheetnames        
        print(sheets)

        # 循环遍历所有sheet
        for i in range(len(sheets)):
            if i == 0:
                continue

            sheet = wb[sheets[i]]
            print('\n\n第' + str(i) + '个sheet: ' + sheet.title + '->>>')
            sheet_title = sheet.title
            for r in range(1, sheet.max_row + 1):
                category = ''
                product_name = ''
                product_id = ''
                vendor_id = ''
                product_search = ''
                vendor_search = ''
                owner = ''
                if r == 1:
                    print('\n' + ''.join(
                        [str(sheet.cell(row=r, column=c).value).ljust(17) for c in range(1, sheet.max_column + 1)]))
                else:
                    category = str(sheet.cell(row=r, column=1).value)
                    product_name = str(sheet.cell(row=r, column=2).value)
                    product_id = str(sheet.cell(row=r, column=3).value)
                    vendor_id = str(sheet.cell(row=r, column=4).value)
                    product_search = str(sheet.cell(row=r, column=5).value)
                    vendor_search = str(sheet.cell(row=r, column=6).value)
                    owner = str(sheet.cell(row=r, column=7).value)
                    #print('category=%s, product_name=%s, product_id=%s, vendor_id=%s, product_search=%s, vendor_search=%s, owner=%s' % (category, product_name, product_id, vendor_id, product_search, vendor_search, owner))
                    Sql.insert_tb_settings(category, product_name, product_id, vendor_id, product_search, vendor_search, owner)

class TopVAS:
    def __init__(self):
        #Sql.drop_tb_cve_report()
        Sql.ctl_tb_cve_report()
        Sql.cls_tb_cve_report()
        Sql.ctl_index_nvts_ness()
        Sql.ctl_tb_ness_report()
        Sql.cls_tb_ness_report()
        Sql.ctl_tb_ness_report_dist()
        Sql.cls_tb_ness_report_dist()
        
        Sql.ctl_tb_nvts_nons()
        Sql.ctl_index_nvts_nons()
        Sql.insert_nvts_nons()

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
            topvas_ness_file = ''
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
                    ns_file =  'ns_' + file[0]
                    ret = Sql.select_nvts_by_file(ns_file)
                    if ret[0] == 1:
                        print('file:%s存在' + file[0])
                        topvas_ness_file = topvas_ness_file + ',' + ns_file
                    
                    if count == 1:
                        nessus_file = file[0]
                    else:
                        nessus_file = nessus_file + ',' + file[0]
            if ',' in topvas_ness_file:
                topvas_ness_file = topvas_ness_file[1:]
            #生成报告
            Sql.insert_cve_report(product_id, product_name, year, vul_type, cve, topvas_file, topvas_ness_file, topvas_exist, nessus_file, nessus_exist)
