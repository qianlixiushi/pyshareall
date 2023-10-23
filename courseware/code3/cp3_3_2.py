#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_3_2.py
# @Author: WRH
# @Date  : 2021/2/6
# @Edition:Python3.8.6

# 多分支结构（if-elif-else语句）
'''
多分支结构（if-elif-else语句）

if 表达式1：
    语句块A
elif 表达式2：
    语句块B
elif 表达式3：
    语句块C
else:
    语句块D
'''

name = input('请输入你的姓名')
chinese = float(input('请输入您的语文成绩：'))
math = float(input('请输入您的数学成绩：'))
english = float(input('请输入您的英语成绩：'))
average = (chinese + math + english)/3
if average >= 85:
    print(name, '获得一等奖')
elif average >= 75:  # elif语句后面和if语句一样要有冒号
    print(name, '获得二等奖')  # 冒号后面属于elif语句条件下执行的语句要在开头缩进四个空格
elif average >= 60:
    print(name, '获得三等奖')
else:
    print(name, '没有获奖')

# 如果只考虑一种表达式的成立与不成立，则没有elif分支，多分支结构（if-elif-else语句）变成双分支结构（if-else语句）

name = input('请输入你的名字')
score = float(input('请输入你的成绩'))
if score >= 60:
    print(name, '通过考试')
    print('可以获得证书')  # 同一条件下的语句都要缩进四个空格，进行左对齐。
else:
    print(name, '未通过考试')
    print('不能获得证书')

# 例3-4
# 编写程序，从键盘输入一个整型数字，判断该数字是否为偶数。
number = int(input("请输入一个整型数据："))  # int()函数确保输入数字转化为整数
if number % 2 == 0:
    print(number, "是一个偶数")
else:
    print(number, "不是一个偶数")

# 例3-5
# 编写程序，从键盘输入三条边，判断是否能够构成一个三角形。如果能，则提示可以构成三角形；如果不能，则提示不能构成三角形。
side1 = float(input("请输入三角形第一条边："))  # float()函数可以不带
side2 = float(input("请输入三角形第二条边："))
side3 = float(input("请输入三角形第三条边："))
if (side1+side2 > side3) and (side2+side3 > side1) and (side1+side3 > side2):  # 组成三角形的条件是任意两边之和大于第三边
    print(side1, side2, side3, "可以构成三角形")
else:
    print(side1, side2, side3, "不能构成三角形")

# 例3-6
# 编写程序，调用随机函数生成一个1～100之间的随机整数，从键盘输入数字进行猜谜，给出猜测结果（太大、太小、成功）的提示。
'''
Python的内置随机数模块random有下列常用函数：
random.random()	# 生成一个半开区间[0.0,1.0）的浮点数n,0 <= n < 1.0
random.randint(start,stop) # 生成一个闭区间[start,stop]的整数n,start <= n <= stop
random.randrange(start,stop[,step])	# 随机返回一个range(start,stop[,step])中的整数
random.choice(seq) # 随机从序列seq（字符串、元组、列表）中挑选返回一个元素
random.shuffle(lst)	#将列表lst的序列随机重排（不能作用于字符串和元组）
'''
import random  # 导入random模块
randnumber = random.randint(1, 100)  # 调用随机函数random.ranint(start,stop)生成一个大于等于1，小于等于100之间的随机整数
guess = int(input("请输入您的猜测："))  # 输入你猜测的这个随机数
if guess > randnumber:  # 编写if-elif-else语句将电脑随机生成的数字和你猜测的数字进行对比并输出结果
    print("您的猜测太大")
elif guess < randnumber:
    print("您的猜测太小")
else:
    print("恭喜您猜对了")


# 课堂作业-答案下节课讲
'''
编写程序，提示用户输入用户名和密码，要求先判断用户名再判断密码，如果用户名不正确，则直接提示用户名输入有误；
如果用户名正确，则进一步判断密码，并给出判断结果的提示。
'''
