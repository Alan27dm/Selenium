from selenium import webdriver
from time import sleep
import unittest
from test_case.public import quit


class Taobao(unittest.TestCase):
    def setUp(self):
        self.taobao = webdriver.Chrome()
        self.taobao.get("http://www.baidu.com")

    def test_taobao(self):
        '''验证腾讯搜索功能'''
        self.taobao.find_element_by_id("kw").send_keys("taobao")
        self.taobao.find_element_by_id("su").submit()
        sleep(2)

    def tearDown(self):
        quit.quit(self.taobao)


if __name__ == "__main__":
    unittest.main()
