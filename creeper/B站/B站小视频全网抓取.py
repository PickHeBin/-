# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# # File  : B站小视频全网抓取.py
# # Author: MuNian
# # Date  : 2019/7/8
# '''
# 视频下载的流程:
#     1. 解析url 得到 视频的信息的地址url
#     2. 视频的url返回的数据是json
#         {键(唯一的):值}
#         a = {'1':3}
#         a['1']
#     3. json数据提取(数据清洗)
#
# 计算机可以识别的:
#     2进制数据 : 0001 1010 0010 0100
#     16进制文件:
#
# 爬虫领域: Python 老大级别
# 渗透网页 ---> 脚本  20行代码   C ---> 100行
# Python就业趋势:
#     web  自动化(自动化运维 自动化测试  脚本) 爬虫(数据采集 渗透 破解  逆向)
# AI + 大数据 = Python时代的首选语言
# 8K - 27K
# web   自动化  爬虫
# 4.5 个月 项目主导 快速就业
# 线上直播 + 课后录播 + 随堂笔记
# 1 3 5正课  2 4 6解答课  20:30 - 22:30   下午 : 补课
# 学会才毕业
# 达到什么样的企业标准:
#     1. 掌握市场主流常用的web  爬虫 自动化框架
#     2. 公司的需要开发独立的web前后端  精准数据采集  自动化部署  测试 运维
#     3. 独立打造搜索引擎
#     ....
#
# 1 -3 年项目经验水平   独立开发WEB网页 爬虫 自动化
# 基于linux
# 12K   文员  5K
# 3 - 5项目经验   15K
# Python 零基础的 入门高薪编程行业 Python首选
# Python 比其他语言简单 在未来的发展就业趋势比其他语言范围广
# 预科班  下午办理入学  晚上可以直接学习
# 学会才毕业
# 就业保障: 就业指导  就业跟踪  就业内推(名额限制 腾讯  学习能力)
# 考核(升班考试 重修(免费的))  学会才毕业  具备独立开发项目的能力
# 1. 入学学习计划制定(架构师一对一制定)
# 2. 课后辅导 补课 知识点吸收情况跟踪(每天都可以跟上课程进度)
# 3. 毕业后: 一对一的职业规划  快速涨薪
#
# 担心时间:
#     课后录播 + 课后辅导 一对一解答
#     跟上一期... 录播 + 解答 + 辅导  重修 (免费的)  毕业后期 考核 毕业标准
#
# 转行:
#     1. Web  爬虫 自动化  就业岗位最多的 薪资也是Ok的 8k - 20K
#     对行业的了解
#     项目经验
# Python 开发效率高  调用第三方库  自定义
# 最后一个名额  高薪就业 犹豫什么?
# 人工智能  首选Python  AI发展   5G - > AI云数据
# 微软:  谷歌 竞争 5G 趋势 Ai 领先
# 月薪6K 不要考虑买车  低于12K 不要考虑买房
# 15K
# 小康 个人薪资 20K  50K
# 专业不对口的工作   理想主义者 - 3K   大学  负债状态   实习 大公司 富士康 流水线 锻炼实习生
# 大学生4年  30w  != 毕业后一个月 6K   普通的研究生  6年  8K
# 现实主义打破大学生理想主义思维  现状  末尾淘汰制   软件公司 甲骨文 900 多名高管都是年薪百万级别
# AI 智能 底层  4W人
# 穷思维  永远都穷 没有能力  提升过自己
# 低级人群 -- 你们为什么没有钱
# 没有富人的接济   安于现状  习惯了温室  迷茫  提升  害怕  执行 坚持  买本书 坚持看多久
# 办理分期  12个月
# 下午学习 : 1000学费优惠 + 终身的解答
# 错过这个名额:  7880
#
#
# '''
#
# import requests
# # 自定义随机生成头部信息
# from fake_useragent import UserAgent
#
# ua = UserAgent()
#
#
# def VIdeo_Downloads(page):
#     # 视频信息的请求地址
#     # http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=11&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc
#     # http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset=21&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc
#     url = 'http://api.vc.bilibili.com/board/v1/ranking/top?page_size=10&next_offset={}&tag=%E4%BB%8A%E6%97%A5%E7%83%AD%E9%97%A8&platform=pc'.format(page)
#
#     # 请求头部信息
#     headers = {
#         'User-Agent': ua.random
#     }
#
#     # 请求视频信息的地址
#     response_data = requests.get(url, headers=headers).json()
#
#     # json数据通过键获取值
#     item = response_data.get('data').get('items')
#     for i in item:
#         ite = i.get('item')
#         # 视频的标题
#         Video_name = ite.get('description')
#         # 视频的下载链接的url
#         Video_downloads_url = ite.get('video_playurl')
#         # 请求视频的下载链接的url
#         sponse = requests.get(Video_downloads_url, headers=headers, stream=True)
#         # 设置每次下载的数据限制  1G = 1024Mb
#         chunk_size = 1024
#         # 异常捕获: 当代码出现问题的时候 但是不希望代码执行结束
#         try:
#             with open('b站小视频/' + Video_name + '.mp4', 'ab') as f:
#                 for data in sponse.iter_content(chunk_size=chunk_size):
#                     print('正在下载{}..'.format(Video_name))
#                     f.write(data)
#         except Exception as e:
#             pass
#
#
# for i in range(0, 100):
#     i = i * 10 + 1
#     VIdeo_Downloads(i)



