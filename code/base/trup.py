#!/usr/bing/python
# -*- coding: UTF-8 -*-

tup1 = ('physics','chemistry',1997, 2000)
tup2 = (1,2,3,4,5,6,7)

print 'tup1', tup1[0]
print 'tup2[1:5]', tup1[1:5]

tup3 = (12, 34, 56)
tup4 = ('abc', 'xyz')

tup5 = tup3 + tup4
print tup5
del tup5
# 运算符
print len(tup4)
print (1,2,3) + (4,5,6)
print 3 in tup2
for x in tup2: print x
# 索引，截取
tup6 = ('spam','Spam','SPAM')
print tup6[2], tup6[-2],tup6[1:]
# 任意无符号的对象，以逗号隔开，默认问元组
print 'abc', -4.24e93, 18+6.6j, 'xyz'
x, y = 1, 2
print x,y

# cmp
t1 , t2 = (123,'xyz'), (456, 'abc')
print cmp(t1, t2)
print cmp(t2, t1)
t3 = t2 + (678,)
print cmp(t3, t2)

# len
print len(t1), len(t2), len(t3)

# max
t4 = (1,2,3,4,5)
print max(t4)
# min
print min(t4)
# tuple(list) 将列表转换为元组
t5 = tuple([1,2,3])
print t5






















