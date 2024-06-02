# -*- coding:utf-8 -*-
"""
@Created on : 2024/5/16 23:06
@Author: xmabc
@Des: api路由
"""
from fastapi import APIRouter
from application.endpoints import test, institution

api_router = APIRouter(prefix="/api/v1")
api_router.post("/test/oath2", tags=["测试oath2授权"], include_in_schema=False)(test.oath2)
api_router.include_router(institution.router, prefix='/institution', tags=["机构管理"])
