#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  reader.py
@ Time           :  2024/04/25 23:07:55
@ Author         :  Flower
@ Version        :  1.0
@ Description    :  读取数据
@ History        :  1.0(2024/04/25) - 读取数据(Flower)
"""
from typing import List


def read_file(file_path: str) -> List[str]:
    """读取文件

    Args:
        file_path (str): 文件路径

    Returns:
        List[str]: url列表
    """
    with open(file_path, "r", encoding="utf-8") as f:
        urls = f.read().splitlines()
    return urls
