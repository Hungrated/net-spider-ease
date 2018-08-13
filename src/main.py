import requests
from bs4 import BeautifulSoup
import re

# 修改header假装浏览器访问
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

headers = {'user-agent': user_agent}

'''

获取页面html文本信息

:param url 页面url

'''
def get_page_content(url):
    try:
        r = requests.get(url, headers=headers)
    finally:
        return r.text

'''

获取html内的目标信息

:param html html文本内容
:param tagname 标签名
:param attr 标签属性名
:param regexp 要匹配的正则表达式（仅在有标签名传入时有效）

'''
def get_objective_set(html, tagname, attr, regexp):
    soup = BeautifulSoup(html, 'lxml')
    temp_arr = []
    attr_flag = False
    re_flag = False
    if attr is not None:
        attr_flag = True
    if regexp is not None:
        re_flag = True
    for raw in soup.find_all(tagname):
        if raw is not None:
            if re_flag and attr_flag:
                if raw.get(attr) is not None:
                    temp = raw.get(attr) if attr_flag else raw
                    if re.search(regexp, temp) is not None:
                        temp_arr.append(temp)
            elif re_flag:
                temp_arr.append(raw)
            elif attr_flag:
                temp = raw.get(attr)
                if temp is not None:
                    temp_arr.append(temp)
            else:
                temp_arr.append(raw)
    return temp_arr

# 将目标网站定为网易云音乐
BASE_URL = 'https://music.163.com'

# 获取页面html
html1 = get_page_content(BASE_URL)

# 获取页面中导航网址信息
obj_arr1 = get_objective_set(html1, 'a', 'href', '^(/discover/)')

print(obj_arr1)

# 获取二级页面中歌手链接信息
html2 = get_page_content(BASE_URL + obj_arr1[3])
obj_arr2 = get_objective_set(html2, 'a', 'href', '^(/discover/)')

print(obj_arr2)
