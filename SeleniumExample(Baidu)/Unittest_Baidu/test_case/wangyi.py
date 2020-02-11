from selenium import webdriver
from time import sleep
import unittest
from test_case.public import quit

class wangyi(unittest.TestCase):
    def setUp(self):
        self.wangyi=webdriver.Chrome()
        self.wangyi.get("http://www.baidu.com")
    def test_wangyi(self):
        '''验证网易搜索'''
        self.wangyi.find_element_by_id("kw").send_keys("网易")
        self.wangyi.find_element_by_id("su").submit()
        sleep(2)
    def tearDown(self):
        quit.quit(self.wangyi)
if __name__=="__main__":
    unittest.main()
