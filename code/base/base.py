#!/usr/bing/python
# -*- coding: UTF-8 -*-
a = 0
b = 1
c = 2
# 多行语句
d = a + \
    b + \
    c
# 不换行输出
print a,
print b, 
print c,
print d
# 字符串
s1 = 'world'
s2 = "this is a string"
# 三个双/单引号表示多行
s3 = """
this
is
a 
string
"""
print s1
print s2
print s3
# 单行注释
''' 这是
多行注释
'''
""" 这是
多行注释
"""
# 等待用户输入
raw_input("按下 enter 键退出， 其他任意键显示...\n")
# 同一行有多条语句需要用;分开
import sys; x = 'base.py'; sys.stdout.write(x + '\n')
