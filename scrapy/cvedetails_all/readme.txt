使用方式：
1.修改setting.spy
在PRODUCT_DICT中新增一项，然后新增一个list列表，列表里面保存的为product_id号

2.单独启动爬虫程序
python main.py

3.数据保存
select * from cve_detail_list;
select * from cve_details;

4.整体跑并生成报告
python start.py