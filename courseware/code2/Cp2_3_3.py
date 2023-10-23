#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cp2_3_3.py
# @Author: WRH
# @Date  : 2021/2/3
# @Edition:Python3.8.6

# 常用的Python数学运算类内置函数
'''
abs(x) # 取绝对值，也就是5
round(x) # 四舍五入取整，也就是3.0
pow(x, y) # 乘方相当于2**3，如果是pow(2, 3, 5)，相当于2**3 % 5
divmod(x,y) # 返回除法结果和余数
max([x,y,z]) # 求最大值
min([x,y,z]) # 求最小值
sum([x,y,z]) # 求和
'''
print(abs(-5))

# math模块中的函数
'''
fabs(x)	返回x的绝对值（float类型）
ceil(x)	取大于等于x的最小的整数值，如果x是一个整数，则返回x
floor(x) 取小于等于x的最大整数值，如果x是一个整数，返回自身
trunc(x) 截取为最接近0的整数
factorial(x) 取x阶乘的值
sqrt(x)	返回x的平方根
exp(x)以e为底的指数运算
log(x,y) 对数
'''

import math  # 首先导入标准库math
print(math.fabs(-5))  # 使用函数时要在函数名前面加上math.
print(math.log(8, 2))
'''
from math import * # 另外一种导入方式，可以在函数前不加math.
print(log(2,6))
'''
# 输入与输出
# 输入函数input()
'''
input() 函数用于向用户生成一条提示，然后获取用户输入的内容。
由于input()函数总会将用户输入的内容放入字符串中，因此用户可以输入任何内容，input()函数总是返回一个字符串。
'''
x = input('请输入你的年龄')
print('哇，原来你只有' + x + '岁！')
print(type(x))

# 一个计算考试总分的小程序
name = input('请输入你的姓名')
a = input('请输入你的语文分数')
b = input('请输入你的数学分数')
c = input('请输入你的英语分数')
sum_score = sum([int(a), int(b), int(c)])
# 因为input()函数返回的数据总是字符串，所以要用int()函数将输入的数据类型转换为整数
print(name + '考了' + str(sum_score) + '分。')
# 因为sum_score变量赋值的数据为整数，所以要用str()函数将输入的整数数据类型转变成字符数据类型，以保证+前后一致






