#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_3_3.py
# @Author: WRH
# @Date  : 2021/2/6
# @Edition:Python3.8.6

# 分支语句嵌套
'''
当有多个条件需要满足并且条件之间有递进关系时，可以使用分支语句的嵌套。
其中，if子句、elif子句以及else子句中都可以嵌套if语句或者if-elif-else子句。
'''
# 我国的婚姻法规定，男性22岁为合法结婚年龄，女性20岁为合法结婚年龄。
# 因此如果要判断一个人是否到了合法结婚年龄，首先需要使用双分支结构判断性别，再用递进的双分支结构判断年龄，并输出判断结果。
sex = input("请输入您的性别（M或者F）：")
age = int(input("请输入您的年龄（1-120）："))
if sex == 'M':
    if age >= 22:  # 注意缩进四个空格
        print("到达合法结婚年龄")  # 注意同样要再缩进四个空格
    else:  # 注意此else语句与第二个if语句为同一级
        print("未到合法结婚年龄")
else:  # 注意此else语句与第一个if语句为同一级
    if age >= 20:
        print("到达合法结婚年龄")
    else:
        print("未到合法结婚年龄")

# 例3-7
# 编写程序，从键盘输入用户名和密码，要求先判断用户名再判断密码，如果用户名不正确，则直接提示用户名输入有误；
# 如果用户名正确，则进一步判断密码，并给出判断结果的提示。
username = input("请输入您的用户名：")
password = input("请输入您的密码：")
if username == "admin":
    if password == "123456":
        print("输入正确，恭喜进入！")
    else:
        print("密码有误，请重试！")
else:
    print("用户名有误，请重试！")

# 例3-8
# 编写程序，开发一个小型计算器，从键盘输入两个数字和一个运算符，根据运算符（+、-、*、/）进行相应的数学运算，
# 如果不是这4种运算符，则给出错误提示。
first = float(input("请输入第一个数字："))
second = float(input("请输入第二个数字："))
sign = input("请输入运算符号：")
if sign == '+':
    print("两数之和为：", first+second)
elif sign == '-':
    print("两数之差为：", first-second)
elif sign == '*':
    print("两数之积为：", first*second)
elif sign == '/':
    if second != 0:  # !=为不等于号
        print("两数之商为：", first/second)  # 现实问题用计算机自动化解决时一定要把问题的分支想全面
    else:
        print("除数为0错误!")
else:
    print("符号输入有误！")
