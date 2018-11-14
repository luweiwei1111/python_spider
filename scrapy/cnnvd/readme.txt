说明：
1.本程序用于爬取cnnvd网址的数据，并将数据通过sqlite3数据库保存在cnnvd.db库文件里面，
里面有两张表：cve_cnnvd_cn 保存cnnvd的相关信息
              cnnvd_url    保存cnnvd的url路径

2.如何进行爬取（分为两步进行爬取）
python main_url.py  爬取cnnvd的url路径保存起来，由于有时候会由于网络原因而导致失败，所以需要继续爬取。
python main.py      遍历cnnvd_url表，并并在cve_cnnvd_cn里面查找cnnvd，如果已经爬取的则不再爬取，否则就需要爬取，支持继续爬取的功能。

3.由于经常会被封锁IP，所以需要使用到IP池代理，我们使用免费的代理（相关网址http://ip.zdaye.com/dayProxy/ip/133009.html），由于免费的代理不稳定，所以我们需要把爬取的数据缓存起来。
防止被禁的策略：
（1）设置download_delay
（2）禁止cookies（COOKIES_ENABLES=False）
（3）使用user agent池
（4）使用IP池
（5）分布式爬取（TODO）
