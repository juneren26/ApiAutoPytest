#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from VAR.VAR import *
from api_keyword.api_key import ApiKey

#项目级fix，整个项目只初始化一次
@pytest.fixture(scope='session')
def token_fix():
    # 初始化工具类
    ak = ApiKey()
    data = {
        "accounts": USERNAME,
        "pwd": PASSWD,
        "type": "username"
    }

    # params = {
    #     "application": "app",
    #     "application_client_type": "weixin",
    # }
    # url = "http://shop-xo.hctestedu.com/index.php?s=api/user/login"
    url = PROJECT_URL + "api/user/login"
    r1 = ak.post(url=url, params=PARAMS, json=data)
    # 获取token
    token = ak.get_text(r1.text,'$..token')
    return ak,token