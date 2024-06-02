# -*- coding:utf-8 -*-
"""
@Time : 2024/5/16 23:03 AM
@Author: xmabc
@Des: oath2授权
"""
from core.Auth import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from models.base import Admin
from core.Utils import check_password


async def oath2(data: OAuth2PasswordRequestForm = Depends()):
    admin = await Admin.get_or_none(adminname=data.username)
    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not admin.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not check_password(data.password, admin.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not admin.admin_status:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}已被管理员禁用!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"admin_id": admin.id, "admin_type": admin.admin_type})

    return {"access_token": access_token, "token_type": "bearer"}
