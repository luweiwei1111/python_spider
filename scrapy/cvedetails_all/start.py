from cvedetails.plugins_data.init_data import ExcelRead
from cvedetails.plugins_data.init_data import TopVAS
from cvedetails.plugins_data.init_data import excelProcess
from cvedetails.plugins_data.init_data import PluginsWriteData
from cvedetails.sqlitepiplines.sql import Sql
import random
import os


if __name__ == '__main__':
    #1.初始化入参
    #读取文件"cvedetails/plugins_data/excel/重点应用分类.xlsx"内容并保存在表settings
    print('##STEP1:insert into table settings')
    excel_fd = ExcelRead()
    excel_fd.read_excel_to_db()

    #2.根据settings表中数据通过scrapy爬取cvedetails.com数据
    print('##STEP2:start spider')
    os.system('python main.py')

    #3.获取topvas和nessus的插件数据到表nvts和nvts_ness
    print('##STEP3:get plugins data')
    # topvas = PluginsWriteData('topvas')
    # topvas.file_walk()

    # ness = PluginsWriteData('nessus')
    # ness.file_walk()
    Sql.delete_XX_nasl()

    #4.生成报告到表cve_report
    print('##STEP4:insert into cve_report')
    topvas = TopVAS()
    topvas.cve_report()

    #5.将表cve_report写到excel文件中
    #文件名："cvedetails/plugins_data/excel/插件移植报告.xls"
    print('##STEP5:read cve_report and write to FILE cvedetails/plugins_data/excel/插件移植报告.xls')
    excel_w_fd = excelProcess()
    excel_w_fd.save_Excel()
    print('##ALL Finish!!!!')

    