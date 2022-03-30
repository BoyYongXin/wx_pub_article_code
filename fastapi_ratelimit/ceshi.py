# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction
import uvicorn
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from fastapi import Request, Response
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from fastapi.responses import PlainTextResponse

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/home")
@limiter.limit("5/minute")
async def homepage(request: Request):
    # return JSONResponse({"code":1})
    return PlainTextResponse("访问成功")


if __name__ == '__main__':
    uvicorn.run(app="ceshi:app", host="0.0.0.0", port=8000)
