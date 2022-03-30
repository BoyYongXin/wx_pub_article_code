from walrus import Database, RateLimitException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

db = Database()
rate = db.rate_limit('xxx', limit=5, per=60)  # in 60s just can only click 5 times

app = FastAPI()


@app.exception_handler(RateLimitException)
def parse_rate_litmit_exception(request: Request, exc: RateLimitException):
    msg = {'success': False, 'msg': f'please have a tea for sleep, your ip is: {request.client.host}.'}
    return JSONResponse(status_code=429, content=msg)


@app.get('/')
@rate.rate_limited(lambda request: request.client.host)
def index(request: Request):
    return {'success': True}


@app.get('/important_api')
@rate.rate_limited(lambda request: request.client.host)
def query_important_data(request: Request):
    data = 'important data'
    return {'success': True, 'data': data}


if __name__ == "__main__":
    uvicorn.run("ceshi2:app", debug=True, reload=True)
