#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCount:
    __prevateCount = 0
    publicCount = 0
    def count(self):
        self.__prevateCount += 1
        self.publicCount += 1
        print self.__prevateCount

count = JustCount()
count.count()
count.count()
print count.publicCount
# 不能直接访问私有变量
#print count.__prevateCount
# 通过object._className__attrName
print count._JustCount__prevateCount
