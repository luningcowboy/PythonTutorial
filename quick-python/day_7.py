#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 一  3/16 08:57:04 2020
# File Name: day_7.py
# Description:
"""

str_1 = "abc"
print(str_1.rjust(10)) #        abc
print(str_1.rjust(10,"*")) # *******abc

str_1 = 'abc   '
print(str_1.rstrip()) #abc
print('abc***'.rstrip('*')) #abc

str_1 = 'abcxabcxabcxabcxabcxabc'
print(str_1.split('x')) # ['abc', 'abc', 'abc', 'abc', 'abc', 'abc']
print(str_1.split('x', 3)) #['abc', 'abc', 'abc', 'abcxabcxabc']

str_1 = 'ab c\n\nde fg\rkl\r\n'
print(str_1.splitlines()) #['ab c', '', 'de fg', 'kl']
print(str_1.splitlines(True)) #['ab c\n', '\n', 'de fg\r', 'kl\r\n']

str_1 = 'this is string example'
print(str_1.startswith('this')) #True
print(str_1.startswith('string', 8)) #True
print(str_1.startswith('this', 2, 4)) #False

str_1 = '***abc***'
print(str_1.strip('*')) #abc

str_1 = 'abcABC'
print(str_1.swapcase()) #ABCabc

