#coding: utf-8

import os
import sys
import os.path
import string
import difflib
import time

case_total_num = 0

def search_file(dir,sname,arr_list): 
    global openvas_plugins_list  # global声明
    global case_total_num     # global声明
    if sname in os.path.split(dir)[1]: #检验文件名里是否包含sname 
        #相对路径
        script_file = os.path.relpath(dir)
        case_total_num = case_total_num + 1
        filename = script_file.split('/')[-1]
        arr_list.append(filename)
    if os.path.isfile(dir):   # 如果传入的dir直接是一个文件目录 他就没有子目录，就不用再遍历它的子目录了
        return 
    for dire in os.listdir(dir): # 遍历子目录  这里的dire为当前文件名 
        search_file(os.path.join(dir,dire),sname, arr_list) #jion一下就变成了当前文件的绝对路径
                                          # 对每个子目录路劲执行同样的操作

def search_path_list(dir,sname, file_string, arr_list): 
    if sname in os.path.split(dir)[1]: #检验文件名里是否包含sname 
        #相对路径
        script_file = os.path.relpath(dir)
        filename = script_file.split('/')[-1]
        if file_string == filename:
            #print("file path:" + script_file)
            arr_list.append(script_file)
            return
    if os.path.isfile(dir):   # 如果传入的dir直接是一个文件目录 他就没有子目录，就不用再遍历它的子目录了
        return 
    for dire in os.listdir(dir): # 遍历子目录  这里的dire为当前文件名 
        search_path_list(os.path.join(dir,dire),sname, file_string, arr_list) #jion一下就变成了当前文件的绝对路径
                                          # 对每个子目录路劲执行同样的操作

#返回文件的相对路径（带文件名）
def search_file_path(dir, pattern, string):
    list = []
    search_path_list(dir, pattern, string, list)
    return list[0]

def cmp_file_content(file_base, file_new, file_same, report_path):
    """比较文件内容主函数"""
    try:
        f1 = file_base  #获取文件名
        f2 = file_new
    except  Exception as e:
        print("Error: "+ str(e))
        print("input error")
        sys.exit()

    if f1 == "" or f2 == "":#参数不够
        print("Usage : python compareFile.py filename1 filename2")
        sys.exit()

    tf1 = readFile(f1)
    tf2 = readFile(f2)

    d = difflib.HtmlDiff()#创建一个实例difflib.HtmlDiff
    writeFile(d.make_file(tf1,tf2), file_same, report_path)#生成一个比较后的报告文件，格式为html

def readFile(filename):
    """读取文件，并处理"""
    try:
        fileHandle = open(filename, "r")
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as e:
        print("Read file error: "+ str(e))
        sys.exit()

def writeFile(file, filename, report_path):
    """写入文件"""
    #diffFile = open('diff_{}_.html'.format(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())), "w")
    diffFile = open(report_path + '/diff_' + filename + '.html', "w")
    diffFile.write("<meta charset='UTF-8'>")
    diffFile.write(file)
    print(filename + " report: {}".format(os.path.abspath(str(diffFile.name))))#提示文件生成在什么地方
    diffFile.close()

# find_cur(string, path)实现对path目录下文件的查找，列出文件命中含string的文件
def find_cur(string, path):
    # print('cur_dir is %s' % os.path.abspath(path))
    l = []

    # 遍历当前文件，找出符合要求的文件，将路径添加到l中
    for x in os.listdir(path):
        if os.path.isfile(path+'/'+x):
            if string in x:
                l.append(os.path.abspath(x))
    if not l:
        print('no %s in %s' % (string, os.path.abspath(path1)))
    else:
        print(l)

if __name__=="__main__":
    #获取升级插件的配置文件
    UPDATE_CONF='update.conf'
    #解析参数
    base_plugins_file = ''
    update_plugins_file = ''
    update_plugins_url = ''
    fp = open(UPDATE_CONF)
    for line in fp.readlines():
        if 'base_plugins' in line:
            base_plugins_file = line.split('=')[1].replace('\n', '')
        if 'update_plugins' in line:
            update_plugins_file = line.split('=')[1].replace('\n', '')
        if 'update_url' in line:
            update_plugins_url = line.split('=')[1].replace('\n', '')    
    fp.close()

    #新建目录，按照日期命名
    current_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    base_path = 'openvas_' + current_time
    #print('base_path=' + base_path)
    isExists = os.path.exists(base_path)
    if not isExists:
        os.makedirs(base_path)
    else:
        os.system('rm -rf ' + base_path)

    report_path = base_path + '/report'
    #print('report path: ' + report_path)
    isExists = os.path.exists(report_path)
    if not isExists:
        os.makedirs(report_path)

    #获取openvas更新包
    wget_cmd = 'wget ' + update_plugins_url
    print("cmd:" + wget_cmd)
    os.system(wget_cmd)

    #解压插件到指定目录
    base_plugins_path = base_path + '/base_plugins'
    #print('base plugins path: ' + base_plugins_path)
    isExists = os.path.exists(base_plugins_path)
    if not isExists:
        os.makedirs(base_plugins_path)

    update_plugins_path = base_path + '/update_plugins'
    print('update plugins path: ' + update_plugins_path)
    isExists = os.path.exists(update_plugins_path)
    if not isExists:
        os.makedirs(update_plugins_path)

    #解压tar包
    tar_base_cmd = 'tar -zxf ' + base_plugins_file + ' -C ' + base_plugins_path
    tar_update_cmd = 'tar -jxf ' + update_plugins_file + ' -C ' + update_plugins_path
    print(tar_base_cmd)
    os.system(tar_base_cmd)
    print(tar_update_cmd)
    os.system(tar_update_cmd)

    #删除.asc
    rm_asc = 'find ' + update_plugins_path + ' -name *.asc -exec rm \'{}\' \\;'
    print(rm_asc)
    os.system(rm_asc)

    OPENVAS_PATH_BASE = base_plugins_path
    OPENVAS_PATH_NEW = update_plugins_path
    report_file = report_path + '/report_info'
    report_info =   '################################################\n' + \
                    '##########OpenVAS Plugins compare INFO##########\n' + \
                    '################################################\n'

    print(report_info)
    print_info =  'base_plugins_file    : ' + base_plugins_file + '\n' + \
                  'update_plugins_file  : ' + update_plugins_file + '\n' + \
                  'update_url           : ' + update_plugins_url + '\n' + \
                  'base_path            : ' + base_path + '\n' + \
                  'report_path          : ' + report_path + '\n' + \
                  'base_plugin_path     : ' + base_plugins_path + '\n' + \
                  'update_plugin_path   : ' + update_plugins_path + '\n' + \
                  'wget cmd             : ' + wget_cmd + '\n' + \
                  'tar base   cmd       : ' + tar_base_cmd + '\n' + \
                  'tar update cmd       : ' + tar_update_cmd

    report_info = report_info + print_info + '\n'
    print(print_info)
    
    openvas_base_list = []
    case_total_num = 0
    search_file(OPENVAS_PATH_BASE, '.nasl', openvas_base_list)

    print_info = '################################################\n' + \
                 '##1.OpenVAS Current Plugins number: ' + str(case_total_num)
    report_info = report_info + print_info + '\n'
    print(print_info)

    openvas_new_list = []
    case_total_num = 0
    search_file(OPENVAS_PATH_NEW, '.nasl', openvas_new_list)
    print_info = '##2.OpenVAS Update Plugins number: ' + str(case_total_num) + '\n' + \
                 '#################baes###########################'
    report_info = report_info + print_info + '\n'
    print(print_info)

    #去重
    diff_by_base = []
    same_by_base = []
    count_out = 0
    count_same_out = 0
    #base包中存在，新包中不存在的
    for base_plugin in openvas_base_list:
        if base_plugin not in openvas_new_list:
            count_out = count_out + 1
            print_info = '###openvas base:' + base_plugin
            report_info = report_info + print_info + '\n'
            diff_by_base.append(base_plugin)
        else:
            count_same_out = count_same_out + 1
            same_by_base.append(base_plugin)
    print_info = '#################baes###########################\n' + \
                 '##3.In Base, Not In Update-->number ' + str(count_out) + '\n' + \
                 '#################new############################'
    report_info = report_info + print_info + '\n'
    print(print_info)

    #去重
    diff_by_new = []
    count_out = 0
    #新包中存在，base包中不存在
    for new_plugin in openvas_new_list:
        if new_plugin not in openvas_base_list:
            count_out = count_out + 1
            print('openvas new:' + new_plugin)
            report_info = report_info + '###openvas new:' + new_plugin + '\n'
            diff_by_new.append(new_plugin)

    print_info = '#################new############################\n' + \
                 '##4.In Update, Not In Base--> number: ' + str(count_out) + '\n' + \
                 '#################same###########################\n' + \
                 '##5.Base && Update, same number: ' + str(count_same_out) 
    report_info = report_info + print_info + '\n'
    print(print_info)

    count = 0
    for same_plugin in same_by_base:
        base = search_file_path(OPENVAS_PATH_BASE, '.nasl', same_plugin)
        new = search_file_path(OPENVAS_PATH_NEW, '.nasl', same_plugin)
        #比较文件内容
        cmp_file_content(base, new, same_plugin, report_path)
        count = count + 1
        if count > 20:
            break
    print_info = '#################same###########################'
    report_info = report_info + print_info + '\n'
    print(print_info)

    fr_nasl = open(report_file, 'w')
    try:
        fr_nasl.write(report_info)
    except:
        print('write '+ report_info + ' failed')
