#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 01 执行登陆获取token
import jsonpath
import requests

# 01 执行登陆获取token
data = {
    "accounts": "zz888",
    "pwd": "123456",
    "type": "username"
}

params = {
    "application": "app",
    "application_client_type": "weixin",
}
r1 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/user/login", params=params, json=data)
token_list = jsonpath.jsonpath(r1.json(),'$..token')
token = token_list[0]
print(token)

# 测试接口
params = {
    "application": "app",
    "application_client_type": "weixin",
    "token": token
}
r1 = requests.post(url="http://shop-xo.hctestedu.com/index.php?s=api/order/index", params=params)
print(r1.text)