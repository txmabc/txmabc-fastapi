# -*- coding:utf-8 -*-
"""
@Created on : 2024/5/16 23:06
@Author: xmabc
@Des: api路由
"""
from fastapi import APIRouter
from application.common.oauth2 import authorize, token
from application.common import user
from schemas.BaseSchema import SuccessRes
# 公共api
common_router = APIRouter(prefix="/api/common")
common_router.post("/oath2/token", summary="获取token", tags=["token"], include_in_schema=False)(token)
common_router.post("/oath2/authorize", summary="获取授权", tags=["授权"], include_in_schema=True)(authorize)
common_router.include_router(user.router, prefix='/user', tags=["用户"])
