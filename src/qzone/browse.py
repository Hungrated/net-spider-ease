import time
from selenium import webdriver
from .account import *
from .encrypt import *

"""

用WebDriver浏览QQ空间

"""


def browse_qzone():
    browser = webdriver.Chrome()
    browser.get('https://user.qzone.qq.com')

    print('switch to login frame...')
    browser.switch_to.frame('login_frame')
    log = browser.find_element_by_id('switcher_plogin')
    log.click()

    print('username & password input...')
    time.sleep(1)
    username = browser.find_element_by_id('u')
    username.send_keys(decrypt_str(USER_NAME))
    ps = browser.find_element_by_id('p')
    ps.send_keys(decrypt_str(USER_PWD))

    print('click the login button...')
    btn = browser.find_element_by_id('login_button')
    time.sleep(1)
    btn.click()

    print('navigate to user home page...')
    time.sleep(1)
    browser.get('https://user.qzone.qq.com/{}'.format(decrypt_str(USER_NAME)))

    print('fetching page source...')
    html = browser.page_source
    print(html)

    print('quit browser...')
    browser.quit()
