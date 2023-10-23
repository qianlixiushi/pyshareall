#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp5_2_1.py
# @Author: WRH
# @Date  : 2021/4/12
# @Edition:Python3.8.6

# 5.3基于文件的数据分析
'''
基于文件的数据分析，通常是利用Python对文本文件操作的便利性，读取文本文件，并转换为相应的数据列表，
再利用循环结构实现统计分析。
'''
# split()函数详解
'''
split()是一个内置函数，用来对字符串进行分割，分割后的字符串以列表形式返回，该函数的语法是:
str.split(str="",num=string.count(str))[n]
字符串.split('分隔符', 分隔次数)[下标]
1.split()中没有参数，默认以所有的空字符作为分割条件全部分割，空字符包括空格、换行(\n)、制表符(\t)等
2.split()中有参数时，会以分隔符作为分割条件，按分隔次数把字符串进行分割，得到下标对应的字符串作为列表的元素返回
'''
# 举例split()中没有参数
s = 'p y t h o n'  # 字符串以空格分隔
s1 = s.split()
print(s1)
# 举例split()中有参数
s2 = 'p-y-t-h-o-n'  # 字符串以-分隔
s3 = s2.split('-')  # 设定分隔符为-
s4 = s2.split('-', 2)  # 设定分隔符为-，分隔2次
s5 = s2.split('-', 2)[-1]  # 设定分隔符为-，分隔2次，取下标为-1的元素
print(s3)
print(s4)
print(s5)

# 例5-7 根据考试成绩，统计学科等级水平。学生成绩原始数据查看score.txt文件。
# 编程要求：从score.txt文件中读取学生成绩数据，判定等级并写入level.txt文件中。
'''
学科等级水平统计标准如下：
（1）每门课达到85分，总分达到260分为优秀；
（2）生物和科学两门课都达到60分，总分达到180分为及格；
（3）其他为不及格。
'''

'''
程序实现方案一：
（1）读取文件score.txt数据到列表L中
列表L中的数据项对应着文件中的每条学生记录，通过循环语句遍历L，提取需要的考号和三门课的成绩，并存放在列表x中。
（2）判定学科等级
列表x包含4个数据项，x[0]为考号，x[1]、x[2]和x[3]分别为“程序设计”、“生物”和“科学”三门课的成绩，
需要转换为整数类型以便进行求和等数值运算。最后通过分支语句，将求得的等级结果存放在key变量中。
（3）将考号和等级结果按一定格式写入文件level.txt中。
代码如下：
'''
L = list(open('score.txt'))  # 使用快速列表方式读取score.txt文件，并赋值为L
#  print(L) # 在编程过程中，如果对数据类型和结构不明确，可以用print()将其打印出来，便于清晰直观的观察,下同
f = open('level.txt', 'w')  # 使用w模式创建level.txt文件并打开写入，并赋值为f
del L[0]  # 删除列表L中第0个元素，即score.txt文件中的第一行  (为标题内容，不是计算的对象）
for s in L:
    x = s.split()  # split()通过指定分隔符对字符串进行切片，分隔符默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
    #  print(x)
    #  print(len(x))
    for i in range(1, len(x)):
        x[i] = int(x[i])  # 将数据从字符转化成整数
    sum_num = x[1] + x[2] + x[3]
    if x[1] >= 85 and x[2] >= 85 and x[3] >= 85 and sum_num >= 260:
        key = '优秀'
    elif x[2] >= 60 and x[3] >= 60 and sum_num >= 180:
        key = '及格'
    else:
        key = '不及格'
    f.write('%s\t%s\n' % (x[0], key))
f.close()
# fr = open('level.txt')
# print(fr.read())

'''程序实现方案二：
方案一利用列表存放文件中的数据，需要占用额外的内存空间。
更优的处理方法是使用readline()语句读取文件score.txt中的学生记录，对每条记录，判定该学生考核等级，
并与考号合并写入文件level.txt中。若某次循环读到空行，则跳出循环，结束对文件的处理。
'''
s = open('score.txt')  # 使用默认r模式打开score.txt文件，并赋值为s
f = open('level.txt', 'w')  # 使用w模式创建level.txt文件并打开写入，并赋值为f
s.readline()  # 读取第一行标题，指针移到第二行开头，此语句避免标题行内容进入循环，引起错误
while True:
    x = s.readline().split()  # split()通过指定分隔符对字符串进行切片，分隔符默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等
    # print(x)
    if len(x) == 0:  # 如果已到达文件的末尾，f.readline()将返回一个空字符串（''），此语句避免末尾空列表进入判断语句引起错误
        break
    for i in range(1, len(x)):
        x[i] = int(x[i])
    sum = x[1] + x[2] + x[3]
    if x[1] >= 85 and x[2] >= 85 and x[3] >= 85 and sum >= 260:
        f.write('%s\t%s\n' % (x[0], '优秀'))
    elif x[2] >= 60 and x[3] >= 60 and sum >= 180:
        f.write('%s\t%s\n' % (x[0], '及格'))
    else:
        f.write('%s\t%s\n' % (x[0], '不及格'))
s.close()
f.close()
# fr = open('level.txt')
# print(fr.read())

# 例5-8
'''
"car_data.txt"文件是以英文逗号分隔的数据文本文件，
记录了某出租汽车公司部分车辆某日0：00~23：00的车辆位置，无标题行。对应列分别是时间、车牌号、北纬、东经。
因协助查找该日发生在北纬31.2222-31.2333，东经121.45-121.55区域内的案件，
编写程序，找到并打印位于该区域内该出租车公司的车辆信息
'''
min_n, min_e = 31.2222, 121.45  # 设置所要查找的区域经纬度
max_n, max_e = 31.2333, 121.55  # 设置所要查找的区域经纬度
LS = list(open('car_data.txt'))  # 使用快速列表方式读取car_data.txt文件，并赋值为LS
# print(LS)
car = []  # 设置一个空列表用于存储处理后的数据
for s in LS:
    carone = s[:-1].split(',')  # 切片取值索引为0到-1（不含）是为了去掉换行符\n
    # split()通过指定分隔符,对字符串进行切片
    # print(carone)
    car.append(carone)  # car列表变成了二维列表
# print(car)
# print(len(car))
print('在该区间出现的车辆有：')
for t in range(len(car)):
    if (min_n < float(car[t][2]) < max_n) and (min_e < float(car[t][3]) < max_e):
        # 二维列表索引，第t个列表中的第2个元素和第三个元素分别为维度和经度
        print('时间：%s\t车牌：%s\t北纬：%s,东经：%s' % (car[t][0], car[t][1], car[t][2], car[t][3]))
        # 二维列表索引，第t个列表中的第0、1、2、3个元素分别为时间、车牌、纬度、经度

