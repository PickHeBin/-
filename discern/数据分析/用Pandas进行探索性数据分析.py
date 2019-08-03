#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 用Pandas进行探索性数据分析.py
# Author: MuNian
# Date  : 2019/7/16

import numpy as np
import pandas as pd
pd.set_option("display.precision", 2)
# 通过分析数据集论电信运营商客户的流失率。让我们读取数据(使用read_csv)
df = pd.read_csv('input/telecom_churn.csv')
print(df.head())
# 数据维度、特征名称和特性类型。
print(df.shape)
print(df.columns)
print(df.info())
# 此方法应用于Churn特性将其转换为int64
df['Churn'] = df['Churn'].astype('int64')
# 显示每个数值特征的基本统计特性(int64和float64(类型)：不缺失值的数量、平均值、标准差、范围、中位数、0.25和0.75四分位数
print(df.describe())
# 查看非数字特性的统计数据，必须在include参数
print(df.describe(include=['object', 'bool']))
# 用于范畴(类型)object)和布尔(类型bool)我们可以使用value_counts方法
print(df['Churn'].value_counts())
# 通过normalize=True到value_counts
print(df['Churn'].value_counts(normalize=True))
# DataFrame可以根据其中一个变量(即列)的值进行排序 使用ascending=False按降序排序
print(df.sort_values(by='Total day charge', ascending=False).head())
# 按多个列进行排序
print(df.sort_values(by=['Churn', 'Total day charge'],
        ascending=[True, False]).head())
# 若要获取单个列，可以使用DataFrame['Name']
print(df['Churn'].mean())
# 数字特征的平均值
print(df[df['Churn'] == 1].mean())
import matplotlib.pyplot as plt
# pip install seaborn
import seaborn as sns
sns.countplot(x='International plan', hue='Churn', data=df)
plt.show()

sns.countplot(x='Customer service calls', hue='Churn', data=df)
plt.show()