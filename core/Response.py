# -*- coding:utf-8 -*-
"""
@Time : 2024/5/17 22:36 PM
@Author: xmabc
@Des: 常用返回类型封装
"""


def base_response(code, msg, data=None):
    """基础返回格式"""
    if data is None:
        data = []
    result = {
        "code": code,
        "message": msg,
        "data": data
    }
    return result


def success(data=None, msg=''):
    """成功返回格式"""
    return base_response(200, msg, data)


def fail(code=-1, msg='', data=None):
    """失败返回格式"""
    return base_response(code, msg, data)