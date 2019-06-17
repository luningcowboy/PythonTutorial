#!/usr/bing/python
# -*- coding: UTF-8 -*-

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print dict['Name']
print dict['Age']
dict['Age'] = 8
print dict['Age']
print dict
"""
dict.clear()
print dict
del dict
print dict
"""

# cmp
d2 = {'Zame': 'Zara', 'Age': 7, 'Class': 'First'}
print cmp(dict, d2)
# len
print len(dict)
# str
print str(dict)
# type
print type(dict)
# clear
dict.clear()
print dict
# dict.copy 返回一个字典的浅拷贝
dct1 = {'Name': 'Zara', 'Age': 7}
dct2 = dct1.copy()
print cmp(dct1, dct2)
dct2['Name'] = 'Tom'
print dct1['Name'], dct2['Name']
import copy
dct1 = {'a':[1,2,3],'b':{'b1':1}}
dct2 = dct1
dct3 = dct1.copy()
dct4 = copy.deepcopy(dct1)
dct1['a'].append(4)
print dct2
print dct3
dct3['a'] = [1,2,1]
print dct3

dct5 = dict.fromkeys(['a','b','c'],[1,2,3])
print dct5
dct5 = dict.fromkeys(['a','b'],1)
print dct5
dct5 = dict.fromkeys(['a','b'])
print dct5
print dct5.get('a')
print dct5.has_key('a')
print dct5.items()
print dct5.keys()
print dct5.setdefault('a',5)
print dct5.setdefault('c',5)

d1 = {'a':1, 'b':2}
d2 = {'a':2, 'c':2}
d1.update(d2)
print d1, d2

print d1.values()

print d1.popitem(), d1
