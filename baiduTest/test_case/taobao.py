import sys

sys.path.extend(['./', '../'])  # 为了导入上层目录的public模块
from test_case.public import *


class Taobao(unittest.TestCase):

    def setUp(self):
        self.taobao = webdriver.Chrome(options=Global.options)
        self.taobao.set_window_size(**Global.InitParams.WindowSize)
        self.taobao.implicitly_wait(10)
        self.taobao.get(Global.Url)

    def test_taobao(self):
        '''验证腾讯搜索功能'''
        self.taobao.find_element(By.ID, "kw").send_keys("taobao")
        self.taobao.find_element(By.ID, "su").submit()
        sleep(5)

    def tearDown(self):
        self.taobao.quit()


if __name__ == "__main__":
    unittest.main()
