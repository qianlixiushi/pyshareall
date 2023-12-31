 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp3_4_1.py
# @Author: WRH
# @Date  : 2021/2/7
# @Edition:Python3.8.6

# 循环结构
'''
# 相关专业术语理解
1、循环（loop），指的是在满足条件的情况下，重复执行同一段代码。比如，while语句。
2、迭代（iterate），指的是按照某种顺序逐个访问序列数据中的每一项。比如，for语句。
3、遍历（traversal），指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次。
4、递归（recursion），指的是一个函数不断调用自身的行为。
循环算是最基础的概念，凡是重复执行一段代码，都可以称之为循环。大部分的递归，遍历，迭代，都是循环
共同点：这些概念都表示“重复”的含义，彼此互相交叉。
在上下文清晰的情况下，不必做过于细致的区分。
'''

# while语句
'''
while循环结构书写格式

初始值
while 表达式:  #表达式的值为真
    语句块A	  #符合条件时执行的语句
else:         #可选项
    语句块B
'''

'''
while后面的表达式可以为单个对象
python中被判定为False的单个对象:
False
None
所有值为零的数:
a. 0（整数）
b. 0.0（浮点数）
c. 0L （长整数）
d. 0.0+0.0j （复数）
所有空序列：
“”（空字符串）
[] （空列表）
() （空元组）
{} ｛空字典｝
除了以上这些，其他的都判定为True
'''

time = 8  # 设置初始计次数为8
while time < 12:  # 和if语句一样，后面有冒号
    print('有效次数内')  # 和if语句一样，要缩进四个空格
    time = time + 1  # 对time进行再次赋值，也可用复合赋值运算符将此语句表示为time += 1
else:
    print('计次已满')

# while死循环
'''
while后面可以为任意数字，只要不是0，就是条件永远为真，等价于while True。
而while 0 等价于 while False。
'''
while 1:  # 此表达式恒为真，当表达式恒为真时，循环将一直执行下去，无法靠自身终止，从而产生死循环。
    print('我是一个死循环')

while 0:
    print('啥也没有')

# 例3-9
# 编写程序，统计并输出1～1000以内所有能够同时被3和7整除的数字个数

number = 1  # 设置待验证的数字初始值
count = 0  # 设置满足条件数字个数的初始值
while number <= 1000:
    if number % 3 == 0 and number % 7 == 0:  # while语句内嵌if语句
        #print(number) #此语句可输出能够同时被3和7整除的数字
        count = count+1  # 如果if语句下的条件满足，则满足条件数字个数加一。因为是在if语句下，所以要再次缩进。
    number = number+1  # 此语句在while语句下，只需要缩进一次
print('能够同时被3和7整除的数字个数为：', count)

