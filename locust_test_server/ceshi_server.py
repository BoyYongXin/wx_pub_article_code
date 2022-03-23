# !/usr/bin/env python
# -*-coding=utf-8 -*-
# @Author: Mr.Yang
# @Date: 
# @email: 
# @Pagefunction


from locust import HttpUser, task, between
import os


class PressureStart(HttpUser):
    min_wait = 100  # 最小等待时间(ms)，模拟用户在执行每个任务之间等待的最小时间
    max_wait = 500  # 最大等待时长(ms)，模拟用户在执行每个任务之间等待的最大时长
    wait_time = between(min_wait, max_wait)
    host = "http://localhost:8000"  # 访问的域名和端口

    # def on_start(self):
    #     # login_result = self.client.post("/login", json={"username": "Tom", "password": "123456"}).text
    #     print(" working start ............")
    #
    # def on_stop(self):
    #     logout_result = self.client.post("/logout", json={"username": "Jim", "password": "456789"}).text
    #     print(" working stop ............")

    @task(1)
    def region_get(self):
        header = {"Content-Type": "application/json"}
        self.client.get('/user/1', headers=header)

    # @task(2)
    # def region_get2(self):
    #     header = {"Content-Type": "application/json"}
    #     self.client.get('/user/1', headers=header)


if __name__ == '__main__':
    os.system(
        "locust -f ceshi_server.py --host=http://localhost:8000 --no-web -c 20 -r 20 -t 100s --csv=example --loglevel=INFO --logfile=test.log ")
