#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : pandas数据可视化入门.py
# Author: MuNian
# Date  : 2019/7/20

'''
首选Python行业: 算法 (年薪70W)  AI(无人  智能  人工智能专家级别 北京三环内买套房子  初级AI工程师 50K左右)
就业趋势笔记好的:
    1. 自动化  爬虫  web开发( 后端  全栈开发)
8K -27K
4.5  个月 为一期
1 3 5 正课 2 4 6解答课 20:30 -22:30
数据处理
线上直播 + 课后录播 + 随堂笔记  一对辅导 补课 解答
学会才毕业 考核 重修免费

基础语法 基础格式 ----> web开发(重点:网页结构) ---> 爬虫(数据采集  数据处理) -- 数据分析
课中测试 课后作业


'''

# pip install  库名
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 从csv文件导入数据
df = pd.read_csv('input/telecom_churn.csv')
print(df.head())
# 数据维度
print(df.shape)
# 特征的名称  列标题
print(df.columns)
# 特征类型
print(df.info())
# Churn特性转换成int64
df['Churn'] = df['Churn'].astype('int64')
# 根据基本的统计特征(int64 float64):不缺失值的数量 平均值  标准差 范围  中位数
print(df.describe())
# 非数字的统计特征
print(df.describe(include=['object', 'bool']))
sns.countplot(x='International plan', hue='Churn', data=df)
plt.show()
# value_counts 方法  object - bool
print(df['Churn'].value_counts())
# 默认的返回是float64
print(df['Churn'].value_counts(normalize=True))
# ascending=False 按降序的排序
print(df.sort_values(by='Total day charge', ascending=False).head())
# 同时操作多个列进行排序
print(df.sort_values(by=['Number vmail messages', 'Churn'], ascending=[True, False]).head())
sns.countplot(x='Customer service calls', hue='Churn', data=df)
plt.show()




