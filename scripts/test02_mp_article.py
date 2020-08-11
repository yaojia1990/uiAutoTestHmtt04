#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-02 10:20
# @Author  : YaoJa
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
import unittest

from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()


# class TestSuite(unittest.TestCase):
class TestSuite():
    # 1、初始化
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2、获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3、获取PageMpLogin对象并调用成功登陆依赖方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 4、获取PageMpArticle页面对象
        self.article = self.page_in.page_get_PageMpArticle()
    # @classmethod
    # def setUpClass(cls):
    #     # 1、获取driver
    #     driver = GetDriver.get_web_driver(page.url_mp)
    #     # 2、获取统一入口类对象
    #     cls.page_in = PageIn(driver)
    #     # 3、获取PageMpLogin对象并调用成功登陆依赖方法
    #     cls.page_in.page_get_PageMpLogin().page_mp_login_success()
    #     # 4、获取PageMpArticle页面对象
    #     cls.article = cls.page_in.page_get_PageMpArticle()

    # 2、结束
    def teardown_class(self):
        GetDriver.quit_web_driver()
    # @classmethod
    # def tearDownClass(cls):
    #     GetDriver.quit_web_driver()

    # 3、测试发布文章方法
    @pytest.mark.parametrize("title, content, expect, channel", read_yaml("mp_article.yaml"))
    # @pytest.mark.parametrize("title, content, expect, channel", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect, channel):
        # 调用发布文章业务
        print("所选频道是:{}".format(channel))
        self.article.page_mp_article(title, content)
        # 查看断言信息
        # print("发布文章结果为：", self.article.page_get_info())
        try:
            assert expect == self.article.page_get_info()
        except Exception as e:
            log.error(e)
            raise


if __name__ == "__main__":
    unittest.main()
