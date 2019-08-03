#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 刷访问.py
# Author: MuNian
# Date  : 2019/7/5

'''
企业当中:
    1. 注册  找回密码  绑定  支付

Python Web开发:搭建天猫商城 ----  市场平均15K薪资
逆向 - 黑客 红客
08年  黑客挑战 -- 14黑客
爬虫: 数据采集  解析 渗透  破解  模拟(外挂 刷会员 )
    安全网络 - 30K

自动化    市场上就业趋势最好的
4.5个月快速就业   web项目实战  + 爬虫实战 + 自动化实战
1 3 5 正课  2 4 6 解答    晚上20:30 -22:30
线上直播 + 课后录播 + 随堂笔记
符合企业技能 竞争力  高薪就业    多年架构的老师授课    8k - 27K

数据分析方向 --> 单独学习数据分析的课程:5080 的数据分析的课程   名额限制 成本

7880 - 500预订一个名额 - 1000优惠 = 6880(报一期送一期 + 5080数据分析班级(1个月) + 全栈班级(4.5)) / 分期 6 9 12  借呗 花呗 信用卡 京东白条 =

从事方向:
        web后端开发
        爬虫
        自动化
        数据分析

1. 掌握市场主流的web 爬虫 自动化 数据分析 框架
2. 掌握市场工作流程 开发架构
3. 根据公司的需求开发对应的数据库
4. .....


学会才毕业的  毕业后 独立开发一个天猫商城项目   分布式爬虫  搜索引擎   数据库.... 脚本
2个名额 .... 新班开班  预科班

学不会  就业问题
完善的VIP服务:
    1. 课后辅导 一对一解答  课后补习 课后学员学习进度跟踪  每日反馈
    2. 进班专门老师进行一对一的学习计划的制定  课程跟踪
    3. 阶段考核 (重读(免费))  学会才毕业
    4. 就业指导 就业跟踪 工作当中解答  ....  毕业后 学习规划 让学员可以快速涨薪

工作的 1
读书 2  兼职  积累经验
从事什么样的职业
A+  满足  提升 技能
转行   数据分析
基础 - 框架 - 项目(自动化) - 爬虫(数据采集) - 数据分析
脱产 成本高 学费也高  基础 爬虫   笔试


没有学习过 啥都不懂
学习后
今天上课没来   补课 每天都可以跟上课程的教学   + 录播 + 一对一的解答

'''

import json

import requests
from urllib import parse

# 创建一个接口的函数
def sebdsms(appkey, mobile, tpl_id, tpl_value):
    '''
    :param appkey: 申请的短信接口的key值
    :param mobile: 接收短信的手机号码
    :param tpl_id: 短信模板
    :param tpl_value: 验证码信息
    :return:
    '''
    # 1. 请求接口的url
    url = 'http://v.juhe.cn/sms/send'
    # 参数的传递
    params = 'mobile={}&tpl_id={}&tpl_value={}&key={}'.format(mobile, tpl_id, parse.quote(tpl_value), appkey)
    # 2. 请求接口平台
    wp = requests.get(url, params=params).text
    result = json.loads(wp)
    if result:
        error_code = result['error_code']
        if error_code == 0:
            # 短信发送成功
            smsid = result['result']['sid']
            print('短信验证码的ID:{}'.format(smsid))
        else:
            print('短信发送失败....{}'.format(result['reason']))
    else:
        print('请求接口平台失败...')


def main():
    # 短信的appkey值
    appkey = '799aaf477f15693a7cd49359556fede8'
    # 端接收人的号码
    poth = input('请输入你要发送的号码:')
    mobile = poth
    # 短信模板ID
    tpl_id = '170620'
    # 验证码
    code = input('请输入你想要发送的验证码:')
    tpl_value = '#code#={}'.format(code)
    sebdsms(appkey, mobile, tpl_id, tpl_value)


if __name__ == '__main__':
    main()


