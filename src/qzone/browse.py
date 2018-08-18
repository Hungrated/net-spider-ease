import time
from selenium import webdriver
from .account import *
from .encrypt import *
from .pages import *
from .moments import *

"""

等待指定秒数

:param secs 秒数

"""


def wait(secs):
    time.sleep(secs)


"""

滚动到页面底部

"""


def scroll_to_bottom(browser):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    return True


"""

完全加载动态页面内容

"""


def load_full_page(browser):
    print('loading full page...')
    wait(1)
    browser.execute_script(
        """
        (function () {
          var y = 0;
          var step = 200;
          window.scroll(0, 0);
          console.log(document.body.scrollHeight)

          function f() {
            if (y < document.body.scrollHeight - 200) {
              y += step;
              window.scroll(0, y);
              setTimeout(f, 150);
            } else {
              window.scroll(0, 0);
              document.title += "scroll-done";
            }
          }
          setTimeout(f, 1000);
        })();
        """
    )
    wait(5)
    return True


"""

获取html源码

"""


def get_html(browser):
    print('fetching page source...')
    wait(2)
    return browser.page_source


"""

WebDriver初始化

"""


def init():
    browser = webdriver.Chrome()
    browser.get('https://user.qzone.qq.com')

    print('switch to login frame...')
    browser.switch_to.frame('login_frame')
    log = browser.find_element_by_id('switcher_plogin')
    log.click()

    print('username & password input...')
    username = browser.find_element_by_id('u')
    username.send_keys(decrypt_str(USER_NAME))
    ps = browser.find_element_by_id('p')
    ps.send_keys(decrypt_str(USER_PWD))

    print('click the login button...')
    btn1 = browser.find_element_by_id('login_button')
    print('navigate to info center page...')
    btn1.click()
    wait(1)

    browser.get('https://user.qzone.qq.com/{}'.format(decrypt_str(USER_NAME)))
    wait(1)

    print('navigate to moment page...')
    btn2 = browser.find_element_by_xpath(".//*[@title='说说']")
    btn2.click()
    wait(1)

    load_full_page(browser)

    frame = browser.find_element_by_xpath('//*[@id="app_container"]/iframe')
    browser.switch_to.frame(frame)

    print('\n*** base browser env established. **\n')
    return browser


"""

销毁WebDriver浏览器

"""


def destroy(browser):
    print('quit browser...')
    browser.quit()
    print('\n*** done. **\n')
    return True


"""

加载说说指定页面

"""


def load_page_by_index(browser, index=1):
    index = str(index)
    print('\n*-> page to go: ', index)

    set_page = browser.find_element_by_xpath('//*[@class="mod_pagenav_option"]/span/input')
    set_page_btn = browser.find_element_by_xpath('//*[@class="mod_pagenav_option"]/span/button')

    set_page.clear()
    set_page.send_keys(index)
    set_page_btn.click()

    browser.switch_to_default_content()
    load_full_page(browser)
    frame = browser.find_element_by_xpath('//*[@id="app_container"]/iframe')
    browser.switch_to.frame(frame)

    return get_html(browser)


"""

获取单页说说数据

"""


def fetch_parsed_moments(browser, index):
    html = load_page_by_index(browser, index)
    raw_arr = get_moment_set(html)
    return get_parsed_moment(raw_arr)


"""

用WebDriver浏览QQ空间并返回说说数据

:param start 开始页数
:param page_cnt 爬取页数

"""


def browse_qzone_moments(start=None, page_cnt=None):
    moments = []
    browser = init()

    if start is None or start == 1:
        start = 1
        init_moment_info()
    if page_cnt is None:
        page_cnt = 1

    for i in range(start, start + page_cnt):
        arr = fetch_parsed_moments(browser, i)
        save_moment_info(arr)
        moments.extend(arr)

    destroy(browser)
    return moments
