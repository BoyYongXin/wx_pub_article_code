# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction

from sqlalchemy import Boolean, Column, Integer, String, DateTime
from database import Base
import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, comment='自增id')
    user_name = Column(String(32), unique=True, index=True, comment='用户名')
    full_name = Column(String(32), unique=False, index=False, default=None, comment='全称')
    email = Column(String(32), unique=True, index=True, comment='邮箱地址')
    hashed_password = Column(String(64), comment='加密密码')
    disabled = Column(Boolean, default=True, comment='用户状态')
    createtime = Column(DateTime, default=datetime.datetime.now, comment='创建时间')
    updatetime = Column(DateTime, default=datetime.datetime.now, comment='修改时间')
