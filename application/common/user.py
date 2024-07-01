# -*- coding:utf-8 -*-
"""
@Time : 2024/5/16 23:03 AM
@Author: xmabc
@Des: oath2授权
"""

from fastapi import Depends, HTTPException, status
from models.base import User, Access
from core.Response import success, fail
from fastapi import Request, Query, APIRouter, Security
from core.Auth import check_permissions
from schemas import UserSchema

router = APIRouter()

@router.post("/add", summary="添加用户", dependencies=[Security(check_permissions, scopes=["user_add"])])
async def user_add(post: UserSchema.CreateUser):
    return success("创建成功")



@router.get("/list")
async def user_list():
    is_pass = await Access.filter(
                role__user__id=2, is_check=True, scopes__in=set(["user_add"])).all()
    return is_pass