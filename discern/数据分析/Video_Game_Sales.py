#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Video_Game_Sales.py
# Author: MuNian
# Date  : 2019/7/19

import  numpy as np
import  pandas as pd

from subprocess import check_output

data = pd.read_csv('input/vgsales.csv')
print(data.info)
data.dropna(how='any', inplace = True)
print(data.info())

# 把数据从float 转换成int
data.Year = data.Year.astype(int)
print(data.head())

from bokeh.io import output_file,show,output_notebook,push_notebook
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource,HoverTool,CategoricalColorMapper
from bokeh.layouts import row,column,gridplot
from bokeh.models.widgets import Tabs,Panel
output_notebook()

'''
x_axis_label:标签的x轴
y_axis_label:标签的y轴
tools:工具移动或缩放图形
pan:幻灯片的plot 
box_zoom:缩放
circle:比如散在matplotlib中
size:大小
color:颜色
alpha:不透明度输出
put_file:保存我们的图形与.html扩展名显示:显示图形
'''

plot = figure(x_axis_label = 'x', y_axis_label = 'y', tools = 'pan, box_zoom')
plot.circle(x=[5, 4, 3, 2, 1], y=[1, 2, 3, 4, 5], size = 10, color = 'black', alpha = 0.7)
output_file('my_first_bokeh_plot.html')
show(plot)

plot = figure()
plot.diamond(x=[5, 4, 3, 2, 1], y=[1, 2, 3, 4, 5], size = 10, color = 'black', alpha = 0.7)
plot.cross(x=[1, 2, 3, 4, 5], y=[1, 2, 3, 4, 5], size = 10, color = 'red', alpha = 0.7)
show(plot)

'''
line:线图
line_width:线之粗细
fill_color:用颜色填充圆的内部

patches: 一个图上同时有多个多项式形状
fill_color: 补片
line_color: 颜色的线周围的补丁

'''

plot = figure()
plot.line(x=[1,2,3,4,5,6,7],y = [1,2,3,4,5,5,5],line_width = 2)
plot.circle(x=[1,2,3,4,5,6,7],y = [1,2,3,4,5,5,5],fill_color = "white",size = 10)
show(plot)

plot = figure()
plot.patches(xs = [[1,1,2,2],[2,2,3,3]],ys = [[1,2,1,2],[1,2,1,2]],fill_color = ["purple","red"],line_color = ["black","black"])
# show(plot)


# 将列的名称映射到序列或数组
source = ColumnDataSource(data)
plot = figure()
plot.circle(x="Year",y="Global_Sales",source = source)
show(plot)

'''
Selection appearance: 当你在数据上选择某个点时，这个点就会发光，而其他的点就会熄灭
tools:
    box_select and lasso_select: 选择工具
    selection_color: 当您选择“点”时，它将变成“选定颜色”
    nonselection_fill_alpha: 其他未选择的点变成未选择的alpha
    nonselection_fill_color: 其他未选择的点变成未选择的颜色
HoverTool: cursor
    Crosshair: 行光标
    hover_color: 盘旋的颜色
Color mapping: 选择字段的颜色映射. (like hue in seaborn)
    factors: 颜色映射变量的名称
    palette: 选择因素的颜色
'''

plot = figure(tools="box_select,lasso_select")
plot.circle(x= "Year",y = "Global_Sales",source=source,color = "black",
            selection_color = "orange",
            nonselection_fill_alpha = 0.2,
           nonselection_fill_color = "blue")
show(plot)

# Hover appearance
hover = HoverTool(tooltips = [("Genre of game","@Genre"),("Publisher of game","@Publisher")], mode="hline")
plot = figure(tools=[hover,"crosshair"])
plot.circle(x= "Year",y = "Global_Sales",source=source,color ="black",hover_color ="red")
show(plot)

# Color mapping
factors = list(data.Genre.unique())
colors = ["red","green","blue","black","orange","brown","grey","purple","yellow","white","pink","peru"]
mapper = CategoricalColorMapper(factors = factors,palette = colors)
plot =figure()
plot.circle(x= "Year",y = "Global_Sales",source=source,color = {"field":"Genre","transform":mapper})
show(plot)


p1 = figure()
p1.circle(x = "Year",y= "Global_Sales",source = source,color="red")
p2 = figure()
p2.circle(x = "Year",y= "EU_Sales",source = source,color="black")
p3 = figure()
p3.circle(x = "Year",y= "NA_Sales",source = source,color="blue")
p4 = figure()
p4.circle(x = "Year",y= "JP_Sales",source = source,color="orange")
layout1 = row(p1,p2)
layout2 = row(p3,p4)
layout3= column(layout1,layout2)
show(layout3)