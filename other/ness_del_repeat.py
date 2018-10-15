# coding=utf-8

import os
import sys
import os.path
import string

"""
ness已移植的插件去重统计
"""

ness_plugins_list = []
case_total_num = 0
def search_file(dir,sname): 
    global ness_plugins_list  # global声明
    global case_total_num     # global声明
    if sname in os.path.split(dir)[1]: #检验文件名里是否包含sname 
        #相对路径
        script_file = os.path.relpath(dir)
        filename = script_file.split('/')[-1]
        if filename.startswith('ns_'):
            case_total_num = case_total_num + 1;
            ness_plugins_list.append(filename)   
    if os.path.isfile(dir):   # 如果传入的dir直接是一个文件目录 他就没有子目录，就不用再遍历它的子目录了
        return 
    for dire in os.listdir(dir): # 遍历子目录  这里的dire为当前文件名 
        search_file(os.path.join(dir,dire),sname) #jion一下就变成了当前文件的绝对路径
                                          # 对每个子目录路劲执行同样的操作

if __name__=="__main__":
    NESS_PATH = '/usr/local/svn-0710/sys/plugins/'
    search_file(NESS_PATH, '.nasl')
    print('case_total_num = ' + str(case_total_num))

    #去重
    out_plugins = []
    del_plugins = []
    count_out = 0;
    count_del = 0;
    for plugin in ness_plugins_list:
        if plugin not in out_plugins:
            count_out = count_out + 1;
            out_plugins.append(plugin)
        else:
            count_del = count_del + 1;
            del_plugins.append(plugin)

    print('count_out = ' + str(count_out))
    print('count_del = ' + str(count_del))
    #重复插件
    for del_file in del_plugins:
        print('delete file:', del_file)
