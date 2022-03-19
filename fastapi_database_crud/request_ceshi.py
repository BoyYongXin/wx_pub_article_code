# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction

import requests
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
url = "http://localhost:8000/users/"
data = {
    "user_name": "monday",
    "email": "14268333@qq.com",
    "password": "123456",
    "full_name": "菜鸟童靴"
}
response = requests.post(url, headers=headers, json=data)
print(response.text)
print(response)

import requests


headers = {
    "accept": "application/json"
}
url = "http://localhost:8000/user/1"
response = requests.get(url, headers=headers)

print(response.text)
print(response)