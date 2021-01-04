import unittest
import HTMLTestRunner
# from test_case import Baidu,Tencent,wangyi
from test_case import *  # *在该处不是代表导入所有测试用例类的文件,而是导入了一个文件__init__
import time
import all_class_name
# 通过一个all-tests文件运行多个.py文件---简单的用例批量执行
# 只能运行和调用以test开头的函数用例
suite = unittest.TestSuite()
class_list = all_class_name.all_class_name()
for class_name in class_list:
    suite.addTest(unittest.makeSuite(class_name))

# suite.addTest(unittest.makeSuite(Baidu.Baidu)) #在一个叫做suite的容器中增加了一个类的
# suite.addTest(unittest.makeSuite(Tencent.Tencent))
# suite.addTest(unittest.makeSuite(wangyi.wangyi))
now_time = time.strftime("%Y-%m-%d %H.%M.%S")  # 写入小时和分钟的时候,不能使用冒号.可以使用.点代替
wz = "D:\\Unittest_Baidu\\report\\"+now_time+" result.html"  # 因为地址信息是字符串,所以可以将文件名和地址以及时间用加号相连
fp = open(wz, "wb")
HTMLTestRunner.HTMLTestRunner(stream=fp, title="Baidu的测试结果", description="Baidu的查询验证").run(suite)
# # print(time.ctime()) #current当前
# # print(time.localtime()) #打印当地时间


'''
1.优化了将多个py文件进行批量执行
2.易度测试报告,一定要注意缩进.必须是在用例函数的下面''"需要注释的内容''"
3.测试报告打印优化:1.测试报告加上运行的时间+不会被覆盖,每一次都会产生一份报告
    #希望产生的文件名字不是test.html,而是取名为:2019-10-09 11:30:00result.html
4.结构优化,将测试用例单独放置到制定文件夹中,以后需要添加用例,去制定的test_case下添加
    #新建文件夹的时候,需要新建python的包体文件夹,会比普通文件夹多了一个__init__.py的初始文件,没有任何含义
5.优化导入文件,每次增加一条用例,不需要再all_tests文件中增加导入类的功能
6.优化当前用例中出现公共模块的时候,可以单独拿出来自定义一个函数,用来进行调用:公用模块的处理
7.优化测试用例的读取


'''
