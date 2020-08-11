#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-02 19:26
# @Author  : YaoJa
from time import sleep

import page
from base.web_base import WebBase


class PageMisLogin(WebBase):
    # 1、输入用户名
    def page_input_username(self, username):
        self.base_input(page.mis_username, username)

    # 2、输入密码
    def page_input_pwd(self, password):
        self.base_input(page.mis_pwd, password)

    # 3、点击登录
    def page_click_login_btn(self):
        # 1、先处理js
        js = "document.getElementById('inp1').disabled = false"
        self.driver.execute_script(js)
        # 2、调用点击操作
        self.base_click(page.mis_login_btn)

    # 4、获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # 5、组合后台登录管理系统业务
    def page_mis_login(self, username, password):
        self.page_input_username(username)
        sleep(2)
        self.page_input_pwd(password)
        sleep(2)
        self.page_click_login_btn()
        sleep(2)

    # 5、组合后台登录管理系统业务--->成功登陆
    def page_mis_login_success(self, username="testid", password="testpwd123"):
        self.page_input_username(username)
        sleep(2)
        self.page_input_pwd(password)
        sleep(2)
        self.page_click_login_btn()
        sleep(2)
