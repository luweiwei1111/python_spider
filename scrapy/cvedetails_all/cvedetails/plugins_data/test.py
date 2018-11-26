# -*- coding:utf-8 -*-
import requests
import re
import PyV8
import codecs
from fake_useragent import UserAgent

class GoogleTranslate:
    def __init__(self,content):
        self.content = content
        ua = UserAgent()
        self.headers = {
            'User-Agent':ua.random
        }

    # 从网页解析出TKK函数
    def get_TKK(self):
        weburl = 'http://translate.google.cn/'
        response = requests.get(weburl,headers=self.headers).text
        result = re.findall(r'(TKK.+?\);)',response)[0]
        result = re.findall(r"TKK=eval\('(.+)'\);",result)[0] + ';'
        return result

    # 破解tk，拿到tk值
    def get_tk(self):
        with PyV8.JSContext() as ctxt:
            # 恢复'\x'的转义功能
            TKK = codecs.getdecoder("unicode_escape")(self.get_TKK())[0]
            func = ctxt.eval(TKK)
            ctxt.eval("""
            var b = function (a, b) {
            for (var d = 0; d < b.length - 2; d += 3) {
                var c = b.charAt(d + 2),
                    c = "a" <= c ? c.charCodeAt(0) - 87 : Number(c),
                    c = "+" == b.charAt(d + 1) ? a >>> c : a << c;
                a = "+" == b.charAt(d) ? a + c & 4294967295 : a ^ c
            }
            return a
        }
        var tk =  function (a,TKK) {
            for (var e = TKK.split("."), h = Number(e[0]) || 0, g = [], d = 0, f = 0; f < a.length; f++) {
                var c = a.charCodeAt(f);
                128 > c ? g[d++] = c : (2048 > c ? g[d++] = c >> 6 | 192 : (55296 == (c & 64512) && f + 1 < a.length && 56320 == (a.charCodeAt(f + 1) & 64512) ? (c = 65536 + ((c & 1023) << 10) + (a.charCodeAt(++f) & 1023), g[d++] = c >> 18 | 240, g[d++] = c >> 12 & 63 | 128) : g[d++] = c >> 12 | 224, g[d++] = c >> 6 & 63 | 128), g[d++] = c & 63 | 128)
            }
            a = h;
            for (d = 0; d < g.length; d++) a += g[d], a = b(a, "+-a^+6");
            a = b(a, "+-3^+b+-f");
            a ^= Number(e[1]) || 0;
            0 > a && (a = (a & 2147483647) + 2147483648);
            a %= 1E6;
            return a.toString() + "." + (a ^ h)
        }
            """)
            vars = ctxt.locals
            Tkk = vars.tk
            tk = Tkk(self.content,func)
            print(tk)
            return tk

    # 返回目标翻译结果，输入语言随机，翻译结果语言为中文
    def get_translated(self):
        tk = self.get_tk()
        url = "https://translate.google.cn/translate_a/single"
        params = {
        "client":"t",
        "sl":"auto",
        "tl":"zh-CN",
        "hl":"zh-CN",
        "dt":"at",
        "dt":"bd",
        "dt":"ex",
        "dt":"ld",
        "dt":"md",
        "dt":"qca",
        "dt":"rw",
        "dt":"rm",
        "dt":"ss",
        "dt":"t",
        "ie":"UTF-8",
        "oe":"UTF-8",
        "otf":"2",
        "ssel":"0",
        "tsel":"0",
        "kc":"1",
        "tk":tk,
        "q":self.content,
        }
        content = requests.get(url,params=params,headers=self.headers).text
        content = content.replace('null','None')
        print(content)
        li = eval(content)
        result = li[0]
        result_list = []
        for i in result:
            result_list.append(i[0])
        print(result_list)
        if len(result_list[0])<30:
            print(result_list[0])
            return result_list[0].strip()
        else:
            result = result_list[0].split(' ')[0]
            return result.strip()

if __name__ == '__main__':
    content = '魔法能穿墻？'
    go = GoogleTranslate(content)
    file_name = go.get_translated()
    print(file_name)