__author__ = 'Administrator'

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class Global:
    Url = "http://www.baidu.com"
    BaseBrowser = webdriver.Chrome
    options = webdriver.ChromeOptions()

    class InitParams:
        WindowSize = {'width': 800, 'height': 600}


Global.options.add_argument('disable-infobars')
Global.options.add_argument(f'--app=chrome://settings/clearBrowserData')
Global.options.add_experimental_option('excludeSwitches', ['enable-automation'])
Global.options.add_argument('--no-sandbox')
Global.options.add_argument(f'--app={Global.Url}')
Global.options.page_load_strategy = 'none' # eager
