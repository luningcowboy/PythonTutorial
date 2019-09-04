#!/usr/bin/python
# -*- coding: UTF-8 -*-

fo = open('foo.txt',"r+")
print fo.name
print fo.closed
print fo.mode
print fo.softspace
#fo.write("www.baidu.com")
str = fo.read(10)
print str
position = fo.tell() # 查找当前未知
print 'position', position
position = fo.seek(0,0) # 再次把指针重新定位到文件头
print 'position', position
str = fo.read(10)
print str
fo.close()
