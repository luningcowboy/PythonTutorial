#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Created Time : 四  3/12 12:26:48 2020
# File Name: day_4.py
# Description:
"""

str1 = 'Hello World'
str2 = 'Python'
print("str1[0]:", str1[0])
print("str2[1:5]:", str2[1:5])

str1 = 'Hello World'
print('新字符串:', str1[:6] + 'AABBCC')

a = 'Hello'
b = 'Python'
print('a + b :', a + b)
print('a * 2 :', a * 2)
print('a[1]:', a[1])
print('a[1:4]', a[1:4])
if 'H' in a :
    print('H in a')
else:
    print('H not in a')
if 'M' not in a:
    print('M not in a')
else:
    print('M in a')

print(r'\n')
print(R'\n')

print('我叫 %s 今年 %d 岁!'%('小明', 10))

print("{} {}".format('hello', 'world'))
print("{0} {1}".format('hello', 'world'))
print("{0} {1} {0}".format('hello', 'world'))
print("NAME:{name},URL:{url}".format(name='百度', url='www.baidu.com'))
site = {"name": '百度', "url": 'www.baidu.com'}
print("Name: {name}, URL: {url}".format(**site))
my_list = ['百度', 'www.baidu.com']
print('Name: {0[0]}, URL: {0[1]}'.format(my_list)) # 0是必须的
