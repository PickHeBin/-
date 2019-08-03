#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : PIma.py
# Author: MuNian
# Date  : 2019/7/17
'''
训练数据集: 以前数据 未来数据的走向 80%

机器学习  + 深度学习 = AI领域
机器人  智能设备  反向传播   5G AI云通道   500亿   100多G  训练集  广告页面
阿里服务器
非计算机专业 达不到AI标准  50K以上的薪资
Python就业趋势:
    web(全栈 后端)  自动化 爬虫   15K
AI  算法  数据分析(量化) 游戏开发
架构师是怎么思考问题的
自动化  全栈开发 爬虫开发 后端开发
市场 主流框架  数据存储   业务逻辑   独立开发的能力
自动化测试  脚本  跟着老师一起学习
课程4.5个月 1 2 5 正课  2 4 6 解答课  每天晚上 20:30 - 22:30
课后一对一的辅导 解答 补课 课后反馈
线上直播 + 课后录播 + 随堂笔记 源码
VIP保障:
    1.  制定学习计划
    2. 课中测试 课后作业 课后解答 补课  学员情况---> 补课
    3. 小班授课模式  30个学员 6个老师
    4. 阶段考核 升班考核 重修(免费的) 学会才毕业  项目实践检验  独立开发项目能力
    5. 授课老师 架构师
    6. 就业服务: 就业指导 就业跟踪 模拟BAT笔试面试  学习规划 ...

长沙
学习时间挤出来的  晚上上课 白天解答
高清录播 + 单独辅导

5080 AI班级学习

7880 享受 1000学费的优惠  = 6880  全栈班级 + AI - 500 = 6380 / 12  = 一个月就500多就能学习了






'''
import numpy
import pandas
import matplotlib.pylab as plt
# 特征缩放
from sklearn.preprocessing import StandardScaler
# 散点矩形生成库
from pandas.plotting import scatter_matrix
# 交叉验证法
from sklearn.model_selection import KFold
# 逻辑回归算法
from sklearn.linear_model import LogisticRegression

# 新建一个简单的数据帧
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

# 从csv文件中来加载数据
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
# 读取训练集
data = pandas.read_csv(url, names=names)
print(data.shape)

# 描述性统计来理解数据
description = data.describe()
print(description)

# 数据可视化
scatter_matrix(data)
plt.show()

# 预处理数据建模
array = data.values
# 分成输出和输入组件
X = array[:,0:8]
Y = array[:, 8]
scaler = StandardScaler().fit(X)
# 通过定心 定标 实现 标准化
rescaledx = scaler.transform(X)
print(rescaledx)



