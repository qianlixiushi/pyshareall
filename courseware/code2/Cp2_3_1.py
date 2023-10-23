#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cp2_3_1.py
# @Author: WRH
# @Date  : 2021/2/2
# @Edition:Python3.8.6

# 变量类型的转换

# 1.float()函数：str类型、int类型的数据转化成为浮点数,注意：str类型数据里的字符只能由数字组成
print(float(1))

# 2.int()函数：能将str类型、float类型的数据转换成整数类型,注意：str类型数据里的字符只能由整数组成
# 转化成整数时不执行“四舍五入”
print(int(1.234))
print(int('8'))

# 3.round()函数：将浮点型数值圆整为整形
# Python采用的是’银行家圆整‘，将小数数字圆整为最接近的偶数，即’四舍六入五留双‘
print(round(1.4))  # 四舍
print(round(1.6))  # 六入
print(round(1.5))  # 五留双

# 4.bool()函数：将其他类型数据转换为布尔类型
# 数值0和空字符串转换为布尔类型为False
print(bool(0))
print(bool(''))
# 非0值和非空字符串转换为布尔类型为True
print(bool(-1))
print(bool('a'))
'''
布尔值可以进行算术运算，True为1，False为0
比如：
d = False + 1 + True
print(d) # d的值为2
'''

# 5.chr()函数：将一个整数按ASCII码转换为对应的字符。ord()函数：chr()函数的逆运算。
print(chr(65))
print(ord('a'))
print(ord('我'))
print(chr(25105))
'''
# 计算机常用编码
ASCII (American Standard Code for Information Interchange): 美国信息交换标准代码
Utf-8：针对Unicode的一种可变长度字符编码。它可以用来表示Unicode标准中的任何字符，而且其编码中的第一个字节仍与ASCII相容，
使得原来处理ASCII字符的软件无须或只进行少部份修改后，便可继续使用
'''

# 6.str()函数：将其他数据类型转换为字符
age = 18  # age被赋值为18这个数字
# print('我今年' + age + '岁了。') # 因为+运算符两边的数据需要类型一致，不用str()函数进行转化会报错
print('我今年' + str(age) + '岁了。')  # 使用str()函数将给age的赋值转化为18这个字符串，与+两侧的字符串数据类型保持一致。

# 7.eval()函数：将一个字符串类型的算术表达式转换为其执行结果，返回表达式的值。
print('1+2*3')
print(eval('1+2*3'))

