from .base import *

"""

获取页面html文本信息

:param url 页面url

"""


def get_page_content(url):
    try:
        r = requests.get(url, headers=headers)
    finally:
        return r.text


"""

将获取内容统一转为utf-8编码

:param raw 输入字符串

"""


def get_decoded_content(raw):
    content = bytes(raw, 'UTF-8')
    return content.decode('UTF-8')


"""

获取歌手描述页面html文本信息

:param url 页面url

"""


def get_desc_page(artist_id):
    return get_page_content(BASE_URL + '/artist/desc?id=' + str(artist_id))


"""

获取html内的目标信息列表

:param html html文本内容
:param tagname 标签名
:param attr 标签属性名
:param regexp 要匹配的正则表达式（仅在有标签名传入时有效）

"""


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
                        temp_arr.append(get_decoded_content(temp))
            elif re_flag:
                temp_arr.append(get_decoded_content(raw))
            elif attr_flag:
                temp = raw.get(attr)
                if temp is not None:
                    temp_arr.append(get_decoded_content(temp))
            else:
                temp_arr.append(get_decoded_content(raw))
    return temp_arr