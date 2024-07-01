# -*- coding:utf-8 -*-
"""
@Time : 2024/5/16 23:03 AM
@Author: xmabc
@Des: oath2授权
"""
import time
from typing import Annotated
from typing_extensions import Doc
from core.Auth import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import Depends, Form, HTTPException, status
from models.base import User
from core.Utils import check_password
from schemas.BaseSchema import LoginReq, SuccessRes
from config import settings
from core.Response import success, fail

async def authorize(username: Annotated[
            str,
            Form(),
            Doc(
                """
                `username` string. The OAuth2 spec requires the exact field name
                `username`.
                """
            ),
        ],
        password: Annotated[
            str,
            Form(),
            Doc(
                """
                `password` string. The OAuth2 spec requires the exact field name
                `password".
                """
            ),
        ]):
    user = await User.get_or_none(username=data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not check_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.status:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}已被管理员禁用!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user.id, "user_type": user.user_type})
    data={"access_token": access_token, "token_type": "bearer", "expires_in": settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES}
    return SuccessRes(data)


async def token(data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(username=data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not check_password(data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}密码验证失败!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.status:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"用户{data.username}已被管理员禁用!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"user_id": user.id, "user_type": user.user_type})
    return {"access_token": access_token, "token_type": "bearer"}