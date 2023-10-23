#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cp5_4_1.py
# @Author: WRH
# @Date  : 2023-10-17
# @Edition:Python3.8.6
# 5.3.4 词语可视化和第三方库wordcloud
'''
Python的第三方库wordcloud是一种能将词语渲染成大小、颜色不一的可视化呈现形式“词云”的函数库。其效果能将枯燥呆板的文字
以直观的艺术效果展示出来。创建词云时，先引用第三方库wordcloud，将其核心类WordCloud实例化为词云对象，

实例化对象的常用参数有：
background_color		词云背景色，默认为黑
width,height			宽和高（像素）
font_path				字体文件的路径
max_font_size			最大字号
max_words			    最多容纳词汇数，默认200

词云对象有两个方法：genaerate()和to_file()，功能分别是将文本生成词云和将词云保存为图片
'''
# 英文实例：
import wordcloud  # 导入wordcloud库
txt = "life is short,you need python"  # 将要处理的文本赋值给txt
w = wordcloud.WordCloud()  # 实例化词云对象
w.generate(txt)  # 将文本生成词云
w.to_file("python_e.png")  # 保存词云，如果要保存在别的文件夹要写好路径如'D:\\Pythonlesson\\Chapter5\\python_e.png'

# 中文实例：（中文需要jieba库先进行分词才行）
import wordcloud
import jieba
txt = "人生苦短，我用Python"
w = wordcloud.WordCloud(font_path="msyh.ttc",)  # 需指定字体msyh.ttc（微软雅黑），因为默认字体不支持显示中文
w.generate(" ".join(jieba.lcut(txt)))  # .join()方法：语法'sep'.join(iterable) 连接字符串数组。
                                        # 将iterable(可迭代对象）的元素以指定的字符sep(分隔符)连接生成一个新的字符串
w.to_file("python_c.png")

# 例5-11 将朱自清散文《荷塘月色》的词汇出现频次结果生成词云图
import wordcloud
import jieba  # 导入jieba第三方库
f = open('荷塘月色.txt')
article_text = f.read()
# print(article_text)
f.close()
article = jieba.lcut(article_text)  # 运用jieba.lcut()方法将字符串中的中文词汇分割，返回词汇列表
# print(article)
text = ''
for i in article:
    text = text+str(i)+' '  # 将列表中的词汇遍历并以空格分隔保存到text字符串中
# 以上三行语句可简写为：text = ' '.join(article)
# print(text)
w = wordcloud.WordCloud(background_color='white',
                      width=400,
                      height=300,
                      max_font_size=48,
                      font_path='C:/Windows/Fonts/simhei.ttf')  # 实例化词云对象
w.generate(text)  # 将文本生成词云
w.to_file('D:\\Pythonlesson\\Chapter5\\cp5_3_1\\荷塘月色云词图.png')  # 保存词云