#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 19:41
# @Author  : YaoJa
"""页面对象目录"""
from time import sleep

from base.base import Base
import page
from base.web_base import WebBase


class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self, username):
        # 调用父类中输入方法
        self.base_input(page.mp_username, username)

    # 输入验证码
    def page_input_code(self, code):
        # 调用父类中输入方法
        self.base_input(page.mp_code, code)

    # 点击登录按钮
    def page_click_login_btn(self):
        # 调用父类中点击方法
        self.base_click(page.mp_login_btn)

    # 获取昵称封装  -->测试脚本层断言调用
    def page_get_nickname(self):
        # 调用父类中 获取文本方法
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法 -->测试脚本层调用
    def page_mp_login(self, username, code):
        """提示：调用相同页面操作步骤，跨页面暂时不考虑"""
        self.page_input_username(username)
        sleep(1)
        self.page_input_code(code)
        sleep(1)
        self.page_click_login_btn()
        sleep(3)

    # 组合业务方法 -->发布文章依赖使用
    def page_mp_login_success(self, username="13812345678", code="246810"):
        self.page_input_username(username)
        sleep(1)
        self.page_input_code(code)
        sleep(1)
        self.page_click_login_btn()
        sleep(2)
