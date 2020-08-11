#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-03 20:21
# @Author  : YaoJa
import unittest

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()


class TestSuite(unittest.TestCase):
    # 初始化
    @classmethod
    def setUpClass(cls):
        # 1、driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2、获取统一入口类
        cls.page_in = PageIn(driver)
        # 3、获取PageMisLogin对象并调用成功登陆依赖方法
        cls.page_in.page_get_PageMisLogin().page_mis_login_success()
        # 4、获取PageMisAudit对象
        cls.audit = cls.page_in.page_get_PageMisAudit()

    # 结束
    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_web_driver()

    # 测试发布文章审核业务方法
    # @pytest.mark.parametrize("article, channel", read_yaml("mis_audit.yaml"))
    def test_mis_article_audit(self, title=page.title, channel=page.channel):
        # 调查审核文章业务方法
        self.audit.page_mis_audit(title, channel)
        # 断言
        try:
            assert self.audit.page_assert_audit()
        except Exception as e:
            # 日志
            log.error(e)
            # 抛出异常
            raise
