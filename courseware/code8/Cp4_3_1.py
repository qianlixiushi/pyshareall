#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cp4_3_1.py
# @Author: WRH
# @Date  : 2021/3/24
# @Edition:Python3.8.6

# 集合（set)
'''
集合（set）是不重复元素的无序集。
集合有类似字典的特点：
1.花括号“{}”来定义
2.集合中的元素是非序列类型的数据，也就是没有顺序，因此不支持索引、切片或其他类序列（sequence-like）的操作
3.集合中的元素不可重复,如有重复元素，将只保留一个
4.集合是可以修改的数据类型，但其中的元素必须是不变对象(字符、数字、元组)，类似于字典中的键。
5.集合和字典基本相同，唯一的区别，就是集合没有键和值的配对，是一系列无序的、唯一的元素组合
'''

# 1.集合的创建

# 使用{}赋值创建
# 例4-15 集合创建举例
s1 = {1, 2, 3, 4, 5}
print(s1)
s2 = {'a', 'b', 'c', 'c'}
print(s2)  # 集合中的元素不可重复,如有重复元素，将只保留一个
s3 = {'Python', (1, 2, 3)}
print(s3)
# 集合中的必须是不变对象(字符、数字、元组)，通过{}无法创建含有列表或字典元素的集合
#s4 = {"Python", [1, 2, 3]}
#s5 = {"Python", {'name': 'alice'}}
#print(s4, s5)

# 使用set()方法创建
# 创建空集合
s1 = set()  # 注意创建空集合要用set()而非{}，若用{}，将创建空字典
print(s1)
print(type(s1))
s2 = {}
print(type(s2))
# 由字符串创建
s3 = set('helloPython')  # 'helloPython'中包含两个'l'、两个'o'和两个'h'，
print(s3)  # 在s3中，'i'、'o'和'h'分别只有一个，即集合创建时自动保留重复字符中的一个。
# 由列表或元组创建
s4 = set([1, 'name', 2, 'age', 'hobby'])
print(s4)
s5 = set((1, 2, 3))
print(s5)

# 2.集合的修改
'''
集合对象的方法	        含义
set.add(x)	        向集合中添加元素x
set.update(a_set)	使用集合a_set更新原集合
set.pop()           删除并返回集合中的任意元素
set.remove(x)	    刪除集合中的元素x,如果x不存在则报错
set.discard(x)	    删除集合中的元素x,如果x不存在则什么也不做
set.clear()         清空集合中的所有元素
'''
a_set = {1, 2}
b_set = {'sisu'}
# 添加元素
a_set.add('python')
print(a_set)
# 添加集合
a_set.update(b_set)
print(a_set)
# 删除并返回集合中任意元素
a_set.pop()
print(a_set.pop())
print(a_set)
#print(a_set.pop('sisu')) # 不可指定要删除的元素
# 删除集合中指定的元素
a_set.remove('sisu')
print(a_set)
#a_set.remove('a') # 如果要删除的元素不存在，会报错
a_set.discard('a')  # 如果要删除的元素不存在，不进行任何操作
print(a_set)
# 清空集合中所有元素
a_set.clear()
print(a_set)

# 3.集合的数学运算
'''
Python符号	集合对象的方法	                含 义
s1 & s2	    s1.intersection(s2)	        返回s1与s2的交集，即s1和s2都有的元素
s1 | s2	    s1.union(s2)	            返回s1与s2的并集，即s1和s2所有元素，相同元素只保留一个
s1 - s2	    s1.difference(s2)	        返回s1与s2的差集，即s1独有的元素
s1 ^ s2	    s1.symmetric_difference(s2)	返回s1与s2的对称差，即s1和s2各自独有元素的合集
x in s1	                                测试x是否是s1的成员
x not in s1		                        测试x是否不是s1的成员
s1 <= s2	s1.issubset(s2)	            测试是否s1是s2的子集
s1 >= s2	s1.issuperset(s2)	        测试是否s1是s2的超集
            s1.isdisjoint(s2)	        测试s1和s2是否有交集,如果没有返回 True，否则返回 False。
s1|= s2	    s1.update(s2)	            用s2更新s1,添加s2中的元素到s1中，如果添加的元素在s1中已存在，则该元素只会出现一次
'''
# 例4-16 集合运算举例。
s1 = {'a', 'e', 'i', 'o', 'u'}
s2 = {'a', 'e', 'c', 'd', 'b'}
print(s1)
print(s2)
print(s1 & s2)  # 交集：s1和s2都有的元素,也可以使用方法输出，print(s1.intersection(s2))
print(s1 | s2)  # 并集：s1和s2所有元素，也可以使用方法输出，print(s1.union(s2))
print(s1 - s2)  # 差集:s1独有的元素，也可以使用方法输出，print(s1.difference(s2))
print(s1 ^ s2)  # 对称差集：s1和s2各自独有元素的合集，也可以使用方法输出，print(s1.symmetric_difference(s2))
print('a' in s1)
print('a' not in s1)
print(s1 <= s2)  # 测试s1是否是s2的子集,也可以使用方法输出，print(s1.issubset(s2))
print(s1 >= s2)  # 测试s1是否是s2的超集,也可以使用方法输出，print(s1.issuperset(s2))
print(s1.isdisjoint(s2)) # 测试s1和s2是否有交集,如果没有返回 True，否则返回 False。
s1.update(s2)  # 添加s2中的元素到s1中，如果添加的元素在s1中已存在，则该元素只会出现一次
print(s1)

# frozenset()方法创建不可修改的集合
# 由于集合中的元素只能是不可变数据类型，所以集合中不能有集合，但是frozenset()方法创建不可变的集合
# 例如：
f_set = {frozenset({1, 2, 3}), 'a'}
print(f_set)
f_dict = {frozenset({1, 2, 3}): 'frozenset', 'python': 3.8}
print(f_dict)

