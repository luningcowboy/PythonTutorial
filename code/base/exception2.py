#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile","w")
    fh.write("这是一个测试文件")
finally:
    print "error"
