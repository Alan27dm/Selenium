from test_case.public import *


class Tencent(unittest.TestCase):

    def setUp(self):
        self.tencent = webdriver.Chrome(options=Global.options)
        self.tencent.set_window_size(**Global.InitParams.WindowSize)
        self.tencent.implicitly_wait(10)
        self.tencent.get(Global.Url)

    def test_Tencent(self):
        '''验证腾讯搜索功能'''
        self.tencent.find_element(By.ID, "kw").send_keys("Tencent")
        self.tencent.find_element(By.ID, "su").submit()
        sleep(5)

    def tearDown(self):
        self.tencent.quit()


if __name__ == "__main__":
    unittest.main()
