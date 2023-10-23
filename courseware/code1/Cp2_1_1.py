#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cp2_1_1.py
# @Author: WRH
# @Date  : 2020/12/8

# Python的基本词法单位

# python之禅
import this
# 运行代码快捷键alt + shift + F10选择运行的文件，shift + F10运行已选择的文件
# 如果需要更改快捷键可在【File】-【Settings】-【Keymap】搜索框中输入run查询修改

# 我的第一行代码
print('Hello World!')  # 代码的输入一定是在英文状态下
print("他说：'人生苦短，我用Python！'")  # '和"都可以使用，如果是多行注释可使用'''或"""

# 常量、标识符、变量、运算符、表达式、语句
x = 1      # x是变量：运行过程中值可以被更改的量。=为赋值符号（不是等于号，等于号用==表示）
# 数字1是常量：初始化（第一次赋值）后就固定不变的值
y = x + 1  # y是变量，x是变量，+是运算符，1是常量，x+1是表达式
print(y)   # print()为函数，用来输出结果
# 以上三行都是语句

# 变量的命名
'''
命名规则:
1.只能是任意字母、数字、汉字、下划线_的组合
2.开头的字符不能是数字
3.不能与关键字同名
4.严格区分大小写
'''

# 关键字
import keyword
print(keyword.kwlist)

# 命名最好简短又有描述性，比如name,number等
name = '张三'
number = 1

# 我的第一段完整代码
import math  # 导入标准库math,python的库有两种，一种是标准库，安装了Python时就有了，另一种是扩展库，也叫第三方库，需要自行安装。

x = -18  # 给变量x赋值-18
y = math.fabs(x)  # 调用标准库math中的求绝对值的函数fabs(),给变量y赋值x的绝对值
print(y)  # 输出y的结果



