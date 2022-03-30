# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction


import time
import uvicorn
from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.middleware("http")
async def log_request(request, call_next):
    print('请求开始前我可以处理事情1')
    start_time = time.time()
    response = await call_next(request)

    print('请求开始后我可以处理的事情3')
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
async def not_timed(response: Response):
    print('请求开始后我可以处理的事情2')
    return {"message": "你好"}


if __name__ == '__main__':
    uvicorn.run('eg2:app', host="127.0.0.1", port=8000, debug=True, reload=True)
