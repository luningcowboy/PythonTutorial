#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Created Time : 六  3/14 16:45:38 2020
# File Name: day_6.py
# Description:
"""

str_1 = '1223'
print(str_1.isdigit())
print('a12b'.isdigit())

print('aB12d'.islower()) # False
print('1234'.islower()) # False
print('1234abc'.islower()) # True

print('123'.isnumeric()) # True
print('123a'.isnumeric()) # False
print('123#'.isnumeric()) # False

print('123'.isspace()) # False
print('1 23'.isspace()) # False
print(''.isspace()) # False
print('    '.isspace()) # True

str_1 = 'This Is Title!'
print(str_1.istitle()) # True
print('This is title'.istitle()) # False
print('This Is Title #123'.istitle()) # True 
print('This Is 231#Title #123'.istitle()) # True 
print('This Is 231#title #123'.istitle()) # False

print('123'.isupper()) # False
print('ABC123'.isupper()) # True
print('abc'.isupper()) # False
print('Abc'.isupper()) # False

print('*'.join('abcd')) # a*b*c*d
print('*'.join(['a','b','c'])) # a*b*c
print(''.join('a b c')) # a b c

print(len('abc')) #3

print('abc'.ljust(10,'*')) #abc*******

print('   abc  a***'.lstrip()) #abc  a***
print('***abc***'.lstrip('*')) #abc***

intab = 'aeiou'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
str_1 = 'this is string example ...wow!!!'
print(str_1.translate(trantab))#th3s 3s str3ng 2x1mpl2 ...w4w!!!

print(max('abcdef')) # f
print(min('abcdef')) # a
print(min('012abcdef')) # 0

print('abc-abc-abc'.replace('abc', 'cba')) #cba-cba-cba
print('abc-abc-abc'.replace('abc', 'cba', 2)) #cba-cba-abc

print('abca'.rfind('a')) # 3
print('abca'.find('a')) # 0

print('abca'.rindex('a')) # 3
print('abca'.index('a')) # 0

