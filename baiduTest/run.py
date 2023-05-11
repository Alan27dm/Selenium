#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time		: 04/01/2021 11:53
# @File		: main_test_ue.py

import unittest
import time
# 使用官方的报告只需要去掉下面这一行导入的下划线
from _HtmlTestRunner import HTMLTestRunner
from pathlib import Path
from test_case import *
import sys

sys.path.extend(['./', '../'])

suite = unittest.TestSuite()
for module in modules:
    clsName = eval(f'{module}.{module.capitalize()}')
    suite.addTest(unittest.makeSuite(clsName))

now_time = time.strftime("%Y-%m-%d %H.%M.%S")
wz = Path(__file__).parent.absolute() / 'reports' / f"{now_time}_result.html"
print('Report:', wz)
with open(wz, "wb") as fp:
    HTMLTestRunner(stream=fp, title="Baidu Search的测试结果", description="Baidu的查询验证").run(suite)
    # unittest.TestProgram(testRunner=HTMLTestRunner()) # 官方的报告
