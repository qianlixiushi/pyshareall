#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_2_1.py
# @Author: WRH
# @Date  : 2021/2/5
# @Edition:Python3.8.6

# 顺序结构

# 顺序结构图
'''
语句A
↓
语句B
↓
语句C
'''

# 例3-1
# 现实问题：求语文、数学、英语三门功课的平均成绩，平均成绩保留小数点后1位。
# 依据程序设计基本模式IPO（Input、Process、Output）将现实问题拆解为计算机可执行的程序步骤：
'''
1.编写输入语文、数学、英语三门功课的成绩的代码(Input)
2.编写计算平均成绩的代码(Process)
3.编写输出平均成绩，要求平均成绩保留小数点后1位的代码(Output)
'''

# 输入模块代码
chinese = float(input('请输入您的语文成绩：'))
math = float(input('请输入您的数学成绩：'))
english = float(input('请输入您的英语成绩：'))
# 计算平均成绩模块代码
average = (chinese + math + english)/3
# 输出模块代码
print('您的平均成绩为：%.1f' % average)
'''
%为Python语言的格式化符:
%.1f表示要把%所代表的变量格式化为保留小数点后1位
% average表示%所代表的的变量是average
'''

# 例3-2
# 现实问题：求圆的周长和面积。
# 依据程序设计基本模式IPO（Input、Process、Output）将现实问题拆解为计算机可执行的程序步骤：
'''
1.编写输入圆的半径的代码(Input)
2.编写计算圆的周长与面积的代码(Process)
3.编写输出圆的周长和面积的代码(Output)
'''
import math  # 因为计算圆周长和面积时要用到π的值，而math模块中包含常量pi(π），所以要先导入math以使用该值。

radius = float(input("请输入圆的半径："))  # 输入圆的半径

circumference = 2*math.pi*radius  # 计算圆的周长C=2πr
area = math.pi*radius*radius  # 计算圆的面积S=πr² 或者area = math.pi*radius**2

print("圆的周长为：%.2f" % circumference)  # 输出圆的周长
print("圆的面积为：%.2f" % area)  # 输出圆的面积

# 例3-3
# 现实问题：输出当年的年历
import calendar

year = int(input('请输入年份：'))
table = calendar.calendar(year)
print(table)

# calendar模块常用的函数
'''
calendar.month(year, month) # 获取月历
calendar.monthcalendar(year, month) # 以日期为元素的一维列表，以周日期为元素的二维列表获取月历
print(calendar.weekday(2021, 2, 5))  # 获取指定日期的星期代码，0代表星期一，1代表星期二，2代表星期三，其余类推
'''
