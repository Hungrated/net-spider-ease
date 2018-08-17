from bs4 import BeautifulSoup

"""

获取html内的说说动态列表

:param html html文本内容

"""


def get_moment_set(html):
    soup = BeautifulSoup(html, 'lxml')
    return soup.find(attrs={'id': 'msgList'}).find_all('li', attrs={'class': 'feed'})


"""

根据列表解析出说说信息

:param raw_arr 原始BeautifulSoup对象

"""


def get_parsed_moment(raw_arr):
    parsed_arr = []
    for raw in raw_arr:
        content_o, content_f = get_content(raw)
        parsed_arr.append({
            'pub_time': get_pub_time(raw),
            'content_o': content_o,
            'content_f': content_f,
            'img_list': get_img_list(raw),
            'like_cnt': get_like_cnt(raw)
        })
    return parsed_arr


"""

获取说说时间

:param raw 单条说说的原始BeautifulSoup对象

"""


def get_pub_time(raw):
    pub_time_raw = raw.find('div', attrs={'class': 'ft'})
    return pub_time_raw.find('a', attrs={'class': 'c_tx'}).get('title') if pub_time_raw is not None else ''


"""

获取说说内容

:param raw 单条说说的原始BeautifulSoup对象

"""


def get_content(raw):
    content = raw.find_all('pre')
    content_original = ''
    content_forwarded = ''
    if len(content) == 1:
        content_original = content[0].text
    elif len(content) == 2:
        content_original = content[0].text
        content_forwarded = content[1].text
    return content_original, content_forwarded


"""

获取图片列表

:param raw 单条说说的原始BeautifulSoup对象

"""


def get_img_list(raw):
    img_raw = raw.find_all('img')
    img_list = []
    if len(img_raw) > 0:
        for img in img_raw:
            if img.get('data-isphoto') is '1':
                img_list.append(img.get('data-src'))
    return img_list


"""

获取说说点赞数

:param raw 单条说说的原始BeautifulSoup对象

"""


def get_like_cnt(raw):
    like_raw = raw.find('div', attrs={'class': 'feed_like'})
    if like_raw is None:
        return 0
    like_cnt_raw = like_raw.find('a', attrs={'href': 'javascript:void(0);'})
    if like_cnt_raw is None:
        return 0
    return int(like_cnt_raw.text.replace('人', ''))
