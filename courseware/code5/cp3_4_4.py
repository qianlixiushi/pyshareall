#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_4_4.py
# @Author: WRH
# @Date  : 2021/3/4
# @Edition:Python3.8.6

# 转移和中断语句

# 1.break语句：用于中断当前循环的执行，跳出循环结构
while 1:  # 此表达式恒为真，当表达式恒为真时，循环将一直执行下去，无法靠自身终止，从而产生死循环。
    print('我是一个死循环')
    break  # break语句跳出当前的死循环
# 在死循环程序中，通过添加break语句终止程序的执行，称为半路循环。

number = 1  # 设置number初始值为1
while 1:  # 当为真时
    print("Python是一门编程语言")
    if number >= 5:  # 如果number大于等于5时
        break  # 中断执行，跳出当前循环
    number = number+1  # 对number进行重新赋值

# 例3-16
'''
编写程序，随机产生色子的一面（数字1～6），给用户三次猜测机会，程序给出猜测提示（偏大或偏小）。
如果某次猜测正确，则提示正确并中断循环；如果三次均猜错，则提示机会用完。
'''
import random  # 导入random库,ctrl+shift+F，输入random复习random库的使用
point = random.randint(1, 6)  # 使用random.randint()函数随机产生1到6之间的任意整数，包含1和6
count = 1  # 设置猜的次数初始值为1
while count <= 3:  # while-else语句控制第一阶循环语句，当次数小于等于三时继续执行下一行，否则输出：很遗憾，三次全猜错了！
    guess = int(input("请输入您的猜测(1-6)："))  # 输入猜的数字
    if guess > point:  # if-elif-else语句将用户猜的数字与计算机随机生成的数字进行比较，并输出相应提示
        print("您的猜测偏大")
    elif guess < point:
        print("您的猜测偏小")
    else:
        print("恭喜您猜对了")
        break
    count = count+1  # 对次数进行重新赋值
else:  # while支持一个else分支语句,此外还有for-else语句，可自行了解
    print("很遗憾，三次全猜错了！")

# 2.continue语句：用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
# continue语句和break语句的区别：continue语句跳出本次循环，而break跳出整个循环。

# 例3-17
# 编写程序，从键盘输入一段文字，如果其中包括“密”字（可能出现0次、1次或者多次），则输出时过滤掉该字，其他内容原样输出。

sentence = input("请输入一段文字：")  # 输入一段文字，比如”你看我的密码密不密“
for word in sentence:  # 对输入的一段文字进行逐字遍历
    if word == "密":  # 如果字是密
        continue  # 跳过剩余语句，继续新一轮循环
    print(word, end="")  # 当字不是密时，执行此语句

# 例3-18（对教材中的例子进行了修改）
# 编写程序，从键盘输入密码（正确的密码是123456），如果输入的密码不是123456，则要求重新输入。如果输入的密码正确则中断循环。

while 1:  # 此表达式恒为真，当表达式恒为真时，循环将一直执行下去
    password = input("请输入密码：")  # 输入密码
    if password != "123456":  # 如果输入的密码不是123456
        print("密码有误，请重试!")
        continue  # 跳过剩余语句，继续新一轮循环
    else:  # 如果输入的密码是123456
        print("恭喜您，密码正确！")
        break  # 终止整个循环

'''
# 思考题一：完善例3-18的代码，使输错密码超过3次时提示明日再重试。
代码参考如下：
number = 1
while 1:
    password = input("请输入密码：")
    if password != "123456":
        print("密码有误，请重试!")
        if number >= 3:
            print("输错密码超过三次，请明日重试")
            break
        number = number + 1
        continue
    if password == "123456":
        print("恭喜您，密码正确！")
        break
        
# 思考题二：
# 使用分支语句、循环语句和中断语句组合编写程序
# 从键盘输入用户名和密码，要求先判断用户名再判断密码，如果用户名不正确，则直接提示用户名输入有误，并让其重新输入；
# 如果用户名正确，则提示输入密码，进一步判断密码，如果密码不正确，则直接提示密码输入有误，并让其重新输入，如果密码正确，提示其进入。

while 1:
    username = input("请输入您的用户名：")
    if username == "admin":
        password = input("请输入您的密码：")
        while 1:
            if password == "123456":
                print("输入正确，恭喜进入！")
                break
            else:
                print("密码有误，请重试！")
                password = input("请输入您的密码：")
        break
    else:
        print("用户名有误，请重试！")
'''
