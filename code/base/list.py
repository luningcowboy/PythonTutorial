#!/usr/bing/python
# -*- coding: UTF-8 -*-
list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,7]
print 'list1[0]', list1[0]
print 'list1[2]', list1[2]
print 'list1[-2]', list1[-2]
print 'list2[1:5]', list2[1:5]
print 'list2[:4]', list2[:4]
print 'list2[4:]', list2[4:]
print '["hi"]*4', ["hi"]*4
print 'len(list1)', len(list1)
print '[1,2,3] + [4,5,6]', [1,2,3] + [4,5,6]
print '2 in [1,2,3]', 2 in [1,2,3]
for x in [1,2,3]: print x

# 更新列表
list3 = []
list3.append('Google')
list3.append('Runoob')
print list3

# 删除列表元素
del list3[1]
print list3

# cmp 比较两个列表的元素
list1, list2 = [123, 'xyz'], [456,'abc']
print cmp(list1, list2)
print cmp(list2, list1)
list3 = list2 + [768]
print cmp(list2, list3)
print cmp(list3, list2)

# max 返回列表中最大的值
list1 = [1,2,3,4,5]
print list1, max(list1)
print list1, min(list1)
list1 = ['abc','xxx','dd']
print list1, max(list1)
print list1, min(list1)

# list 将元组转换位列表
tuple1 = (123, 'xyz','zara','abc')
list1 = list(tuple1)
print tuple1, list1
print list1, max(list1)
print list1, min(list1)

# append
list1 = [1,2,3,4]
list1.append(5)
print list1
list2 = [1,2,3,2,1,4,5]
print list2, list2.count(1)
list1.extend(list2)
print list1

# index
list1 = ['a','b','c','d']
print list1.index('d')
















































