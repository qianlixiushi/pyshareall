#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test5_2.py
# @Author: WRH
# @Date  : 2022-5-5
# @Edition:Python3.8.6
f = open('../../code11/cp5_3_1/i_have_a_dream.txt')  # 使用open()打开i_have_a_dream.txt文本文件，创建一个文件对象并赋值为f
speech_text = f.read()  # 对文件对象f进行读取，并赋值为speech_text
# print(speech_text)
# print(type(speech_text))
f.close()  # 关闭文件对象f，虽然文件已关闭，但文件里的数据已经赋值为speech_text存放在内存中以便调用
speech = speech_text.lower().split()
# 使用lower()方法将字符串speech_text里的字符转为小写，并使用split()方法按空格分隔单词，将所有单词放到列表speech中
print(speech)
dic = {}  # 创建空列表dic
for word in speech:  # 对speech列表中的元素进行遍历
    if word not in dic:  # 如果遍历到的词语不在字典dic中
        dic[word] = 1  # 将遍历到的词语设置为键，值（该词语出现的次数）设置为1，将此键值对添加到字典dic中
    else:  # 如果遍历到的词语在字典dic中
        dic[word] += 1  # 更改键（遍历到的词语）对应的值（该词语出现的次数），其值在原基础上加1
print(dic)

swd = sorted(list(dic.items()), key=lambda tup: tup[1], reverse=True)
# items()方法返回字典的项（键值对）。list()方法以列表形式返回可遍历的(键, 值)元组数组
print(list(dic.items()))
# lambda构造匿名函数，以元组中索引为1是的元素(词语出现的次序)作为排序依据，即tup[1]
# reverse = True 表示降序排列，最后得到按照词语出现次数降序排列的(键, 值)元组的列表，赋值为swd
for kword, times in swd:  # 对列表swd中元组的元素依次遍历，并输出
    print(kword, times)
