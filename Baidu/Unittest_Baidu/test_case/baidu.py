from selenium import webdriver
from time import sleep
import unittest
# from test_case.public import quit


class Baidu(unittest.TestCase):
    def setUp(self):
        self.baidu = webdriver.Chrome()
        self.baidu.get("http://www.baidu.com")

    def test_Baidu(self):
        '''Baidu搜索验证'''
        self.baidu.find_element_by_id("kw").send_keys("selenium")
        self.baidu.find_element_by_id("su").submit()
        sleep(2)

    def tearDown(self):
        # quit.quit(self.Baidu)
        self.baidu.quit()


if __name__ == "__main__":
    unittest.main()
