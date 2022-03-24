# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction


import uvicorn
from fastapi import FastAPI, Header, HTTPException, Depends
from typing import Optional
from pydantic import BaseModel


class UserReturn(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = False


def verify_token(token: str = Header(...)):
    if token != "token":
        raise HTTPException(status_code=400, detail="Token header invalid")
    return UserReturn(**{"id": 1, "username": "菜鸟童靴", "full_name": "Monday最帅"})


app = FastAPI()


@app.get("/items/", )
def read_items(user_info: UserReturn = Depends(verify_token)):
    return user_info


if __name__ == '__main__':
    uvicorn.run(app="demo3:app", host="0.0.0.0", port=8000)
