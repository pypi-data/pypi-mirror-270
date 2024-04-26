#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@ File Name      :  data.py
@ Time           :  2024/04/25 23:44:52
@ Author         :  Flower
@ Version        :  1.0
@ Description    :  None
@ History        :  1.0(2024/04/25) - None(Flower)
"""


class Data:
    def __init__(self):
        self.url: str = ""
        self.like_num: str = ""
        self.fav_num: str = ""
        self.comm_num: str = ""

    def set_url(self, url: str):
        """导入url

        Args:
            url (str): url
        """
        self.url = url

    def set_result(self, like_num: str, fav_num: str, comm_num: str):
        """导入结果

        Args:
            like_num (str): 点赞数
            fav_num (str): 收藏数
            comm_num (str): 评论数
        """
        self.like_num = like_num
        self.fav_num = fav_num
        self.comm_num = comm_num
