#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-02 10:17
# @Author  : YaoJa
from time import sleep

import page
from base.web_base import WebBase


class PageMpArticle(WebBase):
    # 点击 内容管理
    def page_click_content_manage(self):
        self.base_click(page.mp_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        self.base_click(page.mp_publish_article)

    # 输入 标题
    def page_input_title(self, title):
        self.base_input(page.mp_title, title)

    # 输入 内容
    def page_input_content(self, content):
        # 1. 切换iframe
        iframe = self.base_find(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        sleep(2)
        # 2. 输入内容
        self.base_input(page.mp_content, content)
        # 3. 回到默认目录
        sleep(2)
        self.driver.switch_to.default_content()

    # 选择 封面
    def page_click_cover(self):
        self.base_click(page.mp_cover)

    # 选择 频道
    def page_click_channel(self):
        # 调用WebBase封装方法
        self.web_base_click_element(placeholder_text="请选择", click_text=page.channel)

    # 点击 发表按钮
    def page_click_submit(self):
        self.base_click(page.mp_submit)

    # 获取 发表提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合发布文章业务方法
    def page_mp_article(self, title, content):
        self.page_click_content_manage()
        sleep(2)
        self.page_click_publish_article()
        sleep(2)
        self.page_input_title(title)
        sleep(2)
        self.page_input_content(content)
        sleep(2)
        self.page_click_cover()
        sleep(2)
        self.page_click_channel()
        sleep(2)
        self.page_click_submit()

