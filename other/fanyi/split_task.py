#coding=utf-8

import sqlite3
import os

if __name__ == "__main__":
    db_path_topvas_src = './db/tasks.db'
    db_path_split = './db/tasks_split_'
    SPLIT_LENGTH = 1000
    count = 0
    count_nvts_number = 0
    base_id = 0
    db_list = []
    #统计nvts表中数量
    cx_src = sqlite3.connect(db_path_topvas_src)
    cur = cx_src.cursor()
    ret_count = cur.execute('select count(*) from nvts;')
    nvt_num_info = ret_count.fetchall()
    for info in nvt_num_info:
        count_nvts_number = info[0]

    #count_nvts_number = 50
    print('nvts numbers:' + str(count_nvts_number))

    cur.close()
    cx_src.commit()
    cx_src.close()

    while True:
        count = count + 1
        db_str = db_path_split + str(count) + '.db'
        db_list.append(db_str)
        print('#########progress:' + str(count))
        print('connect db:' + db_str)
        cx = sqlite3.connect(db_str)
        cu = cx.cursor()

        try:
            drop_sql = 'drop table if exists nvts;'
            print(drop_sql)
            cu.execute(drop_sql)
        except:
            print('drop sql error:' + drop_sql)

        try:
            attach_sql = 'attach  \"' + db_path_topvas_src + '\"  as t1;'
            print(attach_sql)
            cu.execute(attach_sql)
        except:
            print('attach sql error:' + attach_sql)
            pass

        min_id = base_id + (count - 1) * SPLIT_LENGTH
        max_id = base_id + count * SPLIT_LENGTH
        if max_id >= count_nvts_number:
            max_id = count_nvts_number
        import_sql = 'create table nvts as select * from t1.nvts where id > ' + str(min_id) + ' and id <=' + str(max_id) + ';'
        print('import sql:' + import_sql)
        try:
            print(import_sql)
            cu.execute(import_sql)
        except:
            print('import sql error:' + import_sql)
            pass
        print('import data ok!!!')
        
        #关闭游标
        cu.close()
        #事务提交
        cx.commit()
        #关闭数据库
        cx.close()
        if max_id == count_nvts_number:
            print('###exit')
            break;

    #开始执行翻译
    print('Command to fanyi:')
    for db in db_list:
        cmd = 'python2.7 translate_mul.py first ' + db + ' &'
        print(cmd)
    #os.system('python2.7 translate_mul.py first ./db/tasks_split_2.db')
