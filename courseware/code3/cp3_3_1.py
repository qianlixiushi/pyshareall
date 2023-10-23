#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_3_1.py
# @Author: WRH
# @Date  : 2021/2/6
# @Edition:Python3.8.6

# 分支结构：分为单分支结构（if语句）和多分支结构（if-elif-else语句）

# 单分支结构（if语句）
'''
单分支结构书写格式

if 表达式：#表达式为真时执行缩进下面的语句块
    语句块
'''
name = input('请输入您的姓名：')
age = int(input('请输入您的年龄：'))
if age >= 18:  # if语句后面有冒号
    print(name, '已经成年,符合驾照考试规定')
    # 冒号后面属于if语句条件下执行的语句要在开头缩进四个空格，pycharm默认缩进，也可以使用Tab键进行缩进。

