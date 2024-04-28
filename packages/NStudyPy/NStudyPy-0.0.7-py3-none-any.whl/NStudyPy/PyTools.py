#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024-04-24 18:34
# @Author  : Jack
# @File    : tools

"""
tools
"""

from os import environ


def get_env(key: str, default=None, value_type=None):
    """
        Returns the value from the key.
        check environment variables
    """
    value = default

    if key in environ:
        value = environ.get(key)

    if (value_type is None) or (default is None):
        return value

    if value_type == bool:
        return value == "True"

    return value_type(value)
