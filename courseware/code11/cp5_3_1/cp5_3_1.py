#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp5_3_1.py
# @Author: WRH
# @Date  : 2022-5-10
# @Edition:Python3.8.6

# 背景知识-自然语言处理(NLP，Natural Language Processing)
'''
1.自然语言处理(NLP，Natural Language Processing):研究人与计算机交互的语言问题的一门学科，
其终极目标是使计算机能够理解、分析、操作人类语言，从而实现更加智能化的自然语言交互。
它是语言信息处理的一个分支，是人工智能(AI, Artificial Intelligence)的核心课题之一。
NLP大致可以分为自然语言理解（NLU）和自然语言生成（NLG）两种，

2.NLP主要内容包括以下：
语音识别：将人的语音转换成可被计算机理解的文本形式。
语言理解：理解人类语言的含义，包括语法、词汇、语义和上下文。
机器翻译：将一种语言的文本自动转换成另一种语言的文本。
信息检索：在大量文本数据中查找相关信息。
文本分类：将文本数据分成不同的类别。
命名实体识别：从文本数据中识别出具有特定名称的实体，例如人名、地名、公司名等。
信息抽取：从文本数据中抽取出有用的信息，例如时间、地点、事件等。
情感分析：分析文本数据中的情感倾向，例如正面、负面或中立等。
文本生成：自动产生新的文本数据，例如文章、诗歌等。

3.不同的计算机语言（如Java/Python/Go)对于针对不同的自然语言(如中文、英语）有不同的工具库，
如TextBlob、NLTK、jieba、HanLP、snownlp、Jcseg、sego、FoolNLTK
使用Python语言可以对中文进行自然语言处理的常用工具库有jieba、snownlp、THULAC、NLPIR

4.ChatGPT全称Chat Generative Pre-trained Transformer，由OpenAI开发，是一种自然语言处理模型，
从领域上是属于自然语言处理。它使用了基于Transformer的神经网络架构，可以理解和生成自然语言文本。
ChatGPT的成功表明，预训练语言模型已经成为自然语言处理领域的主流技术之一
人工智能：为机器赋予人的智能
机器学习：一种实现人工智能的方法
深度学习：一种实现机器学习的技术
神经网络：一种机器学习的算法
'''

# 5.3.2词频分析
# sorted()函数用法
'''
sorted()函数对所有可迭代的对象(字符串、列表、元组、字典、集合)进行排序操作，返回重新排序后的列表
语法
sorted(iterable, key=None, reverse=False)
iterable – 可迭代对象。
key – 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse – 排序规则：reverse = True 降序，reverse = False 升序(默认)。
'''
s = 'python'  # 字符串
s1 = sorted(s)
print(s1)

lst = [1, 2, 3]  # 列表
lst1 = sorted(lst)
print(lst1)

tup = (1, 2, 3)  # 元组
tup1 = sorted(tup)
print(tup1)

dic = {'a': 1, 'b': 2, 'c': 3}  # 字典
dic1 = sorted(dic.items())
print(dic1)

set1 = {'a', 'b', 'c'}  # 集合
set2 = sorted(set1)
print(set2)

# sort与sorted的区别
'''
1.sort是应用在列表上的方法，sorted可以对所有可迭代的对象进行排序操作。
2.list的sort方法返回的是对已存在的列表操作后的结果，而内建函数sorted方法返回的是一个新的list，
   而不是在原来的基础上进行的操作。
语法
sorted语法：sorted(iterable,key=None,reverse=False)
sort语法：sort(key=None,reverse=False)
参数说明：
iterable--可迭代的对象
key--取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序，可省略不写
reverse--排序规则，reverse=True降序，reverse=False升序(默认)，省略不写默认升序
'''
lst = [1, 2, 3]
lst1 = sorted(lst)  # 列表sorted()函数
print(lst1)

lst = [1, 2, 3]
lst.sort(reverse=True)  # list.sort方法
print(lst)

# 例5-9 统计著名黑人领袖马丁·路德金演讲“I Have a Dream”的词汇出现频次。
'''
编程思想:读取文本文件，用lower()方法将所有字符转为小写并用split()方法按空格分隔单词，将所有单词放在列表speech中。
定义一个空字典dic，用循环结构遍历列表speech，将单词作为字典的键，统计每个单词出现的次数，作为字典的值。
'''
f = open('i_have_a_dream.txt')  # 使用open()打开i_have_a_dream.txt文本文件，创建一个文件对象并赋值为f
speech_text = f.read()  # 对文件对象f进行读取，并赋值为speech_text
# print(speech_text)
# print(type(speech_text))
f.close()  # 关闭文件对象f，虽然文件已关闭，但文件里的数据已经赋值为speech_text存放在内存中以便调用
speech = speech_text.lower().split()
# 使用lower()方法将字符串speech_text里的字符转为小写，并使用split()方法按空格分隔单词，将所有单词放到列表speech中
# print(speech)
dic = {}  # 创建空列表dic
for word in speech:  # 对speech列表中的元素进行遍历
    if word not in dic:  # 如果遍历到的词语不在字典dic中
        dic[word] = 1  # 将遍历到的词语设置为键，值（该词语出现的次数）设置为1，将此键值对添加到字典dic中
    else:  # 如果遍历到的词语在字典dic中
        dic[word] += 1  # 更改键（遍历到的词语）对应的值（该词语出现的次数），其值在原基础上加1
# print(dic)
swd = sorted(list(dic.items()), key=lambda tup: tup[1], reverse=True)
# items()方法返回字典的项（键值对）。list()方法以列表形式返回可遍历的(键, 值)元组数组
# print(list(dic.items()))
# lambda构造匿名函数，以元组中索引为1是的元素(词语出现的次序)作为排序依据，即tup[1]
# reverse = True 表示降序排列，最后得到按照词语出现次数降序排列的(键, 值)元组的列表，赋值为swd
# print(swd)
for kword, times in swd:  # 对列表swd中元组的元素依次遍历，并输出
    print(kword, times)

# 去除停用词
'''
在例5-9中，the等虚词出现的频率很高，但在实际运用中，统计这种词的出现频率意义不大，所以我们可以讲这些
不参加统计的词（停用词，stop_words)以列表结构形成文本文件，在编写代码输出结果时添加条件，
将不含停用词的词频结果输出出来。
'''
f = open('i_have_a_dream.txt')
speech_text = f.read()
f.close()
speech = speech_text.lower().split()
dic = {}
for word in speech:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1
swd = sorted(list(dic.items()), key=lambda tup: tup[1], reverse=True)
f1 = open('stop_word_list.txt')  # 打开停用词文本文件
stop_wds = f1.read()  # 对文件对象f进行读取，并赋值为stop_wds
f1.close()
for kword, times in swd:
    if kword not in stop_wds:  # 判断统计词频的词是否在停用词文件中，如果不在，输出结果
        print(kword, times)
        # f2 = open('kword_ihaveadream.txt', 'a+')
        # f2.write(kword + ' ' + str(times) + '\n')
        # f2.close()

# 5.3.3第三方库jieba和中文词频分析
# jieba库
'''
英文词汇之间有天然的空格分隔，而中文之间没有，而且中文随着字词长短的变化，不同组合语义差别很大，要对中文进行词频分析，
首先要解决词汇的分割问题，而Python的第三方库jieba是一个用于中文词汇分割的函数库，可用于中文句子/词性分割、词性标注、
未登录词识别，支持用户词典等功能，该库的分词精度达到了97%以上。注意：待分词的字符串可以是gbk字符串、utf-8字符串
（一）支持三种分词模式：
1、 精确模式，试图将句子最精确地切开，适合文本分析，冗余度较低；
2、 全模式，把句子中所有的可以成词的词语都扫描出来，速度非常快，但是不能解决歧义，冗余度最高；
3、 搜索引擎模式，在精确模式的基础上，对长词再次切分，提高召回率。适合用于搜索引擎分词，冗余度最高。
（二）支持繁体分词
（三）支持自定义分词
（四）MIT授权协议（一种开源软件许可协议）
'''
# 三种分词函数
import jieba  # 导入jieba库
s = "jieba是常用的中文分词函数库"
print(jieba.lcut(s))  # 精确模式jieba.lcut(str)返回列表类型
print(jieba.lcut(s, cut_all=True))  # 全模式jieba.lcut(str,cut_all=True)返回列表类型，有冗余
print(jieba.lcut_for_search(s))  # 搜索引擎模式：jieba.lcut_for_search(str)返回列表类型，有冗余

# 例5-10 统计朱自清散文《荷塘月色》的词汇出现频次
import jieba   # 导入jieba第三方库
f = open('../../code12/cp5_4_1/荷塘月色.txt')  # 使用open()打开i荷塘月色.txt文本文件，创建一个文件对象并赋值为f
article_text = f.read()  # 对文件对象f进行读取，并赋值为speech_text
f.close()  # 关闭文件对象f，虽然文件已关闭，但文件里的数据已经赋值为speech_text存放在内存中以便调用
article = jieba.lcut(article_text)  # 运用jieba.lcut()方法将字符串中的中文词汇分割，返回词汇列表
# print(article)
dic = {}  # 创建空列表dic
for word in article:  # 对article列表中的元素进行遍历
    if word not in dic:  # 如果遍历到的词语不在字典dic中
        dic[word] = 1  # 将遍历到的词语设置为键，值（该词语出现的次数）设置为1，将此键值对添加到字典dic中
    else:  # 如果遍历到的词语在字典dic中
        dic[word] += 1  # 更改键（遍历到的词语）对应的值（该词语出现的次数），其值在原基础上加1
swd = sorted(list(dic.items()), key=lambda tup: tup[1], reverse=True)
# print(swd)
# items()方法返回字典的项（键值对）。list()方法以列表形式返回可遍历的(键, 值)元组数组
# lambda构造匿名函数，以元组中索引为1是的元素(词语出现的次序)作为排序依据，即tup[1]
# reverse = True 表示降序排列，最后得到按照词语出现次数降序排列的(键, 值)元组的列表，赋值为swd
f1 = open('中文虚词列表.txt')  # 打开中文虚词列表
stop_wds = f1.read()
# print(stop_wds)
f1.close()
for kword, times in swd:  # 判断统计词频的词是否在中文虚词列表文件中，如果不在，输出结果
    if kword not in stop_wds:
        print(kword, times)

