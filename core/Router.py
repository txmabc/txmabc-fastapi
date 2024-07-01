# -*- coding:utf-8 -*-
"""
@Time : 2024/5/46 22:51 PM
@Author: xmabc.net
@Des: 路由聚合
"""
from application.router import common_router
from fastapi import APIRouter

router = APIRouter()
# API路由
router.include_router(common_router)