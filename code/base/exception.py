#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件")
except IOError:
    print "Error, 没有找到指定文件"
else:
    print "success"
    fh.close()
