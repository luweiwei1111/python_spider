# -*- coding: utf-8 -*-
import json
import os
import scrapy
import time

from PIL import Image

class ZhihuloginSpider(scrapy.Spider):
    name = 'zhihulogin'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['https://www.zhihu.com/']
    Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    header = {
        'User-Agent': Agent,
    }

    def parse(self, response):
        #主页爬取的具体内容
        pass

    def start_requests(self):
        t = str(int(time.time() * 1000))
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=' + t + '&type=login&lang=en'
        return [scrapy.Request(url=captcha_url, headers=self.header, callback=self.parser_captcha)]

    def parser_captcha(self, response):
        with open('captcha.jpg', 'wb') as f:
            f.write(response.body)
            f.close()
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
        captcha = input("please input the captcha\n>")
        return scrapy.FormRequest(url='https://www.zhihu.com/#signin', headers=self.header, callback=self.login, meta={
            'captcha': captcha
        })

    def login(self, response):
        xsrf = response.xpath("//input[@name='_xsrf']/@value").extract_first()
        if xsrf is None:
            return ''
        post_url = 'https://www.zhihu.com/login/phone_num'
        post_data = {
            "_xsrf": xsrf,
            "phone_num": '15527037308',
            "password": 'reed6081509',
            "captcha": response.meta['captcha']
        }
        return [scrapy.FormRequest(url=post_url, formdata=post_data, headers=self.header, callback=self.check_login)]

    # 验证返回是否成功
    def check_login(self, response):
        js = json.loads(response.text)
        if 'msg' in js and js['msg'] == '登录成功':
            for url in self.start_urls:
                yield scrapy.Request(url=url, headers=self.header, dont_filter=True)