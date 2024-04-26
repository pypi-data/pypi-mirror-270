#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  __init__.py
@ Time           :  2024/04/26 01:14:03
@ Author         :  Flower
@ Version        :  1.0
@ Description    :  None
@ History        :  1.0(2024/04/26) - None(Flower)
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .core.bcore import get_bilibili_data
from .core.dcore import get_douyin_data
from .io.reader import read_file
from .io.saver import save_data


class Cabbage:
    def __init__(self):
        self.douyin_data_path: str = ""
        self.bilibili_data_path: str = ""
        self.target_dir: str = ""
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9299")
        self.driver = webdriver.Chrome(options=chrome_options)

    def get_douyin_path(self, path: str) -> None:
        self.douyin_data_path = path
        # 判断路径是否存在，不存在则提示
        if not os.path.exists(self.douyin_data_path):
            print("路径不存在，请检查路径是否正确！")

    def get_bilibili_path(self, path: str) -> None:
        self.bilibili_data_path = path
        # 判断路径是否存在，不存在则提示
        if not os.path.exists(self.bilibili_data_path):
            print("路径不存在，请检查路径是否正确！")

    def set_target_dir(self, path: str) -> None:
        self.target_dir = path
        # 判断路径是否存在，不存在则创建文件夹
        if not os.path.exists(self.target_dir):
            # 提示
            os.makedirs(self.target_dir)
            print("文件夹不存在，创建！")

    def get_douyin_data(self) -> None:
        url_list = read_file(self.douyin_data_path)
        data_list = []
        for idx, url in enumerate(url_list):
            print(f"当前进度: {idx+1}/{len(url_list)}")
            print(url)
            if url:
                data = get_douyin_data(self.driver, url)
                data_list.append(data)

        # 保存成带时间的文件，时间格式例如2024-04-26-01-14-03
        result_path = os.path.join(
            self.target_dir,
            f"douyin-{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.txt",
        )
        save_data(data_list, result_path)
        self.driver.get(url="https://www.baidu.com")

    def get_bilibili_data(self) -> None:
        url_list = read_file(self.bilibili_data_path)
        data_list = []
        for idx, url in enumerate(url_list):
            print(f"当前进度: {idx+1}/{len(url_list)}")
            print(url)
            if url:
                data = get_bilibili_data(self.driver, url)
                data_list.append(data)

        # 保存成带时间的文件，时间格式例如2024-04-26-01-14-03
        result_path = os.path.join(
            self.target_dir,
            f"bilibili-{time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())}.txt",
        )
        save_data(data_list, result_path)
        self.driver.get(url="https://www.baidu.com")
