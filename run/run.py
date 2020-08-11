#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 15:17
# @Author  : Chris.Ma
# 测试用例发现，使用htmltestrunner去运行测试用例
import time
import unittest
import os
import htmlTestRunner
# from scripts.test02_mp_article import TestSuite
from scripts.test02_mp_article import TestSuite
from config import BASE_PATH
# from scripts.test04_mis_audit import TestSuite


class TestRunner(object):
    def __init__(self):
        self.suite = unittest.TestLoader().loadTestsFromTestCase(TestSuite)
        cur_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        file_name = cur_date + ".html"
        # self.report_folder = BASE_PATH + os.sep + "report" + os.sep + file_name
        # self.report_folder = "report" + os.sep + file_name

    def startrun(self, name, title):
        package_path = os.path.abspath("..")
        file_path = os.path.join(package_path, "report")
        os.chdir(file_path)
        now = time.strftime("%Y-%m-%d_%H_%M_%S")
        file_name = title + now + ".html"
        fp = open(file_name, "wb")
        runner = htmlTestRunner.HTMLTestRunner(stream=fp, title=name, description=title)
        runner.run(self.suite)
        fp.close()


if __name__ == '__main__':
    # 执行用例
    tr = TestRunner()
    tr.startrun("测试套件", "自动化测试")