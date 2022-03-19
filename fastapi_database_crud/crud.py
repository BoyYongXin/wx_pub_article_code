# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction


from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext  # passlib 处理哈希加密的包

'''
为了数据安全，我们利用PassLib对入库的用户密码进行加密处理，推荐的加密算法是"Bcrypt"
其中，我们主要使用下面方法：
pwd_context.hash(password) # 对密码进行加密
pwd_context.verify(plain_password, hashed_password) 对密码进行校验
'''
# Context是上下文,CryptContext是密码上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 通过id查询用户
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# 新建用户
def db_create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password,
                          user_name=user.user_name, full_name=user.full_name)
    db.add(db_user)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_user)  # 刷新
    return db_user
