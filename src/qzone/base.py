# 修改header假装浏览器访问
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/68.0.3440.106 Safari/537.36 '

headers = {'user-agent': user_agent}

# 将目标网站定为QQ空间
BASE_URL = 'https://user.qzone.md.qq.com/295415658/'

"""

将获取内容统一转为utf-8编码

:param raw 输入字符串

"""


def get_decoded_content(raw):
    content = bytes(raw, 'UTF-8')
    return content.decode('UTF-8')
