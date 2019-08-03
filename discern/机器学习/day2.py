#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day2.py
# Author: MuNian
# Date  : 2019/7/17

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 列出输入目录中的文件
import warnings
from subprocess import check_output

# 忽略警告,
warnings.filterwarnings('ignore')

data = pd.read_csv('column_2C_weka.csv')
# 查看可用的情节样式
print(plt.style.available)
plt.style.use('ggplot')
# 查看特性和目标变量
# 它的默认值显示前5行(示例)。例如，如果您想查看100行，只需写入head(100)
print(data.head())
# 问题是这个数据有NaN值和长度吗，我们来看信息
print(data.info())
# 为了使数据可视化，值之间应该更接近
print(data.describe())
# pd.plotting.scatter_matrix:
# 1. 红色和绿色 绿色正常 红色异常
# 2. c: 颜色 3. figsize:形状和尺寸 4. diagonal：每个特征的直方图 5.alpha: b不透明 6. s:标志的大小 7. marker:标注类型
color_list = ['red' if i=='Abnormal' else 'green' for i in data.loc[:,'class']]
pd.plotting.scatter_matrix(data.loc[:, data.columns != 'class'],
                                       c=color_list,
                                       figsize= [15,15],
                                       diagonal='hist',
                                       alpha=0.5,
                                       s = 200,
                                       marker = '*',
                                       edgecolor= "black")
# 散点矩阵中每个特征之间都有关系但是有多少正常(绿色)和异常(红色)类
plt.show()
# Searborn库中有countplot()，它计算类的数量
sns.countplot(x="class", data=data)
# 还可以使用value_counts()方法打印它
print(data.loc[:, 'class'].value_counts())

from sklearn.neighbors import KNeighborsClassifier
# KNN:看看最近标记的K个数据点
# 分类方法 需要训练我们的数据
knn = KNeighborsClassifier(n_neighbors = 3)
x,y = data.loc[:,data.columns != 'class'], data.loc[:,'class']
# 训练数据
knn.fit(x,y)
# 预测的数据
prediction = knn.predict(x)
print('Prediction: {}'.format(prediction))

'''
我们用KNN来拟合数据并进行预测。
那么，我们的预测是否正确或者说我们的准确度是多少或者说准确度是评价我们的结果的最佳指标?让我们来回答这个问题
测量模型的性能:
准确度是一种常用的度量方法，它是正确预测的一部分。我们会使用它，但还有一个问题
我用x(特性)训练数据，并再次预测x(特性)
'''

from sklearn.model_selection import train_test_split
# train_test_split(x,y,test_size = 0.3,random_state = 1)
# x: 特征
# y: 目标变量(正常、异常)
# test_size: 测试大小的百分比。例如test_size = 0.3, test size = 30%， train size = 70%
# random_state: 设置一个种子。如果这个种子是相同的数字，那么train_test_split()每次都会生成完全相同的分割
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 1)
knn = KNeighborsClassifier(n_neighbors = 3)
# 训练数据
x,y = data.loc[:,data.columns != 'class'], data.loc[:,'class']
knn.fit(x_train,y_train)
# 预测的数据
prediction = knn.predict(x_test)
#print('Prediction: {}'.format(prediction))
# 预测并给出测试集的准确性
print('KNN (K=3)的精度为: ',knn.score(x_test,y_test))
'''
准确率是86%，这样好吗?其实我也不知道，我们会在最后看到。
现在的问题是为什么我们选择K = 3或者我们需要选择什么值K，答案是:模型复杂度
'''

neig = np.arange(1, 25)
train_accuracy = []
test_accuracy = []
# 循环不同的k值
for i, k in enumerate(neig):
    # k从1至25(不包括)
    knn = KNeighborsClassifier(n_neighbors=k)
    # 符合 knn
    knn.fit(x_train,y_train)
    # train 准确性
    train_accuracy.append(knn.score(x_train, y_train))
    # test  测试的准确性
    test_accuracy.append(knn.score(x_test, y_test))

# Plot
plt.figure(figsize=[13,8])
# 线条标注
plt.plot(neig, test_accuracy, label = 'Testing Accuracy')
plt.plot(neig, train_accuracy, label = 'Training Accuracy')
plt.legend()
# 标题名
plt.title('-value VS Accuracy')
# x和y坐标
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.xticks(neig)
plt.savefig('graph.png')
plt.show()
print("最好的精度 {} 与 K = {}".format(np.max(test_accuracy),1+test_accuracy.index(np.max(test_accuracy))))
# 监督式学习
# 探索性数据分析
'''
监督式学习
我们将学习线性回归和逻辑回归
这个骨科患者的数据不适合回归，所以我只使用了sacral_slope和pelvic_incidence of abnormal这两个特征
我认为特征是pelvic_incidence，目标是sacral_slope
让我们看一下散点图，以便更好地理解它的形状(-1,1):如果您不使用它形状的x或y becaomes(210，)，我们不能在sklearn中使用它，所以我们使用shape(-1,1)和shape of x或y be(210, 1)
'''
data1 = data[data['class'] == 'Abnormal']
x = np.array(data1.loc[:, 'pelvic_incidence']).reshape(-1, 1)
y = np.array(data1.loc[:, 'sacral_slope']).reshape(-1, 1)

plt.figure(figsize=[10, 10])
plt.scatter(x=x, y=y)
plt.xlabel('pelvic_incidence')
plt.ylabel('sacral_slope')
plt.show()

# 线性回归
'''
Y=AX+b，其中y=目标，x=特征，a=模型参数我们根据线性回归中丢失函数的最小误差函数选择模型(A)的参数，用普通最小二乘(OLS)作为丢失函数。
OLS：所有残差之和，但一些正残差和负残差可以互相抵消，所以我们用残差平方和。
它被称为OLS评分：分数使用R^2方法，即(y_pred-y_mean)^2)/(y_real-y_mean)^2。
'''
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
# 预测空间
predict_space = np.linspace(min(x), max(x)).reshape(-1, 1)
reg.fit(x, y)
# 预测
predicted = reg.predict(predict_space)
# R ^ 2
print('R^2 得分:', reg.score(x, y))
# 绘制回归线和散点
plt.plot(predict_space, predicted, color='black', linewidth=3)
plt.scatter(x=x,y=y)
plt.xlabel('pelvic_incidence')
plt.ylabel('sacral_slope')
plt.show()

from sklearn.model_selection import cross_val_score
reg = LinearRegression()
k = 5
# 使用上面定义的x和y的reg(线性回归)，K等于5。它的意思是5次(分裂，训练，预测)
cv_result = cross_val_score(reg,x,y,cv=k) # uses R^2 as score
print('CV 分数: ',cv_result)
print('CV 分数平均: ',np.sum(cv_result)/k)

'''
当我们学习线性回归时，选择参数(系数)，同时最小化损失函数。
如果线性回归认为某一特征是重要的，则该特征的系数较高。
然而，这可能会导致过度拟合，就像KNN中的记忆一样。为了避免过度拟合，我们使用正则化来惩罚大系数。
岭回归:第一个正则化技术。它也被称为L2正则化。
岭回归损失函数= OLS +和(参数^2)是我们需要选择拟合和预测的参数。选择和p相似
'''

from sklearn.linear_model import Ridge
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 2, test_size = 0.3)
ridge = Ridge(alpha = 0.1, normalize = True)
ridge.fit(x_train,y_train)
ridge_predict = ridge.predict(x_test)
print('Ridge score: ',ridge.score(x_test,y_test))

from sklearn.linear_model import Lasso
x = np.array(data1.loc[:,['pelvic_incidence','pelvic_tilt numeric','lumbar_lordosis_angle','pelvic_radius']])
x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 3, test_size = 0.3)
lasso = Lasso(alpha = 0.1, normalize = True)
lasso.fit(x_train,y_train)
ridge_predict = lasso.predict(x_test)
print('Lasso score: ',lasso.score(x_test,y_test))
print('Lasso coefficients: ',lasso.coef_)

'''
pelvic_incidence和pelvic_tilt数值是重要的特性，但其他特性并不重要
现在我们来讨论一下准确性。对于模型选择的度量是否足够。
例如，有一个数据包含95%的正常样本和5%的异常样本，我们的模型使用精度作为测量指标。
该模型对所有样本的正确率为100%，正确率为95%，但对所有异常样本的分类是错误的。
因此，我们需要使用混淆矩阵作为不平衡数据的模型度量矩阵。
在使用混淆矩阵的同时，利用随机森林分类器进行分类
'''

# 随机森林的混淆矩阵
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
x,y = data.loc[:,data.columns != 'class'], data.loc[:,'class']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 1)
rf = RandomForestClassifier(random_state = 4)
rf.fit(x_train,y_train)
y_pred = rf.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
print('Confusion matrix: \n',cm)
print('Classification report: \n',classification_report(y_test,y_pred))

sns.heatmap(cm,annot=True,fmt="d")
plt.show()

from sklearn.metrics import roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
# abnormal = 1 and normal = 0
data['class_binary'] = [1 if i == 'Abnormal' else 0 for i in data.loc[:,'class']]
x,y = data.loc[:,(data.columns != 'class') & (data.columns != 'class_binary')], data.loc[:,'class_binary']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=42)
logreg = LogisticRegression()
logreg.fit(x_train,y_train)
y_pred_prob = logreg.predict_proba(x_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
# Plot ROC curve
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC')
plt.show()
