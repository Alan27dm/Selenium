from selenium import webdriver
from time import sleep
import unittest
# from test_case.public import quit


class Baidu(unittest.TestCase):
    def setUp(self):
        self.Baidu=webdriver.Chrome()
        self.Baidu.get("http://www.baidu.com")
    def test_Baidu(self):
        '''Baidu搜索验证'''
        self.Baidu.find_element_by_id("kw").send_keys("selenium")
        self.Baidu.find_element_by_id("su").submit()
        sleep(2)
    def tearDown(self):
        # quit.quit(self.Baidu)
        Baidu.quit()
if __name__=="__main__":
    unittest.main()
