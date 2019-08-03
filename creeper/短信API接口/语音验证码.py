#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 语音验证码.py
# Author: MuNian
# Date  : 2019/7/8
'''
接口地址: 请求聚合数据平台并且返回数据

'''
import requests, json

# 接口地址
url = 'http://op.juhe.cn/yuntongxun/voice'
# appkey值
appkey = 'aacd2ebd0928810309acda0c7da8736e'
valicode = input('请输入验证码:')
to = input('请输入接收人:')
# 接口参数
parmas = {
    'valicode':valicode,  # 验证码内容
    'to':to, # 接收人
    'playtimes':'',
    'key':appkey,
    'dtype':'' # 返回数据的格式,xml或json，默认json
}
# 带上参数来请求接口地址
sponse = requests.get(url, params=parmas).text
# 解析 json数据
res = json.loads(sponse)
if res:
    error_code = res['error_code']
    if error_code == 0:
        # 请求成功
        print(res['reason'])
    else:
        print(res['reason'])
else:
    print('请求接口失败')
