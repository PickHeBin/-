#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 备课_day1.py
# Author: MuNian
# Date  : 2019/7/5

import requests, json
from urllib import parse


def main():
    # 申请的短信服务appkey
    appkey = '799aaf477f15693a7cd49359556fede8'
    # 短信接受者的手机号码
    mobile = '13764689856'
    # 申请的短信模板ID,根据实际情况修改
    tpl_id = '170620'
    # 短信模板变量,根据实际情况修改
    tpl_value = '#code#=14SB'

    sendsms(appkey, mobile, tpl_id, tpl_value)  # 请求发送短信


def sendsms(appkey, mobile, tpl_id, tpl_value):
    sendurl = 'http://v.juhe.cn/sms/send'  # 短信发送的URL,无需修改

    # 组合参数
    params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % (appkey, mobile, tpl_id, parse.quote(tpl_value))

    wp = requests.get(sendurl, params=params)
    content = wp.text  # 获取接口返回内容

    result = json.loads(content)

    if result:
        error_code = result['error_code']
        if error_code == 0:
            # 发送成功
            smsid = result['result']['sid']
            print("sendsms success,smsid: %s" % (smsid))
        else:
            # 发送失败
            print("sendsms error :(%s) %s" % (error_code, result['reason']))
    else:
        # 请求失败
        print("request sendsms error")


if __name__ == '__main__':
    main()