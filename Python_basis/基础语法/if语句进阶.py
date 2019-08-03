#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : if语句进阶.py
# Author: MuNian
# Date  : 2019/7/13

# holiday = '妇女节'
#
# if holiday == '情人节':
#     print('立马提出分手 后面再复合....')
#
# elif holiday == '妇女节':
#     print('祝女朋友38节快乐')
#
# elif holiday == '生日':
#     print('买蛋糕..')
#
# else:
#     print('每天都是节日')

has_ticket = 1
knife = 20

if has_ticket == 0:
    print('欢迎光临本火车站, 你有票请过下一个安检')

    if knife >= 20:
        print('不好意思,你的刀太长了..')

    else:
        print('欢迎乘坐本次火车.......')

else:
    print('你票都没有 你要干啥子?')