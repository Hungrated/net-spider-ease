import requests
from bs4 import BeautifulSoup
import re

# 修改header假装浏览器访问
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/68.0.3440.106 Safari/537.36 '

headers = {'user-agent': user_agent}

# 将目标网站定为网易云音乐
BASE_URL = 'https://music.163.com'
