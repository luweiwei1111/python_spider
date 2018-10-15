# coding=utf-8

import os
import sqlite3
import sys
import re
import os.path

SCRIPT_CHECK  = 'ubuntu_check'
count_id = 0

def get_script_info(file_name , fr_open, id_sqlite3):
    script_cve_id = ''
    script_cve_id_temp = ''
    script_id = ''
    script_name = ''
    script_category = ''
    script_family = ''

    global count_id
    insert_script_info = ' '
    line_count = 0;
    line_flag = 0;
    #print("#####file_name:", file_name, "#", str(id_sqlite3), "#########################")
    for line in fr_open.readlines():
        line_count = line_count + 1
        #记录script_dependencies行号
        if 'script_dependencies' in line:
            line_depend = line_count
        #记录}行号
        elif '}' in line and line_flag == 0:
            line_flag = 1
            line_desc = line_count
        elif SCRIPT_CHECK in line:
            ubuntu_list = line.split('\"')
            osver = ubuntu_list[1]
            pkgname = ubuntu_list[3]
            pkgver = ubuntu_list[5]
            if osver == '4.10':
                release = 'UBUNTU4.1'
            elif osver == '5.04':
                release = 'UBUNTU5.04'
            elif osver == '5.10':
                release = 'UBUNTU5.10'
            elif osver == '6.06':
                release = 'UBUNTU6.06 LTS'
            elif osver == '6.10':
                release = 'UBUNTU6.10'
            elif osver == '7.04':
                release = 'UBUNTU7.04'
            elif osver == '7.10':
                release = 'UBUNTU7.10'
            elif osver == '8.04':
                release = 'UBUNTU8.04 LTS'
            elif osver == '8.10':
                release = 'UBUNTU8.10'
            elif osver == '9.04':
                release = 'UBUNTU9.04'
            elif osver == '9.10':
                release = 'UBUNTU9.10'
            elif osver == '10.04':
                release = 'UBUNTU10.04 LTS'
            elif osver == '10.10':
                release = 'UBUNTU10.10'
            elif osver == '11.04':
                release = 'UBUNTU11.04'
            elif osver == '11.10':
                release = 'UBUNTU11.10'
            elif osver == '12.04':
                release = 'UBUNTU12.04 LTS'
            elif osver == '12.10':
                release = 'UBUNTU12.10'
            elif osver == '13.04':
                release = 'UBUNTU13.04'
            elif osver == '13.10':
                release = 'UBUNTU13.10'
            elif osver == '14.04':
                release = 'UBUNTU14.04 LTS'
            elif osver == '14.10':
                release = 'UBUNTU14.10'
            elif osver == '15.04':
                release = 'UBUNTU15.04'
            elif osver == '15.10':
                release = 'UBUNTU15.10'
            elif osver == '16.04':
                release = 'UBUNTU16.04 LTS'
            elif osver == '16.10':
                release = 'UBUNTU16.10'
            elif osver == '17.04':
                release = 'UBUNTU17.04'
            elif osver == '17.10':
                release = 'UBUNTU17.10'
            elif osver == '18.04':
                release = 'UBUNTU18.04 LTS'
            count_id = count_id + 1
            #print('osver:' + osver, ", release:", release, ", pkgname:", pkgname, ", pkgver:", pkgver)
            id = str(count_id)

            #获取文件总函数
            cmd = 'cd ' + '/usr/local/var/lib/openvas/plugins/ns_ubuntu' + ' && awk \'END{print NR}\' ' + file_name
            r = os.popen(cmd)
            info_cmd = r.readlines()
            line_all = info_cmd[0].replace('\n', '')
            insert_script_info = insert_script_info +  'insert into ubuntu_info(id, file_name, line_depend, line_desc, line_all, release, osver, pkgname, pkgver) values('+ \
                                 '\'' + id + '\',' +  \
                                 '\'' + file_name + '\',' +  \
                                 '\'' + str(line_depend) + '\',' +  \
                                 '\'' + str(line_desc) + '\',' +  \
                                 '\'' + str(line_all) + '\',' +  \
                                 '\'' + release + '\',' +  \
                                 '\'' + osver + '\',' +  \
                                 '\'' + pkgname + '\',' +  \
                                 '\'' + pkgver + '\');'
            #print('insert_script_info:', insert_script_info);
    #print("#####file_name:", file_name, "#", str(id_sqlite3), "#########################")
    return insert_script_info;

def del_script_info(file_name , id_sqlite3, cu):
    UBUNTU_PATH = '/usr/local/var/lib/openvas/plugins/ns_ubuntu/'
    select_file = 'select distinct line_depend, line_all from ubuntu_info where file_name = ' + '\'' + file_name + '\''
    try:
        result_count = cu.execute(select_file)
        all_info = result_count.fetchall()
        for info in all_info:
            line_depend = info[0]
            line_all = info[1]
        #按照行号删除插件内容
        del_cmd = 'cd ' + UBUNTU_PATH + '&& sed -i ' + line_depend + '\',\'' + line_all + '\'d\' ' +  file_name
        os.system(del_cmd)
    except:
        print("error:" + select_file)

def add_script_info(file_name , id_sqlite3, fr_open, cu):
    print("#-->file_name:", file_name, "#", str(id_sqlite3), "#########################")
    UBUNTU_PATH = '/usr/local/var/lib/openvas/plugins/ns_ubuntu/'
    select_release = 'select distinct release from ubuntu_info where file_name = ' + '\'' + file_name + '\''
    try:
        release_arr = []
        ssh_release = ''
        result_release = cu.execute(select_release)
        all_info_release = result_release.fetchall()
        for info_release in all_info_release:
            release = info_release[0].replace('UBUNTU', '').replace('.', '\\.')
            release_arr.append(release)
            #print('select info->release:', release)

        if len(release_arr) == 1:
            ssh_release = release_arr[0] + '");'
        else:
            for index in range(len(release_arr)):
                if index == 0:
                    ssh_release = release_arr[0] + '|'
                elif index == len(release_arr) - 1:
                    ssh_release = ssh_release + release_arr[index] + ')");'
                else:
                    ssh_release = ssh_release + release_arr[index] + '|'

        #1.拼接内容description
        if len(release_arr) > 1:
            description = '  script_dependencies("gather-package-list.nasl");\n'  \
                + '  script_mandatory_keys("ssh/login/ubuntu_linux", "ssh/login/packages", re:"ssh/login/release=UBUNTU(' + ssh_release \
                + '\n\n  exit(0);\n}\n\n'
        else:
            description = '  script_dependencies("gather-package-list.nasl");\n'  \
                + '  script_mandatory_keys("ssh/login/ubuntu_linux", "ssh/login/packages", re:"ssh/login/release=UBUNTU' + ssh_release \
                + '\n\n  exit(0);\n}\n\n'         
        #print('description:\n', description)

        #2.拼接内容inc
        content_inc = 'include("revisions-lib.inc");\ninclude("pkg-lib-deb.inc");\n' + \
            'release = get_kb_item("ssh/login/release");\n\nres = "";\n' + \
            'if(release == NULL){\n  exit(0);\n}\n\n'

        #print('content_inc:\n', content_inc)
    except:
        print("error:" + select_file)
    

    content_main_isdpkgvuln_4_10  = ''
    content_main_isdpkgvuln_5_04  = ''
    content_main_isdpkgvuln_5_10  = ''
    content_main_isdpkgvuln_6_06  = ''
    content_main_isdpkgvuln_6_10  = ''
    content_main_isdpkgvuln_7_04  = ''
    content_main_isdpkgvuln_7_10  = ''
    content_main_isdpkgvuln_8_04  = ''
    content_main_isdpkgvuln_8_10  = ''
    content_main_isdpkgvuln_9_04  = ''
    content_main_isdpkgvuln_9_10  = ''
    content_main_isdpkgvuln_10_04  = ''
    content_main_isdpkgvuln_10_10  = ''
    content_main_isdpkgvuln_11_04  = ''
    content_main_isdpkgvuln_11_10  = ''
    content_main_isdpkgvuln_12_04  = ''
    content_main_isdpkgvuln_12_10  = ''
    content_main_isdpkgvuln_13_04  = ''
    content_main_isdpkgvuln_13_10  = ''
    content_main_isdpkgvuln_14_04  = ''
    content_main_isdpkgvuln_14_10  = ''
    content_main_isdpkgvuln_15_04  = ''
    content_main_isdpkgvuln_15_10  = ''
    content_main_isdpkgvuln_16_04  = ''
    content_main_isdpkgvuln_16_10  = ''
    content_main_isdpkgvuln_17_04  = ''
    content_main_isdpkgvuln_17_10  = ''
    content_main_isdpkgvuln_18_04  = ''
    select_file = 'select release, osver, pkgname, pkgver from ubuntu_info where file_name = ' + '\'' + file_name + '\''
    try:
        content_main_isdpkgvuln = ''
        result_count = cu.execute(select_file)
        all_info = result_count.fetchall()
        for info in all_info:
            release = info[0]
            osver = info[1]
            pkgname = info[2]
            pkgver = info[3]
            print('select info->release:', release, ', osver:', osver, ', pkgname', pkgname, ', pkgver', pkgver)
            #拼接if内容
            if osver == '4.10':
                content_main_isdpkgvuln_4_10 = content_main_isdpkgvuln_4_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '5.04':
                content_main_isdpkgvuln_5_04 = content_main_isdpkgvuln_5_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '5.10':
                content_main_isdpkgvuln_5_10 = content_main_isdpkgvuln_5_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '6.06':
                content_main_isdpkgvuln_6_06 = content_main_isdpkgvuln_6_06 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '6.10':
                content_main_isdpkgvuln_6_10 = content_main_isdpkgvuln_6_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '7.04':
                content_main_isdpkgvuln_7_04 = content_main_isdpkgvuln_7_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '7.10':
                content_main_isdpkgvuln_7_10 = content_main_isdpkgvuln_7_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '8.04':
                content_main_isdpkgvuln_8_04 = content_main_isdpkgvuln_8_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '8.10':
                content_main_isdpkgvuln_8_10 = content_main_isdpkgvuln_8_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '9.04':
                content_main_isdpkgvuln_9_04 = content_main_isdpkgvuln_9_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '9.10':
                content_main_isdpkgvuln_9_10 = content_main_isdpkgvuln_9_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '10.04':
                content_main_isdpkgvuln_10_04 = content_main_isdpkgvuln_10_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '10.10':
                content_main_isdpkgvuln_10_10 = content_main_isdpkgvuln_10_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '11.04':
                content_main_isdpkgvuln_11_04 = content_main_isdpkgvuln_11_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '11.10':
                content_main_isdpkgvuln_11_10 = content_main_isdpkgvuln_11_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '12.04':
                content_main_isdpkgvuln_12_04 = content_main_isdpkgvuln_12_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '12.10':
                content_main_isdpkgvuln_12_10 = content_main_isdpkgvuln_12_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '13.04':
                content_main_isdpkgvuln_13_04 = content_main_isdpkgvuln_13_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '13.10':
                content_main_isdpkgvuln_13_10 = content_main_isdpkgvuln_13_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '14.04':
                content_main_isdpkgvuln_14_04 = content_main_isdpkgvuln_14_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '14.10':
                content_main_isdpkgvuln_14_10 = content_main_isdpkgvuln_14_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '15.04':
                content_main_isdpkgvuln_15_04 = content_main_isdpkgvuln_15_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '15.10':
                content_main_isdpkgvuln_15_10 = content_main_isdpkgvuln_15_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '16.04':
                content_main_isdpkgvuln_16_04 = content_main_isdpkgvuln_16_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '16.10':
                content_main_isdpkgvuln_16_10 = content_main_isdpkgvuln_16_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '17.04':
                content_main_isdpkgvuln_17_04 = content_main_isdpkgvuln_17_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '17.10':
                content_main_isdpkgvuln_17_10 = content_main_isdpkgvuln_17_10 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'
            elif osver == '18.04':
                content_main_isdpkgvuln_18_04 = content_main_isdpkgvuln_18_04 + \
                    '  if ((res = isdpkgvuln(pkg:"' + pkgname + \
                    '", ver:"' + pkgver + \
                    '", rls:"' + release + \
                    '")) != NULL)\n' + \
                    '  {\n      security_message(data:res);\n      exit(0);\n   }\n\n'

        if 'UBUNTU4.1' in content_main_isdpkgvuln_4_10:
            content_main_isdpkgvuln_4_10 = '\nif(release == "UBUNTU4.1")\n{\n' + content_main_isdpkgvuln_4_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU5.04' in content_main_isdpkgvuln_5_04:
            content_main_isdpkgvuln_5_04 = '\nif(release == "UBUNTU5.04")\n{\n' + content_main_isdpkgvuln_5_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU5.10' in content_main_isdpkgvuln_5_10:
            content_main_isdpkgvuln_5_10 = '\nif(release == "UBUNTU5.10")\n{\n' + content_main_isdpkgvuln_5_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU6.06 LTS' in content_main_isdpkgvuln_6_06:
            content_main_isdpkgvuln_6_06 = '\nif(release == "UBUNTU6.06 LTS")\n{\n' + content_main_isdpkgvuln_6_06 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU6.10' in content_main_isdpkgvuln_6_10:
            content_main_isdpkgvuln_6_10 = '\nif(release == "UBUNTU6.10")\n{\n' + content_main_isdpkgvuln_6_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU7.04' in content_main_isdpkgvuln_7_04:
            content_main_isdpkgvuln_7_04 = '\nif(release == "UBUNTU7.04")\n{\n' + content_main_isdpkgvuln_7_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU7.10' in content_main_isdpkgvuln_7_10:
            content_main_isdpkgvuln_7_10 = '\nif(release == "UBUNTU7.10")\n{\n' + content_main_isdpkgvuln_7_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU8.04 LTS' in content_main_isdpkgvuln_8_04:
            content_main_isdpkgvuln_8_04 = '\nif(release == "UBUNTU8.04 LTS")\n{\n' + content_main_isdpkgvuln_8_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU8.10' in content_main_isdpkgvuln_8_10:
            content_main_isdpkgvuln_8_10 = '\nif(release == "UBUNTU8.10")\n{\n' + content_main_isdpkgvuln_8_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU9.04' in content_main_isdpkgvuln_9_04:
            content_main_isdpkgvuln_9_04 = '\nif(release == "UBUNTU9.04")\n{\n' + content_main_isdpkgvuln_9_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU9.10' in content_main_isdpkgvuln_9_10:
            content_main_isdpkgvuln_9_10 = '\nif(release == "UBUNTU9.10")\n{\n' + content_main_isdpkgvuln_9_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU10.04 LTS' in content_main_isdpkgvuln_10_04:
            content_main_isdpkgvuln_10_04 = '\nif(release == "UBUNTU10.04 LTS")\n{\n' + content_main_isdpkgvuln_10_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU10.10' in content_main_isdpkgvuln_10_10:
            content_main_isdpkgvuln_10_10 = '\nif(release == "UBUNTU10.10")\n{\n' + content_main_isdpkgvuln_10_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU11.04' in content_main_isdpkgvuln_11_04:
            content_main_isdpkgvuln_11_04 = '\nif(release == "UBUNTU11.04")\n{\n' + content_main_isdpkgvuln_11_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU11.10' in content_main_isdpkgvuln_11_10:
            content_main_isdpkgvuln_11_10 = '\nif(release == "UBUNTU11.10")\n{\n' + content_main_isdpkgvuln_11_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU12.04 LTS' in content_main_isdpkgvuln_12_04:
            content_main_isdpkgvuln_12_04 = '\nif(release == "UBUNTU12.04 LTS")\n{\n' + content_main_isdpkgvuln_12_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU12.10' in content_main_isdpkgvuln_12_10:
            content_main_isdpkgvuln_12_10 = '\nif(release == "UBUNTU12.10")\n{\n' + content_main_isdpkgvuln_12_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU13.04' in content_main_isdpkgvuln_13_04:
            content_main_isdpkgvuln_13_04 = '\nif(release == "UBUNTU13.04")\n{\n' + content_main_isdpkgvuln_13_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU13.10' in content_main_isdpkgvuln_13_10:
            content_main_isdpkgvuln_13_10 = '\nif(release == "UBUNTU13.10")\n{\n' + content_main_isdpkgvuln_13_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU14.04 LTS' in content_main_isdpkgvuln_14_04:
            content_main_isdpkgvuln_14_04 = '\nif(release == "UBUNTU14.04 LTS")\n{\n' + content_main_isdpkgvuln_14_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU14.10' in content_main_isdpkgvuln_14_10:
            content_main_isdpkgvuln_14_10 = '\nif(release == "UBUNTU14.10")\n{\n' + content_main_isdpkgvuln_14_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU15.04' in content_main_isdpkgvuln_15_04:
            content_main_isdpkgvuln_15_04 = '\nif(release == "UBUNTU15.04")\n{\n' + content_main_isdpkgvuln_15_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU15.10' in content_main_isdpkgvuln_15_10:
            content_main_isdpkgvuln_15_10 = '\nif(release == "UBUNTU15.10")\n{\n' + content_main_isdpkgvuln_15_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU16.04 LTS' in content_main_isdpkgvuln_16_04:
            content_main_isdpkgvuln_16_04 = '\nif(release == "UBUNTU16.04 LTS")\n{\n' + content_main_isdpkgvuln_16_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU16.10' in content_main_isdpkgvuln_16_10:
            content_main_isdpkgvuln_16_10 = '\nif(release == "UBUNTU16.10")\n{\n' + content_main_isdpkgvuln_16_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU17.04' in content_main_isdpkgvuln_17_04:
            content_main_isdpkgvuln_17_04 = '\nif(release == "UBUNTU17.04")\n{\n' + content_main_isdpkgvuln_17_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU17.10' in content_main_isdpkgvuln_17_10:
            content_main_isdpkgvuln_17_10 = '\nif(release == "UBUNTU17.10")\n{\n' + content_main_isdpkgvuln_17_10 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        if 'UBUNTU18.04 LTS' in content_main_isdpkgvuln_18_04:
            content_main_isdpkgvuln_18_04 = '\nif(release == "UBUNTU18.04 LTS")\n{\n' + content_main_isdpkgvuln_18_04 + \
                '  if (__pkg_match) exit(99);\n  exit(0);\n}\n'
        
        content_main = content_main_isdpkgvuln_4_10 + content_main_isdpkgvuln_5_04 + \
                       content_main_isdpkgvuln_5_10 + content_main_isdpkgvuln_6_06 + \
                       content_main_isdpkgvuln_6_10 + content_main_isdpkgvuln_7_04 + \
                       content_main_isdpkgvuln_7_10 + content_main_isdpkgvuln_8_04 + \
                       content_main_isdpkgvuln_8_10 + content_main_isdpkgvuln_9_04 + \
                       content_main_isdpkgvuln_9_10 + content_main_isdpkgvuln_10_04 + \
                       content_main_isdpkgvuln_10_10 + content_main_isdpkgvuln_11_10 + \
                       content_main_isdpkgvuln_12_04 + content_main_isdpkgvuln_12_10 + \
                       content_main_isdpkgvuln_13_04 + content_main_isdpkgvuln_11_04 + \
                       content_main_isdpkgvuln_13_10 + content_main_isdpkgvuln_14_04 + \
                       content_main_isdpkgvuln_14_10 + content_main_isdpkgvuln_15_04 + \
                       content_main_isdpkgvuln_15_10 + content_main_isdpkgvuln_16_04 + \
                       content_main_isdpkgvuln_16_10 + content_main_isdpkgvuln_17_04 + \
                       content_main_isdpkgvuln_17_10 + content_main_isdpkgvuln_18_04
        

        #输出总数据
        content_all = description + content_inc + content_main
        print('content_all:\n', content_all)
        fr_open.write(content_all)
    except:
        print("error:" + select_file)

if __name__=="__main__":
    cx = sqlite3.connect('/usr/local/openvas-src/src/db/topvas_plugins.db')
    cu = cx.cursor()

#创建表
    ctb_script_info = 'create table if not exists ubuntu_info  \
    ( \
    id                  INTEGER, \
    file_name           TEXT NOT NULL, \
    description         TEXT, \
    line_depend         TEXT, \
    line_desc           TEXT, \
    line_all            TEXT, \
    release             TEXT NOT NULL, \
    osver               TEXT NOT NULL, \
    pkgname             TEXT NOT NULL, \
    pkgver              TEXT, \
    info                TEXT, \
    reserve1            TEXT, \
    reserve2            TEXT, \
    reserve3            TEXT, \
    PRIMARY KEY (id,file_name) \
    )'
    cu.execute(ctb_script_info)
    #cu.execute('CREATE INDEX ubu_file_name_index ON ubuntu_info(id,file_name);')
    cu.execute("delete from ubuntu_info where 1=1;")

    #NESS_PATH = '/usr/local/openvas-src/src/ns_ubuntu/'
    NESS_PATH = '/usr/local/var/lib/openvas/plugins/ns_ubuntu/'
    count = 0

    #获取ubuntu关键信息
    for filename in os.listdir(NESS_PATH):
            if os.path.splitext(filename)[1] == '.nasl':
                count = count + 1
                script_file = NESS_PATH + filename
                
                #打开文件
                fr_nasl = open(script_file)
                insert_sql_tmp = get_script_info(filename , fr_nasl, count)
                #print('sql:', insert_sql)
                insert_sql = insert_sql_tmp.split(';')
                for i in range(0, len(insert_sql)):
                    try:
                        cu.execute(insert_sql[i])
                    except:
                        print("error:" + insert_sql[i])
                
                #关闭文件
                fr_nasl.close()

    #删除ubuntu不需要的信息
    count = 0
    for filename in os.listdir(NESS_PATH):
            if os.path.splitext(filename)[1] == '.nasl':
                count = count + 1
                script_file = NESS_PATH + filename
                
                #删除无用信息
                del_script_info(filename , count, cu)

    #修改ubuntu脚本
    count = 0
    print('#############ubuntu begin###########################')
    for filename in os.listdir(NESS_PATH):
            if os.path.splitext(filename)[1] == '.nasl':
                count = count + 1
                script_file = NESS_PATH + filename

                #打开文件
                fr_nasl = open(script_file, 'a')
                #修改脚本
                add_script_info(filename , count, fr_nasl, cu)
                #关闭文件
                fr_nasl.close()
    print('#############ubuntu end############################')
#关闭游标
    cu.close()

#事务提交
    cx.commit()

#关闭数据库
    cx.close()

    print("ALL OK!")
