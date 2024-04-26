#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  dcore.py
@ Time           :  2024/04/24 13:18:20
@ Author         :  Flower
@ Version        :  1.0
@ Description    :  None
@ History        :  1.0(2024/04/24) - None(Flower)
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from cabbage.model.data import Data


def get_douyin_data(driver: webdriver.Chrome, url: str) -> Data:
    """获取抖音的数据

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
        value="#douyin-right-container > div:nth-child(2) > div > div.leftContainer.gkVJg5wr > div.XYnWH9QO > div > div.YuF0Acwt > div.xi78nG8b > div:nth-child(1) > span",
    )
    fav_info = driver.find_element(
        By.CSS_SELECTOR,
        value="#douyin-right-container > div:nth-child(2) > div > div.leftContainer.gkVJg5wr > div.XYnWH9QO > div > div.YuF0Acwt > div.xi78nG8b > div:nth-child(3) > span",
    )
    comm_info = driver.find_element(
        By.CSS_SELECTOR,
        value="#douyin-right-container > div:nth-child(2) > div > div.leftContainer.gkVJg5wr > div.XYnWH9QO > div > div.YuF0Acwt > div.xi78nG8b > div:nth-child(2) > span",
    )

    print("点赞数: ", like_info.text)
    print("收藏数: ", fav_info.text)
    print("评论数: ", comm_info.text)
    data = Data()
    data.set_url(url)
    data.set_result(like_info.text, fav_info.text, comm_info.text)
    return data
