#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-08-02 10:07
# @Author  : YaoJa
from time import sleep

from selenium.webdriver.common.by import By

from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class WebBase(Base):
    """以下为你web项目专属方法"""
    def web_base_click_element(self, placeholder_text, click_text):
        # 1.点击复选框
        loc = By.CSS_SELECTOR, "[placeholder={}]".format(placeholder_text)
        self.base_click(loc)
        # 2.暂停
        sleep(2)
        # 3.点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)

    # 判断当天页面是否包含指定的元素
    def web_base_is_exist(self, text):
        # 1、组织元素配置信息
        log.info("正在调用查找页面是否存在指定元素方法".format(text))
        loc = By.XPATH, "//*[text()='{}']".format(text)
        # 2、找元素操作
        try:
            # 1、找元素， 修改查找元素总时间
            self.base_find(loc, timeout=3)
            # 2、输出找到信息
            print("找到:{}元素".format(loc))
            # 3、返回True
            return True
        except:
            # 1、输出未找到信息
            print("未找到：{}元素".format(loc))
            # 2、返回False
            return False
