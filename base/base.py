#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 19:00
# @Author  : YaoJa
"""所以page页面基类，page页面公共方法目录"""
from selenium.webdriver.support.wait import WebDriverWait
import allure

from tools.get_log import GetLog

log = GetLog.get_logger()

class Base:
    # 初始化
    def __init__(self, driver):
        """解决driver"""
        log.info("正在初始化driver: {}".format(driver))
        self.driver = driver

    # 查找 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        """

        :param loc: 格式为列表或元组，内容：元素定位信息使用By类
        :param timeout: 查找元素超时时间，默认为30秒
        :param poll: 查找元素频率，默认为0.5
        :return: 返回元素
        """
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入 方法封装
    def base_input(self, loc, value):
        """

        :param loc: 元素的定位信息
        :param value: 要输入的值
        """
        # 获取元素
        el = self.base_find(loc)
        # 清空操作
        log.info("正在对：{} 元素执行清空操作！".format(loc))
        el.clear()
        # 输入操作
        log.info("正在对：{} 元素执行输入:{} 操作！".format(loc, value))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """

        :param loc: 元素定位信息
        """
        # 获取元素并点击
        log.info("正在对：{} 元素执行点击操作！".format(loc))
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        """

        :param loc: 元素定位信息
        :return: 返回元素文本值
        """
        log.info("正在对：{} 元素获取文本操作！，获取的文本值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error("断言出错，正在执行截图操作！")
        # self.driver.get_screenshot_as_file("./image/err.png")
        self.driver.get_screenshot_as_file("./image/err.png")
        # 调用 将图片写入报告方法
        log.error("断言出错，正在将错误图片写入allure报告！")
        self.__base_write_image()

    # 图片写入allure报告方法(私有化)
    def __base_write_image(self):
        # 获取图片流
        with open("./image/err.png", "rb") as f:
            # 调用 allure.attach方法将图片写入报告
            allure.attach("失败原因：", f.read(), allure.attachment_type.PNG)
