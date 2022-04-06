# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction
from passlib.context import CryptContext  # passlib 处理哈希加密的包

password = '123456'
# Context是上下文,CryptContext是密码上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
res = pwd_context.hash(password)  # 对密码进行加密
print(res)
