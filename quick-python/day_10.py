#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 四  4/ 9 21:33:26 2020
# File Name: day_10.py
# Description:
"""
tup1 = (50)
print(type(tup1)) #<class 'int'>
tup1 = (50,)
print(type(tup1)) #<class 'tuple'>
tup1 = (1,2,3,4,5)
print(tup1[0]) # 1
print(tup1[1:5]) # (2, 3, 4, 5)
tup1 = (1, 2, 4)
tup2 = ('a', 'b', 'c')
tup3 = tup1 + tup2
print(tup3) # (1, 2, 4, 'a', 'b', 'c')
tup4 = (1, 2, 3)
del tup4
#print(tup4)#NameError: name 'tup4' is not defined

print(len(tup3)) # 6
print((1,2,3) + (4,5,6)) #(1, 2, 3, 4, 5, 6)
print((1,2,4) * 3) #(1, 2, 4, 1, 2, 4, 1, 2, 4)
print(3 in (1,2,3)) # True
print(3 not in (1,2,3)) # False
for x in (1,2,3):
    print(x, end=" ") # 1 2 3

print()
tup5 = (1,2,3,4,5)
print(tup5[0]) # 1
print(tup5[-1]) # 5
print(tup5[1:]) # (2, 3, 4, 5)

print(len(tup5)) # 5
print(max(tup5)) # 5
print(min(tup5)) # 1
print(tuple([1,2,3,4])) # (1, 2, 3, 4)

tup6 = (1,2,3)
print(id(tup6)) #4436455784
tup6 = ('a', 'b', 'c')
print(id(tup6)) #4454681624
