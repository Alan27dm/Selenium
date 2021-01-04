#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time		: 04/01/2021 11:53
# @File		: main_test_ue.py


import unittest
import time
import os
import HTMLTestRunner
from test_case import *


from all_class_name import all_class_name
suite = unittest.TestSuite()
for class_name in all_class_name():
    suite.addTest(unittest.makeSuite(class_name))
now_time = time.strftime("%Y-%m-%d %H.%M.%S")
wz = os.path.sep.join([os.path.dirname(__file__), 'report', '']) + f"{now_time}_result.html"
fp = open(wz, "wb")
HTMLTestRunner.HTMLTestRunner(stream=fp, title="Baidu Search的测试结果", description=":Baidu的查询验证").run(suite)
