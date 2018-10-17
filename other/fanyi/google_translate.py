#coding=utf-8
import urllib.request
from HandleJs import Py4Js
import requests
import time

class GoogleTranslate:
    content = ''
    language = 'en'

    # Example: find_last('aaaa', 'a') returns 3
    # Make sure your procedure has a return statement.
    def __init__(self):
    	self.content = ''
    	self.language = 'en'
    
    def find_last(self, string, str):
        last_position=-1
        while True:
            position=string.find(str,last_position+1)
            if position==-1:
                return last_position
            last_position=position  

    def open_url(sefl, url):    
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}      
        req = urllib.request.Request(url = url,headers=headers)    
        response = urllib.request.urlopen(req)    
        data = response.read().decode('utf-8')    
        return data

    def translate_core(self, content, tk, language):    
        if len(content) > 4891:    
            print("too long byte >4891")
            return

        content = urllib.parse.quote(content)    

        if language == 'de':
            url = "http://translate.google.cn/translate_a/single?client=t"+ "&sl=de&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"+"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"+"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(tk,content)    
        else:
            url = "http://translate.google.cn/translate_a/single?client=t"+ "&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca"+"&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1"+"&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(tk,content)    

        #result为json格式
        #print('url' + url)
        result = self.open_url(url)    
        #print('results:' + result)

        if len(content) < 10:
            end = result.find("\",")  
            if end > 4:  
                return result[4:end]
        else:
            result_all = ''
            if language == 'de':
                result_all = result.split(',null,"de",null,null,')[0].replace('[[', '').replace(']]', ']')[1:]
            else:
                result_all = result.split(',null,"en",null,null,')[0].replace('[[', '').replace(']]', ']')[1:]
            
            #print('result_all:' + result_all)

            output_cn = ''
            #解析中文字段并拼接
            list = result_all.split('],[')
            for i in range(len(list)-1):
                end = list[i].find("\",")
                tmp_buf = list[i][1:end]
                output_cn = output_cn + tmp_buf
            return output_cn

    def translate_normal(self, content, language):    
        js = Py4Js()    

        tk = js.getTk(content)
        #print('#英文#:' + content)
        cn_buf = self.translate_core(content, tk, language)
        #print('#中文#:' + cn_buf)

        return cn_buf

    def translate_cn(self, content, language):
        LEN_LIMIT = 4891
        all_len = len(content)
        #print('en:' + content)
        #time.sleep(0.1)
        if all_len > LEN_LIMIT:
            content_cn = ''
            while True:
                content_limit = content[0:LEN_LIMIT]
                limit_end = self.find_last(content_limit, '.') + 1
                #print('limit_end:' + str(limit_end))
                if limit_end == 0:
                    limit_end = self.find_last(content_limit, ' ') + 1
                    if limit_end == 0:
                        limit_end = LEN_LIMIT
                content_en = content[0:limit_end]
                leave_len = all_len - limit_end
                if content_en == '':
                    break;
                #print('content_en:' + content_en)
                content_cn = content_cn + self.translate_normal(content_en, language);
                content = content[limit_end:]
     
            return content_cn
        else:
            return self.translate_normal(content, language)