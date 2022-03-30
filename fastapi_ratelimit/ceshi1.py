# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction

import time
from ratelimiter import RateLimiter

def limited(until):
    duration = int(round(until - time.time()))
    print('Rate limited, sleeping for {:d} seconds'.format(duration))
# 3秒之内只能访问2次
rate_limiter = RateLimiter(max_calls=2, period=3, callback=limited)

for i in range(3):
    with rate_limiter:
        print('Iteration', i)