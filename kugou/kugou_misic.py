# encoding=utf-8
# Time    : 2018/10/28
# Language: Python 3
import requests
import json

class KgDownLoader(object):
    def __init__(self):
        self.search_url = 'http://songsearch.kugou.com/song_search_v2?callback=jQuery191034642999175022426_1489023388639&keyword={}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_=1489023388641'
        # .format('张玮 - 吻得太逼真 (Live)')
        self.play_url = 'http://www.kugou.com/yy/index.php?r=play/getdata&hash={}'
        self.song_info = {
                '歌名': None,
                '演唱者': None,
                '专辑': None,
                'filehash': None,
                'mp3url': None
            }

    def get_search_data(self, keys):
        search_file = requests.get(self.search_url.format(keys))
        search_html = search_file.content.decode().replace(')', '').replace('jQuery191034642999175022426_1489023388639(', '')
        views = json.loads(search_html)
        for view in views['data']['lists']:
            song_name = view['SongName'].replace('<em>', '').replace('</em>', '')
            album_name = view['AlbumName'].replace('<em>', '').replace('</em>', '')
            sing_name = view['SingerName'].replace('<em>', '').replace('</em>', '')
            file_hash = view['FileHash']
            new_info = {
                '歌名': song_name,
                '演唱者': sing_name,
                '专辑': album_name if album_name else None,
                'filehash': file_hash,
                'mp3url': None
            }
            self.song_info.update(new_info)
            yield self.song_info

    def get_mp3_url(self, filehash):
        mp3_file = requests.get(self.play_url.format(filehash)).content.decode()
        mp3_json = json.loads(mp3_file)
        real_url = mp3_json['data']['play_url']
        self.song_info['mp3url'] = real_url
        yield self.song_info

    def save_mp3(self, song_name, real_url):
        #print(real_url)
        with open(song_name + ".mp3", "wb")as fp:
            fp.write(requests.get(real_url).content)

if __name__ == '__main__':
    kg = KgDownLoader()
    mp3_info = kg.get_search_data(input('请输入歌名：'))
    for x in mp3_info:
        mp3info = kg.get_mp3_url(x['filehash'])
        for info in mp3info:
            name = info['歌名']
            url = info['mp3url']
            #print('url: ' + url)
            try:
                kg.save_mp3(name, url)
            except:
                print('name: ' + name)
                print('url: ' + url)
