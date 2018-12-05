import pymysql
 
# 打开数据库连接
db = pymysql.connect("localhost","root","12345678","topvas" )
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL 插入语句
sql = """select count(*) from nvts_cn_tmp"""

try:
   # 执行sql语句
   cursor.execute(sql)
   data = cursor.fetchone()
   print(data)
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()