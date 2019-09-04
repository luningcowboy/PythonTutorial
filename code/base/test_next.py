#!/usr/bin/python
# -*- coding: UTF-8 -*-

it = iter([1,2,3,4,5])
for i in it:
    print i
while True:
    try:
        x = next(it)
        print x
    except StopIteration:
        print "stop"
        break
