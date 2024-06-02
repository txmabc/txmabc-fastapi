# -*- coding:utf-8 -*-
"""
@Time : 2024/5/16 23:03 AM
@Author: xmabc
@Des: oath2授权
"""

from fastapi import Depends, HTTPException, status
from models.base import Institution
from core.Response import success, fail
from fastapi import Request, Query, APIRouter, Security
from core.Auth import check_permissions
from schemas import InstitutionSchema

router = APIRouter(prefix='/institution')


@router.post("", summary="机构添加", dependencies=[Security(check_permissions, scopes=["institution_add"])])
async def institution_add(post: InstitutionSchema.CreateInstitution):
    return success("创建成功")



