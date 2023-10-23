#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cp2_2_1.py
# @Author: WRH
# @Date  : 2021/1/29
# @Edition:Python3.8.6

# Python的基本数据类型

"""
Python3中有六个标准的数据类型：
数值 Number
字符串 String
列表 List
元组 Tuple
集合 Set
字典 Dictionary
"""

# Number（数值）有四种类型
# 整数（int）、浮点数（float）、布尔值（bool）、复数（complex）

# 1.整数（int）：不带小数的数字，如10，-19，Python中整数没有长度限制
'''
Python中整数的书写支持四种数制：
十进制
二进制:数值前缀0b或0B # 英语单词binary，二进（位，制）的,通常用两个不同的符号0（代表零）和1（代表一）来表示
八进制：数值前缀0o或0O # 英语单词octal,八进（位，制）的,一种以8为基数的计数法，采用0，1，2，3，4，5，6，7八个数字，逢八进1
十六进制：数值前缀0x或0X  #英语单词hexadecimal,十六进（位，制）的,一种逢16进1的进位制。
        一般用数字0到9和字母A到F（或a~f）表示，其中:A~F表示10~15
'''
x = 0b1010
print(x)

y = 0o15
print(y)

z = 0x2f
print(z)

# 2.浮点数（float）：带小数的数字，如4.0,0.5,-2.7315e2,
# 浮点数只能以十进制数形式书写表达
# 计算机内部以二进制数表示，由于机内表示浮点数的二进制位数所限，所以计算结果最后的二进制位被截断，产生的精度误差称为截断误差。
print(2/3)

# 3.布尔值（bool），即逻辑值，有两种True和False,代表“真”和“假”。对应数值为1和0。
print(1 == 1)  # 注意区分：=为赋值符号，==为等于号。
print(123 == '123')

# 4.复数（complex）：由一个实数和一个虚数组合构成，表示为：x+yj,x为实部（real),y为虚部（imag)
x = 123+12j
print(x.real)
print(x.imag)

# 判断数据类型的方法：type()函数
x = 'a'
print(type(x))  # 输出变量x的数据类型

y = 123
print(type(y))  # 输出变量y的数据类型





