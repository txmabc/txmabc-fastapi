# -*- coding:utf-8 -*-
"""
@Time : 2022/4/24 10:15 AM
@Author: Tang Xiaomi
@Des: mysql数据库
"""

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import os


# -----------------------数据库配置-----------------------------------
DB_ORM_CONFIG = {
    "connections": {
        "base": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('BASE_HOST', '127.0.0.1'),
                'user': os.getenv('BASE_USER', 'root'),
                'password': os.getenv('BASE_PASSWORD', '123456'),
                'port': int(os.getenv('BASE_PORT', 3306)),
                'database': os.getenv('BASE_DB', 'xmabc_base'),
            }
        },
        "demo": {
            'engine': 'tortoise.backends.mysql',
            "credentials": {
                'host': os.getenv('DB2_HOST', '127.0.0.1'),
                'user': os.getenv('DB2_USER', 'root'),
                'password': os.getenv('DB2_PASSWORD', '123456'),
                'port': int(os.getenv('DB2_PORT', 3306)),
                'database': os.getenv('DB2_DB', 'xmabc_demo'),
            }
        },

    },
    "apps": {
        "base": {"models": ["models.base"], "default_connection": "base"},
        "demo": {"models": ["models.demo"], "default_connection": "demo"},
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app: FastAPI):
    # 注册数据库
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=True,
        add_exception_handlers=True,
    )
