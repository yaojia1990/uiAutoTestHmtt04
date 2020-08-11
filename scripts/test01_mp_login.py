#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 20:40
# @Author  : YaoJa
"""测试脚本"""
import pytest
from page.page_in import PageIn
from tools.get_driver import GetDriver
import page
from tools.read_yaml import read_yaml


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 通过统一入口类获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, code, expect):
        # 调用登录业务方法
        self.mp.page_mp_login(username, code)
        # 断言  让程序代替人工对程序执行的结果验证的过程
        # print("\n 获取的昵称为：", self.mp.page_get_nickname())
        # assert expect == self.mp.page_get_nickname()
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            print("错误原因：", e)
            self.mp.base_get_img()
            # 抛出异常
            raise
