import requests
import json
import os
import re
from urllib import request
from PIL import Image
from bs4 import BeautifulSoup
from lxml import etree

class Captchar:
    def __init__(self):
        self.url = 'https://www.cvedetails.com/cdn-cgi/scripts/baidu.challenge.js'
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0"} 

    def get_captchar_url(self):
    	#https://captcha.su.baidu.com/image/?session=4e66d2d900d99f88f446cad677c98305_MTU0Mjk2MTA3MS4zNjI=_10.23.236.14&pub=377e4907e1a3b419708dbd00df9e8f79
        print(self.url)

        #1.pub
        #https://captcha.su.baidu.com/session_cb/?pub=377e4907e1a3b419708dbd00df9e8f79&callback=callback
        response = requests.get(self.url, headers=self.headers)
        pub = response.text.split(',f="')[-1].split('"')[0]
        print('pub=' + pub)
        pub_url = 'https://captcha.su.baidu.com/session_cb/?pub=%s&callback=callback' % (pub)
        
        #2.session
        response = requests.get(pub_url, headers=self.headers)
        resp_text = response.text.replace('callback(', '')
        len_text = len(resp_text) -1 
        json_dict =json.loads(resp_text[:len_text])
        session = json_dict['sessionstr']
        print('session=' + session)
        captcha_url = 'https://captcha.su.baidu.com/image/?session=%s&pub=%s' % (session, pub)
        print('captcha_url:' + captcha_url)

        return captcha_url

    def input_chptchar(self, base_url):
        print('base_url:' + base_url)
        response = requests.get(base_url, headers=self.headers)
        #<h2 class="yjs-subheadline"><span data-translate="complete_sec_check">输入验证码，可以浏览</span> www.cvedetails.com</h2>
        soup = BeautifulSoup(response.text, 'lxml')
        results = soup.find('h2', class_="yjs-subheadline")
        print(results.text)

        request.urlretrieve(self.get_captchar_url(), 'captcha.jpg')
        try:
            im = Image.open('captcha.jpg')
            im.show()
            im.close()
        except:
            print(u'请到 %s 目录找到captcha.jpg 手动输入' % os.path.abspath('captcha.jpg'))
        captcha = input("please input the captcha\n>")

if __name__ == '__main__':
	base_url = 'https://www.cvedetails.com'
	captchar = Captchar()
	captchar.input_chptchar(base_url)
