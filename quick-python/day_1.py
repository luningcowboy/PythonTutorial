# -*- coding: utf-8 -*-
#!/usr/bin/python3

# 这是注释
# 获取保留字
import keyword
print(keyword.kwlist)
'''
多行注释
多行注释
'''
"""
多行注释
多行注释
"""
print("Hello, Python")

if True:
    print('true')
else:
    print('false')

total = 1 + \
    2 \
    + 3
print(total)

total = [1, 2, 
         3, 4,
         5]
print(total)

str_0 = """
xxxx
yyyy
zzzz
"""
print(str_0)
str_1 = r"this is a line with \n xxxx"
str_2 = "this is a line with \n xxxx"
print(str_1)
print(str_2)

str_3 = "a" + "b" + 'c'
print(str_3)
str_4 = 'a'*5
print(str_4)

str_5 = 'abcdef'
print(str_5[0])
print(str_5[-1])
print(str_5[0:2:3])

import sys
print(sys.argv[0])
print(len(sys.argv))

a, b, c, d = 10, 1.1, False, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int), isinstance(b, float), isinstance(c, bool), isinstance(d, complex))

a, b, c, d = 1, 2, 3, 4
print(a + b) # 加法
print(c - a) # 减法
print(c / b) # 除法，得到一个浮点数
print(c // b) # 除法， 得到一个整数
print(c % b) # 取余数
print(b ** c) # 乘方

str = 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str + "TEST")
print('Ru\noob')
print(r'Ru\noob')

list = ['abcd', 123, 0.01, 'hello']
l2 = ['ddd', 1001]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(l2 + list)
print(l2 * 2)
l3 = l2 * 2
print(l3)

def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output
print(reverseWords('I like runoob'))
