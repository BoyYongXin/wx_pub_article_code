# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction
# 路径操作装饰器依赖项
import uvicorn
from fastapi import FastAPI, Header, HTTPException, Depends

app = FastAPI()
fake_items_db = [{"city": "beijing"}, {"city": "shanghai"},
                 {"city": "heze"}]


def verify_token(token: str = Header(...)):
    if token != "zhidingtoken":
        raise HTTPException(status_code=400, detail="Token header invalid")


def verify_key(key: str = Header(...)):
    if key != "key":
        raise HTTPException(status_code=400, detail="Key header invalid")
    return key


@app.get("/items/", dependencies=[Depends(verify_token), Depends(verify_key)])
def read_items():
    return fake_items_db


if __name__ == '__main__':
    uvicorn.run(app="demo1:app", host="0.0.0.0", port=8000)
