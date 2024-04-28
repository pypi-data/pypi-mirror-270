#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-04-28 14:13
# @Author  : Jack
# @File    : PyFile

"""
PyFile
"""
import os


def check_file_ext(filename: str, allowed_extensions=['png', 'jpg', 'jpeg']) -> bool:
    """
    检查文件扩展名是否符合要求
    :param filename:
    :param allowed_extensions:
    :return:
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def makedirs(path: str, is_file: bool = True):
    """
    创建目录
    :param is_file: 是否是文件
    :param path:
    :return:
    """
    if is_file:
        path = os.path.dirname(path)
    os.makedirs(path, exist_ok=True)
