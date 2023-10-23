#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_5_2.py
# @Author: WRH
# @Date  : 2021/3/7
# @Edition:Python3.8.6

# try-except异常处理（在代码很多时比较实用，可以帮助程序员迅速定位错误代码的位置）
'''
异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
一般情况下，在Python无法正常处理程序时就会发生一个异常。
异常是Python对象，表示一个错误。
当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。
'''

# 1.try-except结构
# 可能存在异常的语句
obj = open("test.txt", "r")  # 尝试打开test.txt文件

# 添加异常处理语句
try:
    obj = open("test.txt", "r")  # 尝试打开test.txt文件
except IOError:
    print("文件打开失败")  # 如果不能打开输出：文件打开失败

# 2.try-except-else结构
try:
    num1 = int(input("请输入分子："))
    num2 = int(input("请输入分母："))
    num3 = num1/num2
except ZeroDivisionError:
    print("除数为0")
else:
    print(num3)

# 3.try-except-else-finally结构
try:
    obj = open("test.txt", "r")
except IOError:
    print("文件打开失败")
else:
    print("文件打开成功")
    obj.close()
finally:
    print("文件测试结束")  # 无论try语句块中是否有误，finally语句块都会执行

