import time
from selenium import webdriver
from .account import *
from .encrypt import *

"""

用WebDriver浏览QQ空间

"""


def browse_qzone_moments(start=None, end=None):
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
    btn1 = browser.find_element_by_id('login_button')
    time.sleep(1)
    btn1.click()

    print('navigate to info center page...')
    time.sleep(1)
    browser.get('https://user.qzone.qq.com/{}'.format(decrypt_str(USER_NAME)))

    print('navigate to moment page...')
    time.sleep(1)
    btn2 = browser.find_element_by_xpath(".//*[@title='说说']")
    btn2.click()

    print('loading full page...')
    time.sleep(1)
    browser.execute_script(
        """
        (function () {
          var y = 0;
          var step = 100;
          window.scroll(0, 0);

          function f() {
            if (y < (document.body.scrollHeight)/5) {
              y += step;
              window.scroll(0, y);
              setTimeout(f, 100);
            } else {
              window.scroll(0, 0);   //滑动到顶部
              document.title += "scroll-done";
            }
          }
          setTimeout(f, 1000);
        })();
        """
    )

    print('fetching page source...')
    time.sleep(3)

    frame = browser.find_element_by_xpath('//*[@id="app_container"]/iframe')
    browser.switch_to.frame(frame)
    html = browser.page_source

    time.sleep(1)
    print('quit browser...')
    browser.quit()

    print('done.')
    return html
