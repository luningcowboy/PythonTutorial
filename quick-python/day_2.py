#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Created Time : 二  3/10 12:38:42 2020
# File Name: day_2.py
# Description:
"""
tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple1)
print(tuple1[0])
print(tuple1[1:3])
print(tuple1[2:])
print(tuple1 * 2)
print(tuple1 + tinytuple)

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
if 'Rose' in student:
    print('Roese 在集合中')
else:
    print('Rose 不在集合中')
a = set('abcdefghijklmn')
b = set('abacdefad')

print(a)
print(a - b) # a 和 b 的差集
print(a | b) # 并集
print(a & b) # 交集
print(a ^ b) # 不同时存在的元素

dict1 = {}
dict1['one'] = '1 - 菜鸟教程'
dict1[2] = '2 - 菜鸟工具'

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict1['one'])
print(dict1[2])
print(dict1.keys())
print(dict1.values())
print(tinydict)
print(tinydict.keys())
print(tinydict.values())

print(int())
print(int(3))
print(int(3.6))
print(int('12', 16))
print(int('0xa', 16))
print(int('10', 8))

print(float(1))
print(float())
print(float('123'))
print(float(-123.4))

print(complex(1, 2))
print(complex(1))
print(complex('1'))
print(complex("1+2j"))# 不能加空格

s = 'RUNOOB'
print(str(s))
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'}
print(str(dict1))

s = 'RUNOOB'
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'}
print(repr(s))
print(repr(dict1))

x = 7
print(eval('3*x'))
print(eval('pow(2,2)'))
print(eval('2 + 2'))
n = 81
print(eval('n + 4'))

list1 = ['Google', 'Taobao', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)


aTuple = (123, 'Google', 'Baidu', 'Taobao')
list1 = list(aTuple)
print(list1)
s = 'abcdeft'
list2 = list(s)
print(list2)

x = set('runoob')
y = set('google')
print((x, y)) # 重复的元素被删除
print(x & y) # 交集
print(x | y) # 并集
print(x - y) # 差集
print(y)

print(dict())
print(dict(a = 'a', b= 'c', c = 1, d = 2))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(dict([('one', 1), ('two', 2), ('three', 3)]))

a = frozenset(range(10))
print(a)
b = frozenset('runoob')
print(b)

print(chr(0x30), chr(0x31), chr(0x61))
print(chr(48), chr(49), chr(97))

print(ord('a'))
print(ord('b'))
print(ord('c'))

print(hex(255))
print(hex(-42))
print(hex(12))
print(type(hex(12)))


print(oct(10))
print(oct(20))
print(oct(15))
print(type(oct(15)))

a = 21
b = 10
c = 0
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

a = 21
b = 10
c = 0
if (a == b):
    print('a==b')
else:
    print('a!=b')

if (a != b):
    print('a!=b')
if (a < b):
    print('a < b')
if (a > b):
    print('a > b')
a = 5 
b = 20
if (a <= b):
    print('a <= b')
else:
    print('a > b')
if (b >= a):
    print('b >= a')

a = 21
b = 10
c = 0
c = a + b
print(c)
c += a
print(c)
c *= a
print(c)
c /= a
print(c)
c = 2
c %= a
print(c)
c **= a
print(c)
c //= a
print(c)

a = 60
b = 13
c = 0
c = a & b
print(c)
c = a | b
print(c)
c = a ^ b
print(c)
c = ~a
print(c)
c = a << 2
print(c)
c = a >> 2
print(c)

a = 10
b = 20
if (a and b):
    print('a and b true')
else:
    print('a and b false')
if (a or b):
    print('a or b true')
else:
    print('a or b false')

a = 0
if (a and b):
    print('a and b true')
else:
    print('a and b false')
if (a or b):
    print('a or b true')
else:
    print('a or b false')
if not (a and b):
    print('not (a and b) true')
else:
    print('not (a and b) false')

a = 10
b = 20
list1 = [1, 2, 3, 4, 5]
print(a in list1)
print(a not in list1)

a = 20
b = 20
if (a is b):
    print('a is b')
else:
    print('a is not b')
if (id(a) == id(b)):
    print('相同标识')
else:
    print('不同标识')
