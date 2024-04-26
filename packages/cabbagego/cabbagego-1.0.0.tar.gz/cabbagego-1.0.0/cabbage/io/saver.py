#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  saver.py
@ Time           :  2024/04/25 23:08:01
@ Author         :  Flower
@ Version        :  1.0
@ Description    :  写入数据
@ History        :  1.0(2024/04/25) - 写入数据(Flower)
"""
from typing import List

from cabbage.model.data import Data


def save_data(raw_data: List[Data], file_path: str) -> None:
    """保存数据

    Args:
        raw_data (List[Data]): 原始数据
        file_path (str): 文件路径
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"url,点赞数,收藏数,评论数\n")
        for data in raw_data:
            f.write(f"{data.url},{data.like_num},{data.fav_num},{data.comm_num}\n")
