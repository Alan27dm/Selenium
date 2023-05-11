from test_case.public import *


class Wangyi(unittest.TestCase):

    def setUp(self):
        self.wangyi = webdriver.Chrome(options=Global.options)
        self.wangyi.set_window_size(**Global.InitParams.WindowSize)
        self.wangyi.implicitly_wait(10)
        self.wangyi.get(Global.Url)

    def test_wangyi(self):
        '''验证网易搜索'''
        self.wangyi.find_element(By.ID, "kw").send_keys("网易")
        self.wangyi.find_element(By.ID, "su").click()
        sleep(5)

    def tearDown(self):
        self.wangyi.quit()


if __name__ == "__main__":
    unittest.main()
