from selenium import webdriver
from time import sleep
import unittest
from test_case.public import quit

class Tencent(unittest.TestCase):
    def setUp(self):
        self.Tencent=webdriver.Chrome()
        self.Tencent.get("http://www.baidu.com")
    def test_Tencent(self):
        '''验证腾讯搜索功能'''
        self.Tencent.find_element_by_id("kw").send_keys("Tencent")
        self.Tencent.find_element_by_id("su").submit()
        sleep(2)
    def tearDown(self):
        quit.quit(self.Tencent)
if __name__=="__main__":
    unittest.main()

