#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Cp4_2_1.py
# @Author: WRH
# @Date  : 2021/3/18
# @Edition:Python3.8.6

# 映射型组合数据类型——字典（dictionary）
'''
字典包含键（key）和值（value）映射的集合。一个键对应一个值。
这种一一对应的关联称为键值对（key-value pair) ，或称为项（item）。
简单地说，字典就是用花括号包裹的键值对的集合。
每个键值对用冒号:分隔，每对之间用逗号,分隔
d = {key1 : value1, key2 : value2 }
注意:键必须是唯一的，必须是不可变数据类型的，例如，字符串、数字或元组。值可以是任何数据类型。
另外，字典的数据是散列表，其中的键值对是无序的，键值对的顺序可以随机变化，所以每次遍历输出的顺序可能不同。
'''
# 1.创建字典
dict1 = {'jack': 20, 'rose': 18}
dict2 = {(1, 2): ['a', 'b'], (3, 4): ['c', 'd'], (5, 6): ['e', 'f']}
print(dict1)
print(dict2)
print(type(dict2))  # 输出dict2的数据类型
# 通过字典键值表创建字典，但键只能是字符串，且不能加引号
print(dict(name='allen', age='40'))
# 创建空字典
dict3 = {}
print(dict3)
# 使用dict()将列表或元组转换为字典
list1 = [('rose', 18), ('jack', 20)]
dict4 = dict(list1)
print(dict4)
# 字典中的键值对是无序的
dict1 = {'jack': 20, 'rose': 18}
dict4 = {'rose': 18, 'jack': 20}
print(dict1 == dict4)  # 字典中元素无序
# 对比列表，列表中元素有序
list1 = [('rose', 18), ('jack', 20)]
list2 = [('jack', 20), ('rose', 18)]
print(list1 == list2)

# 2.访问字典中的某个键值对的值
'''
要得到字典中某个键值对的值，可以使用dict[key]的形式得到
字典名[键名]
'''
dict1 = {'name': 'earth', 'port': 80}
print(dict1['port'])
# 若要检查字典dict中是否含有某个键key，可以使用in。例如：
print('name' in dict1)

# 3.添加、删除、更新字典中的某一项（键值对）
adict = {'name': 'earth', 'port': 80}
adict['age'] = 18  # 添加新键值对('age':18)
print(adict)

adict['name'] = 'moon'  # 更新键name的值
print(adict)

del adict['port']  # 删除键键值对('port': 80)
print(adict)

# 4.对字典的操作
'''
方法	                                含 义
dict.keys()                         返回包含字典所有key的列表
dict.values()                       返回包含字典所有value的列表
dict.items()                        返回包含所有(键:值)项的列表
dict.clear()                        删除字典中的所有项或元素，无返回值
dict.copy()                         返回字典浅复制副本
dict.get(key,default=None)	        返回字典中key对应的值，若key不存，则返回default的值,
                                    default默认为None,可自定义
dict.setdefault(key,default=None)   若字典中不存在key,将会添加键key并将值设为default值
                                    default默认为None,可自定义
dict.pop(key, default)              若字典中存在key，则删除并返回key对应的值;如果key不存在，
                                    且没有给出default值，则引发 KeyError异常
dict.update(adict)                  将字典adict中的项（键值对）添加到dict中
'''
# 返回字典所有的键、值和项
# dict.keys()、dict.values()、dict.items()这三个方法分别返回包含原字典中每项的键、值和项(键,值)的列表
d = {'name': 'alice', 'age': 19, 'sex': 'F'}
print(d.keys())
print(d.values())
print(d.items())
# 要遍历一个字典，只需要遍历它的键即可
for key in d.keys():
    print('key=%s, value=%s.' % (key, d[key]))
    # print(key, d[key]) # 非格式化符方式直接输出

# 字典清空
'''
用dict.clear()可清空原始字典中所有的元素。
对于两个相关联的字典对象x,y，若将x赋值为空字典，将不对y产生影响；
而用clear方法清空x，也将清空字典y中所有元素。例如：
'''
d1 = {'name': 'alice', 'age': 19, 'sex': 'F'}
d1.clear()
print(d1)

x = {'name': 'alice', 'age': 19, 'sex': 'F'}
y = x
x = {}  # 若将x赋值为空字典，将不对其关联字典y产生影响
print(x)
print(y)

x = {'name': 'alice', 'age': 19, 'sex': 'F'}
y = x
x.clear()  # 用clear()方法清空x，也将清空x关联字典y中所有元素
print(x)
print(y)

# 字典的浅复制与深复制
'''
直接赋值：其实就是对象的引用（别名）。（始终相互影响）
浅复制(copy)：拷贝父对象，不会拷贝对象的内部的子对象。（在父对象层级，相互完全独立；在子对象层级，始终相互影响）
深复制(deepcopy)： copy模块的deepcopy 方法，完全拷贝了父对象及其子对象。（相互完全独立）
'''
# 直接赋值，原字典和复制后的字典始终相互影响
d = {'a': [1, 2, 3], 'b': 2}
d_1 = d
d['c'] = 3  # 给字典d添加键值对'c':3（父对象层级）
d['a'].append(4)  # 给字典d中键'a'对应的值[1, 2, 3]（子对象层级）添加元素4
print(d)
print(d_1)

# 字典的浅复制，原字典和浅复制的字典：父对象层级相互完全独立；子对象层级始终相互影响
d = {'a': [1, 2, 3], 'b': 2}
d_2 = d.copy()
d['c'] = 3  # 给字典d添加键值对'c':3（父对象层级）
d['a'].append(4)  # 给字典d中键'a'对应的值[1, 2, 3]（子对象层级）添加元素4
print(d)
print(d_2)

# 字典的深复制,原字典和深复制的字典相互完全独立
import copy  # 使用深复制.deepcopy()方法要先导入copy库

d = {'a': [1, 2, 3], 'b': 2}
d_3 = copy.deepcopy(d)
d['c'] = 3  # 给字典d添加键值对'c':3（父对象层级）
d['a'].append(4)  # 给字典d中键'a'对应的值[1, 2, 3]（子对象层级）添加元素4
print(d)
print(d_3)

# 以键查值
'''
dict.get(key,default=None)方法可访问字典项的对应值。若使用get访问一个不存在的key，会得到None值。
还可以自定义默认值，替换None值。
'''
d = {}  # 创建空字典
print(d.get('name'))
print(d.get("name", '没有该键'))  # 自定义default值为 没有该键
d['name'] = 'Eric'  # 给字典d添加键值对name：'Eric'
print(d)
print(d.get('name'))

# 以键查值，不存在时自动添加所查键及其对应的default值,default值可自定义
'''
dict.setdefault(key, default=None)
setdefault()函数与get()类似, 如果键key不存在于字典中，将会添加键key并将值设为default值。
'''
d = {'q': 1, 'w': 2}
print(d.setdefault('w'))  # 查询键w的值
print(d.setdefault('e', '自动添加'))  # 查询键'e'的值，键'e'不存在自动添加键'e'及其对应的default值,default值默认为None
print(d)

# 移除键值对
# dict.pop(key, default)方法用来获得并返回对应给定键的值，然后将这个键值对从字典中移除。例如：
d = {'name': 'alice', 'age': 19, 'sex': 'F'}
print(d.pop('name'))  # 删除name键并返回其值alice
print(d)  # 键值对'name': 'alice'已从字典d中删除
print(d.pop('name', '没有该键'))  # 设置default值 没有该键

# 字典更新
'''
dict.update(adict)方法可以利用一个字典更新另一个字典。
提供的字典中的所有键值对均会被添加到旧字典中，若有相同的键则会进行覆盖
'''
d = {'name': 'alice', 'age': 19, 'sex': 'F'}
x = {'name': 'bob', 'phone': '12345678'}
d.update(x)
print(d)

# 例4-13 输入两个数字，并输入加减乘除运算符号，输出运算结果。若输入其他符号，则退出程序。
while True:  # 循环语句
    a = float(input('请输入第一个数字'))
    b = float(input('请输入第二个数字'))
    t = input('请输入运算符号(+-*/四选一），其他符号为退出程序')
    tup = ('+', '-', '*', '/')  # 元组
    if t not in tup:  # 如果输入的运算符号不在元组tup中
        break  # 退出整个循环
    dic = {'+': a + b, '-': a - b, '*': a * b, '/': a / b}  # 字典
    print('%s%s%s=%0.1f' % (a, t, b, dic.get(t)))  # get()函数，以键取值

# 例4-14 引入内置模块calendar，输入年、月、日，根据weekday(year,month,day)的返回值，
# 输出该日期是星期几。函数weekday()返回0～6分别对应星期一至星期日。
from calendar import *
# *表示这是导入了calendar模块的每个类，可以直接使用类，无需句点表示法，不推荐使用这种方法导入类
y = input('请输入年')
m = input('请输入月')
d = input('请输入日')
dic = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期日'}
if y.isdigit() and m.isdigit() and d.isdigit() and 1 <= int(m) <= 12 and 1 <= int(d) <= 31:
    #  isdigit()是字符串的一个方法，用来判断这个字符串是否是纯数字的字符串
    w = weekday(int(y), int(m), int(d))
    print('您输入的%s年%s月%s日是%s' % (y, m, d, dic[w]))
else:
    print('输入日期有误')
