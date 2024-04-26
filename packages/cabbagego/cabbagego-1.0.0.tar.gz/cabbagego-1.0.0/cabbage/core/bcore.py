#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  bcore.py
@ Time           :  2024/04/24 13:18:16
@ Author         :  Flower
@ Version        :  1.0
@ Description    :  None
@ History        :  1.0(2024/04/24) - None(Flower)
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from cabbage.model.data import Data


def get_bilibili_data(driver: webdriver.Chrome, url: str) -> Data:
    """获取b站的数据

    Args:
        driver (webdriver.chrome.webdriver.WebDriver): 驱动
        url (str): url

    Returns:
        Data: 数据
    """
    driver.get(url)
    time.sleep(5)
    like_info = driver.find_element(
        By.CSS_SELECTOR,
        value="#arc_toolbar_report > div.video-toolbar-left > div.video-toolbar-left-main > div:nth-child(1) > div > span",
    )
    fav_info = driver.find_element(
        By.CSS_SELECTOR,
        value="#arc_toolbar_report > div.video-toolbar-left > div.video-toolbar-left-main > div:nth-child(3) > div > span",
    )
    comm_info = driver.find_element(
        By.CSS_SELECTOR,
        value="#comment > div > div > div > div.reply-header > div.reply-navigation > ul > li.nav-title > span.total-reply",
    )

    print("点赞数: ", like_info.text)
    print("收藏数: ", fav_info.text)
    print("评论数: ", comm_info.text)
    data = Data()
    data.set_url(url)
    data.set_result(like_info.text, fav_info.text, comm_info.text)
    return data
