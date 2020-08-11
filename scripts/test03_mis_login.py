#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-02 19:46
# @Author  : YaoJa
import unittest

import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


class TestMisAudit():
    # 1、初始化
    # @classmethod
    # def setUpClass(cls):
    #     # 1、获取driver
    #     driver = GetDriver.get_web_driver(page.url_mis)
    #     # 2、获取统一入口类对象
    #     cls.page_in = PageIn(driver)
    #     # 3、获取PageMisLogin对象
    #     cls.mis = cls.page_in.page_get_PageMisLogin()
    def setup_class(self):
        # 1、获取driver
        driver = GetDriver.get_web_driver(page.url_mis)
        # 2、获取统一入口类对象
        self.page_in = PageIn(driver)
        # 3、获取PageMisLogin对象
        self.mis = self.page_in.page_get_PageMisLogin()

    # 2、结束
    # @classmethod
    # def tearDownClass(cls):
    #     GetDriver.quit_web_driver()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    # 3、登录测试业务方法
    @pytest.mark.parametrize("username, password, expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, password, expect):
        # 1、调用登录业务方法
        self.mis.page_mis_login(username, password)
        # 2、调用断言信息
        # print("获取的昵称为：", self.mis.page_get_nickname())
        try:
            assert expect in self.mis.page_get_nickname()
        except Exception as e:
            print("错误原因为：", e)
