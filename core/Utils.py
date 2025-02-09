# -*- coding:utf-8 -*-
"""
@Created on : 2022/4/22 22:02
@Author: Tang Xiaomi
@Des: 工具函数
"""

import hashlib
import uuid
from passlib.handlers.pbkdf2 import pbkdf2_sha256


def random_str():
    """
    唯一随机字符串
    :return: str
    """
    only = hashlib.md5(str(uuid.uuid1()).encode(encoding='UTF-8')).hexdigest()
    return str(only)


def en_password(psw: str):
    """
    密码加密
    :param psw: 需要加密的密码
    :return: 加密后的密码
    """
    password = pbkdf2_sha256.hash(psw)
    return password


def check_password(password: str, old: str):
    """
    密码校验
    :param password: 用户输入的密码
    :param old: 数据库密码
    :return: Boolean
    """
    check = pbkdf2_sha256.verify(password, old)
    if check:
        return True
    else:
        return False


def get_tree(data, pid):
    """
    遍历树
    :param data: rule[]
    :param pid: 父ID
    :return: list
    """
    result = []
    for item in data:
        if item["parent_id"] == pid:
            temp = get_tree(data, item["id"])
            if len(temp) > 0:
                item["children"] = temp
            result.append(item)
    return result