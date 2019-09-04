#!/usr/bing/python
# -*- coding: UTF-8 -*-

def printStr(str):
    print str

printStr('test')
printStr('test1')

def ChangeInt(a):
    a = 10
b = 2
ChangeInt(b)
print b

def changeme(mylist):
    mylist.append([1,2,3,4,5])
    print 'in function ',mylist
    return
mylist =[10,20,30]
changeme(mylist)
print 'out function',mylist

def printme(str):
    print str

printme(str="测试")

def printinfo(name, age):
    print "Name:", name
    print "Age:", age
printinfo(name="Tom",age=10)

# 默认参数
def printinfo2(name, age=20):
    print "Name:", name
    print "Age:", age
printinfo2(name="Tom")

# 不定长参数
def printinfo3(arg1, *vartuple):
    print "输出:"
    print arg1
    for var in vartuple:
        print var
    return
printinfo3(1,2,3,4,5,6)

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2
print sum(1,2)
print sum(1,3)

# 函数返回值
def sum(arg1, arg2):
    return arg1 + arg2
print sum(1,2) #

# 作用域
total = 0
def sum2(arg1, arg2):
    total = arg1 + arg2
    return total
sum2(1,10)
print "total=",total

