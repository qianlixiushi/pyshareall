#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cp2_2_2.py
# @Author: WRH
# @Date  : 2021/1/29
# @Edition:Python3.8.6

# 字符串（string）类型
# 字符串（string）：由字符串组成的序列。

# 1.字符串界定符：字符串通常使用单引号'',双引号"",三引号''''''或""""""括起来,这些符号称为字符串界定符。
print('123abc')

x = "I'm OK !"  # 当字符串中含有'（单引号）时要使用"（双引号），同理当字符串中含有"（双引号）时要使用'（单引号）
y = '他对她说："你真好看！"'
print(x)
print(y)

z = '''我是一串很长的字符串balabala'''  # 三引号'''或"""也用于多行注释。
print(z)

# 2.转义符（\）和原始字符串,转义符用来表示特殊字符。
'''
\\ 反斜杠符号
\' 单引号
\" 双引号
\b 退格符
\n 换行符
\t 横向制表符(补齐4个字符位置的倍数）
'''

print('1\\2\'3\"4\n5\t67\b')

# 若让转义符不生效，有两种方式，一是在原始字符串前用r或R来定义原始字符串，另一个是每个转义符前再加一个转义符
print(r'1\\2\'3\"4\n5\t67\b')
print('\\n5\\t7')

# 3.Python内置的对字符串操作方法
'''
s.lower() 将s字符串中的字符全部转写为小写 
s.upper() 将s字符串中的字符全部转写为大写
s.strip('x') 将s字符串两端含有的x字符删除
s.split(sep='x') 将字符串s中被x分割的字符以列表形式输出
'sep'.join(iterable) 连接字符串数组。
                     将iterable(可迭代对象）的元素以指定的字符sep(分隔符)连接生成一个新的字符串
'''

print('aBc'.lower())
print('AbC'.upper())
print('-a-'.strip('-'))
print('a-b-c'.split(sep='-'))
print('-'.join('abc'))

# 4. len()函数输出字符串长度
print(len('abc'))

# 5. +连接两个字符串
print('abc' + '甲乙丙')

# 6. *可以让字符串多次重复并连接在一起
print('鬼畜' * 8)
