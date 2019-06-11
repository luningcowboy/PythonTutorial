#!/usr/bin/python
# -*- coding: UTF-8 -*-


for letter in 'Python':
    print '当前字母:', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print '当前水果', fruit

for index in range(len(fruits)):
    print '当前水果', fruits[index] 

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d 等于 %d * %d'%(num, i,j )
            break
    else:
        print num, '是一个质数'

