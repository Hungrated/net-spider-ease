# -*- coding:utf-8 -*-

from .base import *

"""

获取歌手信息

:param start id下限
:param end id上限

"""


def get_artist_info(start, end):
    artist_info_arr = []
    for i in range(start, end):
        a = get_page_content(BASE_URL + '/artist?id=' + str(i))
        tlt = BeautifulSoup(a, 'lxml').title.text
        if tlt != "网易云音乐":
            artist_name = tlt.replace(" - 歌手 - 网易云音乐", "")
            artist_info = (i, tlt.replace(" - 歌手 - 网易云音乐", ""))
            artist_info_arr.append(artist_info)
            print("id: " + str(i) + ", artist: " + artist_name)
    return artist_info_arr
