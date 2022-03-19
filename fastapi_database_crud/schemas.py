# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction

from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    """
    请求模型验证：
    email:
    password:
    """
    password: str
    user_name: str
    full_name: Optional[str] = None


class User(UserBase):
    """
    响应模型：
    id:
    email:
    is_active
    并且设置orm_mode与之兼容
    """
    id: int
    disabled: bool

    class Config:
        orm_mode = True
