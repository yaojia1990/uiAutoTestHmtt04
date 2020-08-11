#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-21 20:46
# @Author  : YaoJa
"""工具类存储目录"""
from time import sleep

from selenium import webdriver
import appium.webdriver

import page


class GetDriver:
    # 声明变量
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断driver是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()

            # 置空操作  重点 执行完quit后driver对象清空了但driver在内存中的地址没有清空，上面的判断为空一直不为空，只有第一次获取能成功
            cls.__web_driver = None

    # 获取app driver方法
    @classmethod
    def get_app_driver(cls):
        # 判断__app_driver 为空
        if cls.__app_driver is None:
            # 驱动手机的配置文件
            desired_caps = {}
            # 手机类型、Android或者ios
            desired_caps['platformName'] = 'Android'
            # 手机版本，手机中查看，设置
            desired_caps['platformVersion'] = '5.1'
            # 手机设备名称，adb devices, 自定义
            desired_caps['deviceName'] = 'GYYS6HUW99999999'
            # APP信息 adb shell dumpsys window | findstr mCurrentFocus 命令行获取package/activity
            # app包名，每一个Android APP都有包名
            desired_caps['appPackage'] = page.appPackage
            # 启动入口
            desired_caps['appActivity'] = page.appActivity
            # 设置driver
            cls.__app_driver = appium.webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    # 退出app driver方法
    @classmethod
    def quit_app_driver(cls):
        # 判断driver不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()

            # 置空操作  重点 执行完quit后driver对象清空了但driver在内存中的地址没有清空，上面的判断为空一直不为空，只有第一次获取能成功
            cls.__app_driver = None


if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(2)
    GetDriver.quit_app_driver()
