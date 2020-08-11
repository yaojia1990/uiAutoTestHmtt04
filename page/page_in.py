#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 19:42
# @Author  : YaoJa
"""统一入口类"""
# from page.page_app_login import PageAppLogin
from page.page_mis_audit import PageMisAudit
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin
from page.page_mis_login import PageMisLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageMisLogin对象
    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)

    # 获取PageMisAudit对象
    def page_get_PageMisAudit(self):
        return PageMisAudit(self.driver)

