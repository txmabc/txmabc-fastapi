# -*- coding:utf-8 -*-
"""
@Time : 2024/5/17 22:36 PM
@Author: xmabc
@Des: 常用返回类型封装
"""
import time

def base_response(code, data=None):
    """基础返回格式"""
    if data is None:
        data = []
    result = {
        "code": code,
        "data": data,
        "time": int(time.time())
    }
    return result


def success(data=None):
    """成功返回格式"""
    return base_response(0, data)


def fail(code=-1, data=None):
    """失败返回格式"""
    return base_response(code, data)