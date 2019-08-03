#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/5

from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '16723507'
API_KEY = 'y1GGsX6t09SHCfn3gP5I0T2U'
SECRET_KEY = 'M9c4QeyrfrErwO95GeyrcyBSmoeIPC6m'

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text = "百度是一家高科技公司"

""" 调用词法分析 """
Nice = client.sentimentClassify(text)
print(Nice)