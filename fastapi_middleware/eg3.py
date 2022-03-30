# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction
import uvicorn
import time
from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


@app.middleware("http")
async def log_request(request, call_next):
    print('请求开始前我可以处理事情1')
    response = await call_next(request)

    print('请求开始后我可以处理的事情3')

    return response


# 基于BaseHTTPMiddleware的中间件实例，
class CostimeHeaderMiddleware(BaseHTTPMiddleware):

    # dispatch 必须实现
    async def dispatch(self, request, call_next):
        print('请求开始前我可以处理事情4---CostimeHeaderMiddleware')
        start_time = time.time()
        responser = await call_next(request)
        process_time = round(time.time() - start_time, 4)
        # 返回接口响应时间
        responser.headers["X-Process-Time"] = f"{process_time} (s)"
        print('请求开始后我可以处理事情5----CostimeHeaderMiddleware')
        return responser


# 基于BaseHTTPMiddleware的中间件实例，
class CostimeHeaderMiddleware2(BaseHTTPMiddleware):

    # dispatch 必须实现
    async def dispatch(self, request, call_next):
        print('请求开始前我可以处理事情6-----CostimeHeaderMiddleware2')
        start_time = time.time()
        responser = await call_next(request)
        process_time = round(time.time() - start_time, 4)
        # 返回接口响应时间
        responser.headers["X-Process-Time"] = f"{process_time} (s)"
        print('请求开始后我可以处理事情7---CostimeHeaderMiddleware2')
        return responser


app.add_middleware(CostimeHeaderMiddleware)
app.add_middleware(CostimeHeaderMiddleware2)


@app.get("/")
async def not_timed():
    print('请求开始后我可以处理的事情2')
    return {"message": "你好"}


if __name__ == '__main__':
    uvicorn.run('eg3:app', host="127.0.0.1", port=8000, debug=True, reload=True)
