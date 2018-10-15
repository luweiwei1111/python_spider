1.将翻译的数据导入到nvts_cn表中
python2.7 nvts_cn.py

2.继续执行翻译的脚本
python2.7 fanyi_cn_en_mul.py continue tasks.db &

3.查看翻译进度
sqlite3 tasks.db
sql>select count(*) from blog_blogspost where cn_ok='1';