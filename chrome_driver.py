from selenium import webdriver
from fake_useragent import UserAgent
import platform
import sys
import os
import random
import time
import numpy as np


def sleep_random_time(t1: int, t2: int):
    """
    隨機 sleep t1~t2 s 時間
    :param t1: t1
    :param t2: t2
    :return: None
    """
    ts = random.randint(t1, t2)
    time.sleep(ts)


def sleep_time(t1: float):
    """
    sleep t1 s
    :param t1: t1
    :return: None
    """
    time.sleep(t1)


def set_options(chrome_type: str, show: bool = True):
    """
    set chrome options
    :param chrome_type: chromedriver or geckodriver
    :param show: show windows
    :return:
    """
    user_agent = UserAgent().random
    if chrome_type == 'chromedriver':
        # init google chrome options
        options = webdriver.ChromeOptions()

        # options.add_argument("--disable-gpu")
        # 不載入圖片
        # options.add_argument('blink-settings=imagesEnabled=false')
        options.add_argument('--user-agent=%s' % user_agent)

        # 不顯示畫面(linux不需要GUI顯示查看)
        if not show:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument("window-size=1920,1080")

            # 設定瀏覽器大小(滿版)
            # options.add_argument("--start-maximized")
            # options.add_argument("window-size=1920,1080")
        return options

    elif chrome_type == 'geckodriver':
        # init firefox chrome options
        options = webdriver.FirefoxOptions()

        # 不載入圖片
        # options.add_argument("--disable-gpu")
        # options.add_argument('blink-settings=imagesEnabled=false')
        options.add_argument('--user-agent=%s' % user_agent)

        # 不顯示畫面(因linux不需要GUI顯示查看)
        if not show:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument("window-size=1920,1080")
            # 設定瀏覽器大小(滿版)
            # options.add_argument("--start-maximized")
            # options.add_argument("window-size=1920,1080")
        return options
    else:
        return None


def get_chrome_driver(show: bool = True):
    """
    get chrome driver(需先下載driver)
    :param show: show windows
    :return:
    """
    # 回傳資訊
    log_message = ""

    # chrome exe and driver setting
    driver = None
    try:
        # google chromedriver geckodriver
        chrome_path = 'chromedriver'
        if platform.system() == 'Linux':
            chrome_path = 'chromedriver'
            # if not os.path.isfile(chrome_path):
            #     chrome_path = 'geckodriver'
        else:
            # windows
            # chrome_path = 'chromedriver.exe'
            chrome_path = './chrome-win64/chrome.exe'

        if os.path.isfile(chrome_path):
            options = set_options(chrome_type="chromedriver", show=show)
            # 新版本executable_path會出錯
            # driver = webdriver.Chrome(options=options, executable_path=os.path.abspath(chrome_path))
            driver = webdriver.Chrome(options=options)
            if show:
                driver.maximize_window()
            log_message = '{} open'.format(chrome_path)
        else:
            driver = None
            log_message = '{} is not exist'.format(chrome_path)
    except Exception as e:
        log_message = e
        driver = None
    finally:
        if driver is None:
            log_message = "chrome driver is not exist"
            driver = None
            # sys.exit()  # 離開程式
        return log_message, driver


def get_remote_chrome_driver(ip='http://localhost:4444/wd/hub'):
    # 使用已經建立好環境取的driver(Docker)
    # chrome exe and driver setting
    driver = None
    try:
        # init google chrome options
        options = webdriver.ChromeOptions()

        user_agent = UserAgent().random
        options.add_argument('--user-agent=%s' % user_agent)

        # 不顯示畫面(linux不需要GUI顯示查看)
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--incognit")
        options.add_argument("--disable-application-cache")
        options.add_argument('--disable-dev-shm-usage')

        # 設定瀏覽器大小(滿版)
        # options.add_argument("--start-maximized")
        options.add_argument("window-size=1920,1080")

        driver = webdriver.Remote(
            command_executor=ip,
            options=options  # webdriver.ChromeOptions(),
        )
        driver.maximize_window()
        return driver, "open {}".format(ip)
    except Exception as e:
        return None, e


def slider_window(driver):
    """
    silder windows
    :param driver: chrome driver
    :return:
    """
    # 隨機停止秒數
    sleep_random_time(t1=1, t2=5)
    # 隨機滑動
    # Get scroll height
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    random_size = random.randint(5, 10)
    random_scroll = np.random.randint(scroll_height, size=random_size)
    random_scroll.sort()
    for rs in random_scroll:
        js = 'window.scrollBy(0,{})'.format(rs)
        driver.execute_script(js)
        ts1 = random.randint(1, 10) / 10
        sleep_time(t1=ts1)
    # 隨機停止秒數
    sleep_random_time(t1=1, t2=5)
