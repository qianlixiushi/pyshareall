#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp5_1_1.py
# @Author: WRH
# @Date  : 2021/4/7
# @Edition:Python3.8.6

# 第5章：文件与基于文件的数据分析
# 5.1文件的基本概念

# 1.文件和目录
'''
文件是存储在外部介质上的数据集合，通常可以长久保存，也称为磁盘文件
文件是通过目录来组织和管理的，目录提供了指向对应磁盘空间的路径地址
目录一般采用树状结构，在这种结构中，每个磁盘有一个根目录，它包含若干文件和子目录。
'''

# 2.绝对路径与相对路径
'''
绝对路径：从根目录开始标识文件所在完整路径的方式成为绝对路径，任何程序想要对这一文件进行操作都可以使用此路径。
相对路径：相对于程序所在的目录位置建立其引用文件所在的路径，这时保存在不同目录下的程序引用这一文件时所使用的路径不相同。
        文件与程序所在的相同的目录省略
绝对路径的获取方法（以win10为例）：
（在pycharm界面，在文件上面右键选择 Show in Explore 可以打开文件所在的文件夹）
方法一：找到文件所在的文件夹，单击选中文件，按住shift键的同时右键单击选择“复制文件地址”
方法二：找到文件所在的文件夹，鼠标放在顶部地址栏，右键选择”复制地址“，然后在复制的地址后面补上文件名（包括后缀）
'''

# 例5-1 绝对路径示例。
'''
绝对路径是由磁盘驱动器、目录层次和文件名三部分组成的，
文件workfile1.txt保存在C:盘myproject的子目录cp5_1_1目录下，
即"C:\myproject\cp5_1_1\workfile1.txt"，
为避免遇到转义符(比如\n)引起路径错误，在Python中用字符串表示为：
"C:\\myproject\\cp5_1_1\\workfile1.txt"   (\\为反斜杠/)
或
"C:/myproject/cp5_1_1/workfile1.txt" # 用一个/代替\\
'''
# 例5-2 相对路径示例。
'''
相对路径书写原则：要读取文件的程序和文件所在的相同目录层级可省略不写

文件workfile1.txt保存在C:盘myproject的子目录cp5_1_1目录下：
1.如果程序test5_1.py要读取文件workfile1.txt，那么相对路径可表示为"workfile1.txt"
因为程序test5_1.py也保存在C:盘myproject的子目录cp5_1_1目录下，
相同的目录层级C:\\myproject\\cp5_1_1可省略；

2.如果程序test5_2.py要读取文件workfile1.txt，那么相对路径可表示为"..\\cp5_1_1\\workfile1.txt"
（..\\表示上一级目录）详情参考https://blog.csdn.net/weixin_63986098/article/details/123808947
因为程序test5_2.py保存在C:盘myproject的子目录cp5_2_1下，
与文件workfile1.txt相同的目录层级C:\\myproject可省略。
'''

# 3.文件的编码与解码
'''
a.数据在计算机上的存储方式是二进制的，即由0和1组成，而我们通常采用两种方式对其解读，一种是基于字符编码，一种是基于值编码。
  如果某文件的数据使用基于字符的编码，那么该文件为“文本文件”，这种文件通常具有可读性，例如txt文件；
  如果某文件的数据使用基于值的编码，那么该文件为“二进制文件”，这种文件通常无法直接读懂，例如可执行程序、图形图像、声音等等
b.文本文件可以用win10记事本打开并选择编码方式保存，使用“另存为”命令，在打开的对话框中，
  点击编码旁边的倒三角符号可以选择ANSI、UTF-8等编码方式进行保存
c.文本文件常用的编码:
在计算机系统中，所有的数据都以二进制存储，所有的运算也以二进制表示，人类语言和符号也需要转化成二进制的形式，
才能存储在计算机中，于是需要有一个从人类语言到二进制编码的映射表。这个映射表就叫做字符集。最早的字符集是ASCII。
最全的字符集是Unicode，又叫万国码，可以容纳全世界所有的语言文字吗，每个字符都有唯一的编码。
ASCII (American Standard Code for Information Interchange): 
美国信息交换标准码，是一种定长编码，编码规则为：1字节 0xxxxxxx (8位)
ANSI：ASCII的扩展版
Utf-8(8-bit Unicode Transformation Format)：
针对Unicode字符集的一种可变长度字符编码规则。它可以用来表示Unicode标准中的任何字符，
而且其编码中的第一个字节仍与ASCII相容，使得原来处理ASCII字符的软件无须或只进行少部份修改后，便可继续使用，
编码规则可以有1-4个字节
GBK：纯中文编码规则，是一种双字节编码格式，优点是节省空间，缺点是不支持其他语言字符，容易出现乱码
d.解码与编码
解码：是把字节流（bytes）转换成字符串,简单的来说：解码就是把字节流转化成人看的懂得文字
编码：是把字符串转换成字节流（bytes），简单的来说：编码就是把人看的懂得文字转化成字节流
'''

# 例5-3 编码与解码示例
s1 = '我发誓学好python'
print(type(s1))
print(s1)

s2 = s1.encode('utf-8')  # 将字符串s1使用utf-8编码格式编码为字节流（bytes）
print(type(s2))
print(s2)
# 将字符串转换成字节流（bytes）对象时，对于非ASCII字符，print输出的是它的字符编码值（十六进制形式），而不是字符本身。

s3 = s2.decode('utf-8')  # 将字节流（bytes）s2使用utf-8编码格式解码为字符串
print(type(s3))
print(s3)

# 5.2文件的操作
'''
程序中对文件的操作一般包括：
打开文件
读取文件
对文件数据进行处理
写入文件
关闭文件

python文本文件的信息项是字符，二进制文件的信息项是字节。
'''

# 1.文件的打开与关闭
'''
文件的打开方法：文件对象 = open(文件名, 模式, encoding='编码', errors='ignore')
文件的关闭方法：文件对象.close()
open()方法返回了一个文件对象，括号中通常包含四个字符串类型参数：文件名、模式、编码方式、错误忽略
文件名是程序需要操作文件的完整物理文件名
编码即采用何种编码进行转化，可省略
错误即忽略错误直接打开文件，可省略
模式表示文件的使用方式，可以省略，省略时默认为r模式，常用的模式具体如下：

模式	含义
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
x	写模式，新建一个文件，如果该文件已存在则会报错FileExistsError。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。
    如果该文件不存在，创建新文件进行写入。
b	表示二进制模式，添加在其他控制字符后。
t	文本模式 (默认，一般省略不写)。
+	打开一个文件进行更新(可读可写)，添加在其他控制字符后。

rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。

wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，
    即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
    如果该文件不存在，创建新文件。一般用于非文本文件如图片等。

ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
    也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。
    如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
'''
# 例5-4 打开与关闭文件示例
# 第一种方法，使用os模块切换到程序所要操作的文件所在的目录进行打开与关闭
import os  # 导入python内置模块os,此模块用于处理文件和目录
os.chdir('C:\\myproject\\cp5_1_1')  # chdir为change directory的缩写
# os.chdir(path)函数：改变当前工作目录，path内容为所要操作文件所在的目录
f = open('workfile1.txt', 'r')
# 使用open()方法以只读方式打开workfile1文件，返回一个文件对象并赋值为f。
f.close()  # 关闭文件

# 第二种方法，直接使用绝对路径进行打开与关闭(推荐)
f = open('C:\\myproject\\cp5_1_1\\workfile1.txt', 'r')
f.close()

# 第三种方法，当且仅当程序和程序要操作的文件在同一文件夹，可直接对文件进行打开与关闭
f = open('workfile1.txt', 'r')
f.close()

# 2.对文件内容进行定位操作
'''
通过open()方法创建了一个文件对象后，读/写指针会定位在文件的头部，即最左边的开始位置，然后文件中的信息将按照
从左到右的顺序被访问，这称为顺序存取。如果要对文件中的自定义位置进行随机读/写，可以使用seek()方法。
seek()方法格式如下：
f.seek(偏移值, 起始位置)
偏移值：表示从起始位置再移动一定量的距离，偏移值为正数表示向右（即文件尾部方向）移动为负数表示向左（即文件头部方向）移动。
       当起始位置为1或2时，只有二进制模式可以指定非0的偏移值。偏移值的单位是字节（Byte）。
起始位置：为0表示自文件起始处开始（默认值，当有偏移值时可省略），1表示从当前文件指针位置开始，2表示从文件末尾开始。
'''
# 例5-5 随机访问文本文件示例。
f = open('C:\\myproject\\cp5_1_1\\workfile1.txt', 'r+')
# r+ 打开一个文件用于读写。文件指针将会放在文件的开头。
f.write('我发誓要好好学Python')  # 将字符串'我发誓要好好学Python'写到对象f对应的文件workfile1.txt中
f.seek(8)  # 指针从文件开始位置向右偏移8个字节，根据编码格式，这里每两个字节对应一个中文字符。
print(f.read(9))  # 从指针位置向右开始读取9个字符内容并输出
f.close()  # 关闭文件

# 例5-6 随机访问二进制文件示例。
f = open('C:\\myproject\\cp5_1_1\\workfile2.txt', 'rb+')
# rb+ 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
f.write(b'I like Python !')  # f.write()方法将字符串string(或字节流bytes)的内容写到对象f对应的文件中
print(f.seek(2))  # 指针从文件开始位置向右偏移2个字节，并输出指针所在位置
print(f.read(4))  # 从指针位置向右开始读取4个字节内容并输出
print(f.seek(-8, 2))  # 指针从文件末尾位置向左偏移8个字节，并输出指针所在位置
print(f.read(6))  # 从指针位置向右开始读取6个字节内容并输出
f.close()  # 关闭文件

# 3.文件的读取、写入、追加

# 读取
# f.read(size)方法
'''
该方法返回一个字符串，内容为长度为size的文本。数字类型参数size表示读取的字符数，可以省略。
如果省略size参数，则表示读取文件所有内容并返回。如果指针已到达文件的末尾，f.read()将返回一个空字符串（''）
'''
f = open('C:\\myproject\\cp5_1_1\\workfile3.txt', 'r', encoding='utf-8')
# 国内Windows10系统下默认使用gbk（《汉字内码扩展规范》）编码，如果文件内容含有中文或某些特殊字符，
# 对文件进行更改时会报UnicodeDecodeError（编码错误），这里添加encoding = 'utf-8'进行更改编码
print(f.read())  # 输出文件全部内容，两行字符，一行空格
print(f.read())  # 指针到达文件末尾，输出空字符''

# f.readline()方法
'''
该方法返回一个字符串，内容为文件的当前一行。换行符（\n）留在字符串的末尾。
如果已到达文件的末尾，f.readline()将返回一个空字符串（''）。如果是一个空行，则返回'\n'
'''
f.seek(0)  # 指针回到文件开始处
print(f.readline())  # 输出第一行
print(f.readline())  # 输出第二行
print(f.readline())  # 输出第三行，第三行是空行

# 从文件中读取行，更高效的是在文件对象上循环
f.seek(0)
for line in f:
    print(line)

# f.readlines()方法
'''该方法返回一个列表，列表中的每个字符串类型元素对应文件的每行（包括结尾的换行符“\n”）'''
f.seek(0)
print(f.readlines())  # 输出全部内容，指针到达末尾
print(f.readlines())  # 指针在末尾，后面没有内容，输出空列表
f.close()

# 快速列表读取：列表 = list(open(文件名, 模式, 编码, 错误忽略))
L = list(open('C:\\myproject\\cp5_1_1\\workfile3.txt', 'r', encoding='utf-8'))
print(L)

# 写入
# f.write(string)方法
'''
将字符串string的内容写到f对应的文件中，并返回写入的字符数。
但write语句不会自动换行，如果需要换行，则要使用换行符\n。
\n代表一个字符。以w模式打开的文件的原有内容将被覆盖，如果文件不存在将创建此文件。
'''
f = open('C:\\myproject\\cp5_1_1\\workfile4.txt', 'w', encoding='utf-8')
# w模式，打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
f.write('人生苦短\n')
f.seek(0)

# 追加
f = open('C:\\myproject\\cp5_1_1\\workfile4.txt', 'a', encoding='utf-8')
# 以a模式打开文件，指针会移到末尾处，写入的内容将追加到该文件的末尾
f.write('我用Python！\n')
#f.seek(0)
#print(f.read())
f.close()
