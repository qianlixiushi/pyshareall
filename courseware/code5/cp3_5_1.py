#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_5_1.py
# @Author: WRH
# @Date  : 2021/3/7
# @Edition:Python3.8.6

# 程序调试

'''
1.语法错误:指程序代码不符合解释器语法规则，导致程序无法正常运行
编译器就会以醒目的形式报错，含有语法错误的语句是不能通过编译

2.逻辑错误:指程序代码符合语法规定，但是由于算法、运行环境等问题不能得到预期的计算结果
逻辑错误往往能够通过编译因而难以被直接发现，需要通过人工或调试工具跟踪执行过程来排查
'''

# 常见的语法错误和逻辑错误

# 1.对象名称错误
name = "张三"
print(Name)  # 变量名首字母大写

# 2.语法符号的错漏
for cNum in "Python"  # 缺少冒号
    print(cNum)

# 3.误将关键字作为对象名称（回想第一节课的内容，变量名的命名规则）
# 获取关键字的方法
import keyword
print(keyword.kwlist)
False = 'a'

# 4.赋值运算符=与比较运算符==的误用

# 5.缩进错误
import math
if math.pi>3:
print('yes') # 开头没有缩进

# 6.索引错误
name = "张三" # 索引从0开始，张对应0，三对应1.
print(name[2])  # 输出变量name的第三个字符，不存在此索引值的字符

# 7.映射错误（第四章讲述）

# 8.类型错误
age = 18
name = "张三"
merge= name + "今年" + age +"岁" # age变量应使用str()函数进行转化
print(merge)

# 9.模块引入错误
import Calendar # 日历模块的名称是calendar,首字母小写

# 10.算术错误
num1 = 15
num2 = 0 # 除数不能为0
print(num1/num2)

# 11.操作系统错误
fobj = open('test.txt','r')  #文件不存在
for line in fobj:
    print(line)
fobj.close()

# 12.属性错误
s = 'ABCDE'
s = s.lowerr() # 应为lower()
print(s)

# 排除程序错误的方法
# 1.程序中使用print()函数，输入中间值进行调试
# 2.跟踪调试





