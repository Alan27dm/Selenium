import sys
# 添加了这个path到sys了，就可以在其他位置导入上层目录的public模块了
# 添加这个是适合使用from public import * 而不是 from test_case.public import *
# 后者的导入方式不需要添加这个sys.asyncpath
sys.path.extend(['./', '../'])

# 如果在 最顶层的main.py or run.py下运行，这样倒入会报错
# ModuleNotFoundError: No module named 'public'
# 下面这样导入只是适合在当前这个文件运行
# from public import *

from test_case.public import *


class Baidu(unittest.TestCase):

    def setUp(self):
        self.baidu = webdriver.Chrome(options=Global.options)
        self.baidu.set_window_size(**Global.InitParams.WindowSize)
        self.baidu.implicitly_wait(10)
        self.baidu.get(Global.Url)

    def test_Baidu(self):
        '''Baidu搜索验证'''
        self.baidu.find_element(By.ID, "kw").send_keys("selenium")
        self.baidu.find_element(By.ID, "su").submit()
        sleep(5)  # 演示用，实际不需要

    def tearDown(self):
        self.baidu.quit()


if __name__ == "__main__":
    unittest.main()
