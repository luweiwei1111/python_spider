import sys
import json
import sqlite3
from sqlite3_sql import Sql

class Redis_data:
    def read_json(self, json_file):
        fr_open = open(json_file)
        for line in fr_open.readlines():
            inp_dict = json.loads(line)
            file_name = inp_dict['key']
            if ':oid' in file_name:
                oid = inp_dict['value'][0]
                file_name = inp_dict['key'].split(':')[1]
                name = file_name.split('/')[-1]
                Sql.insert_topvas_oid_info(oid, name)
                #print('oid:' + oid + ' file_name:' + file_name)
        fr_open.close()

if __name__ == '__main__':
	#数据初始化
    Sql.ctl_tb_topvas_oid_info()
    Sql.clr_topvas_oid_info()

    json_file = 'redis_data.json'
    cmd = 'redis-dump -u 127.0.0.1 > ' + json_file
    os.system(cmd)
    redis_data = Redis_data()

    redis_data.read_json(json_file)
