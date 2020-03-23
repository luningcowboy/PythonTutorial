#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 一  3/23 09:02:19 2020
# File Name: day_8.py
# Description:
"""
STR_1 = 'this is a title'
print(STR_1.title()) #This Is A Title

IN_TAB = 'aeiou'
OUT_TAB = '12345'
TRAN_TAB = str.maketrans(IN_TAB, OUT_TAB)
STR_1 = 'this is string example'
print(STR_1.translate(TRAN_TAB)) #th3s 3s str3ng 2x1mpl2

STR_1 = 'this is a string example'
print(STR_1.upper()) #THIS IS A STRING EXAMPLE

STR_1 = 'this is a string'
print(STR_1.zfill(40))#000000000000000000000000this is a string

print('123'.isdecimal()) # True
print('a12'.isdecimal()) # False

LIST_1 = [1, 2, 3, 4, 5]
print(LIST_1[0])#1
print(LIST_1[1:3])#[2,3]
print(LIST_1)#[1, 2, 3, 4, 5]
print(LIST_1[-1::-1])#[5, 4, 3, 2, 1]
print(LIST_1[::-1])#[5, 4, 3, 2, 1]
