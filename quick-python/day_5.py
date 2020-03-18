#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Created Time : 五  3/13 20:53:21 2020
# File Name: day_5.py
# Description:
"""

class AssignValue(object):
    def __init__(self, value):
        self.value = value
        self.name = 'AssignValue'

my_value = AssignValue(6)
print("value = {0.value} ,name = {0.name}".format(my_value))
print("{:.2f}".format(3.141592653)) # 3.14

para_str = """这是一个多行实例
多行字符串可以使用制表符
TAB( \t )
也可以使用换行符( \n )
"""
print(para_str)

name = 'world'
str_1 = f'Hello {name}' #Hello world
print(str_1)
print(f'{1 + 2}') # 3
w = {'name': 'BaiDu', 'url': 'www.baidu.com'}
str_2 = f'{w["name"]}: {w["url"]}'
print(str_2) #BaiDu: www.baidu.com
x = 1
print(f'{x + 1}') # python 3.6 =>2
#print(f'{x + 1=}') # python 3.8 => x + 1 = 2


str_1 = 'this is string example about capitalize.'
print(str_1.capitalize())#This is string example about capitalize.

str_1 = 'hello'
print(str_1.center(40, '*'))#*****************hello******************

str_1 = 'hello,hellopython hello hello he'
print(str_1.count('hell')) #4
print(str_1.count('hell', 7)) #2
print(str_1.count('hell', 7, 25)) #1

str_1 = 'Baidu'
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str_1)
print(f'utf8=>{str_utf8}')
print(f'gbg=>{str_gbk}')
print(f'utf8 decode:{str_utf8.decode("UTF-8","strict")}')
print(f'gbk decode:{str_gbk.decode("GBK", "strict")}')

str_1 = 'Baidu example ...wow!!!'
suffix = '!!'
print(str_1.endswith(suffix))
print(str_1.endswith(suffix, 20))

str_1 = "this is\tstring example...wow"
print(str_1)
print(str_1.expandtabs(18))
print(str_1.expandtabs(40))

str_1 = 'this is string example'
print(str_1.find('is')) # 2
print(str_1.index('is'))
#print(str_1.index('goo')) # error

str_1 = 'abc1ad'
print('Test isalnum'.center(30,'*'))
print(str_1.isalnum()) # True
print('abc'.isalnum()) # True
print('!@#$'.isalnum()) # False
print(''.isalnum()) # False
print(str_1.isalpha()) # False
print('abcd'.isalpha()) # True

