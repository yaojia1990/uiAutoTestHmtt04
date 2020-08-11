#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-07-25 14:35
# @Author  : YaoJa
# 定义函数
import os
import yaml
from config import BASE_PATH


def read_yaml(filename):
    file_path = BASE_PATH + os.altsep + "data" + os.altsep + filename
    # 定义空列表 组装测试数据
    arrs = []
    # 获取文件流
    with open(file_path, "r", encoding="utf-8") as f:

        # 遍历 调用yaml.safe_load(f).values()方法
        for datas in yaml.safe_load(f).values():
            # tuple 列表嵌套元组  list 列表嵌套列表
            arrs.append(tuple(datas.values()))
            # arrs.append(list(datas.values()))
        # 返回结果
        return arrs


if __name__ == "__main__":
    print(read_yaml("mp_article.yaml"))
