#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-03 19:23
# @Author  : YaoJa
from time import sleep

import page
from base.web_base import WebBase
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMisAudit(WebBase):
    article_id = None
    # 1、点击信息管理
    def page_click_info_manage(self):
        self.base_click(page.mis_info_manage)

    # 2、点击内容审核
    def page_click_content_audit(self):
        self.base_click(page.mis_content_audit)

    # 3、输入文章名称
    def page_input_article(self, article):
        self.base_input(page.mis_article, article)

    # 4、输入频道
    def page_input_channel(self, channel):
        self.base_input(page.mis_channel, channel)

    # 5、选择状态
    def page_click_status(self, placeholder_text="请选择状态", click_text="待审核"):
        self.web_base_click_element(placeholder_text, click_text)

    # 6、点击查询按钮
    def page_click_find(self):
        self.base_click(page.mis_find)

    # 7、获取文章id
    def page_get_article_id(self):
        print(self.base_get_text(page.mis_article_id))
        return self.base_get_text(page.mis_article_id)

    # 8、点击通过
    def page_click_pass_btn(self):
        self.base_click(page.mis_pass)

    # 9、点击确认
    def page_click_confirm_pass(self):
        self.base_click(page.mis_confirm_pass)

    # 10、组合发布文章审核业务方法
    def page_mis_audit(self, title, channel):
        log.info("正在调用组合发布文章审核业务方法，title:{} channel:{}".format(title, channel))
        self.page_click_info_manage()
        sleep(2)
        self.page_click_content_audit()
        sleep(2)
        self.page_input_article(title)
        sleep(2)
        self.page_input_channel(channel)
        sleep(2)
        self.page_click_status()
        sleep(2)
        self.page_click_find()
        sleep(2)
        self.article_id = self.page_get_article_id()
        print(self.article_id)
        # print(self.article_id())
        print(type(self.article_id))
        print("文章的ID为：", self.article_id)
        sleep(2)
        self.page_click_pass_btn()
        sleep(1)
        self.page_click_confirm_pass()

    # 11、组织断言业务操作方法
    def page_assert_audit(self):
        log.info("正在调用组织断言业务操作方法")
        # 1、暂停3秒
        sleep(3)
        # 2、修改状态-->审核通过
        self.page_click_status(click_text="审核通过")
        # 3、点击查询按钮
        self.page_click_find()
        # 4、判断当前页面是否存在指定元素 并返回结果
        return self.web_base_is_exist(self.article_id)
