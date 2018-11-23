import requests
from HandleJs import Py4Js

#调用google在线翻译
class GoogleTranslate:
    def __init__(self):
        self.MAX_LEN = 5000

    def translate_core(self, tk, content):
        if len(content) > self.MAX_LEN:
            print("翻译的长度超过限制！！！")
            return ''
     
        param = {'tk': tk, 'q': content}

        result = requests.get("""http://translate.google.cn/translate_a/single?client=t&sl=en
            &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss
            &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2""", params=param)

        cn_info = ''
        text_info = result.json()[0]
        for text in text_info:
            if text[0] != None:
                cn_info = cn_info + text[0]

        return cn_info

    def translate_normal(self, content):
        js = Py4Js()
        tk = js.getTk(content)

        return self.translate_core(tk, content)

    def translate_cn(self, content):
        all_len = len(content)
        if all_len >= self.MAX_LEN:
            content_list = content.split('\n')
            content_en = ''
            content_cn = ''
            for i in range(0, len(content_list)):
                content_en = content_en + content_list[i]
                if len(content_en) < self.MAX_LEN:
                    content_cn = content_cn + self.translate_normal(content_en)
                    content_en = ''

            return content_cn
        else:
            return self.translate_normal(content)
