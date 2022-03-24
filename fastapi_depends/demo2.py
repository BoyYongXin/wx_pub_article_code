# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction 全局依赖项

import uvicorn
from fastapi import FastAPI, Header, HTTPException, Depends

fake_items_db = [{"city": "beijing"}, {"city": "shanghai"},
                 {"city": "heze"}]

fake_items_db2 = {
    "city1": "beijing",
    "city2": "shanghai",
    "city3": "heze"
}


def verify_token(token: str = Header(...)):
    if token != "zhidingtoken":
        raise HTTPException(status_code=400, detail="Token header invalid")


def verify_key(key: str = Header(...)):
    if key != "key":
        raise HTTPException(status_code=400, detail="Key header invalid")
    return key


app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
def read_items():
    return fake_items_db


@app.get("/items/{city}")
def read_items(city: str):
    return fake_items_db2[city]


if __name__ == '__main__':
    uvicorn.run(app="demo2:app", host="0.0.0.0", port=8000)
