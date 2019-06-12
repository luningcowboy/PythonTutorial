#!/usr/bing/python
# -*- coding: UTF-8 -*-

for letter in 'Python':
    if letter == 'h':
        continue
    print ' 当前字母', letter

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print '当前字母', var
print 'Good Bye'
