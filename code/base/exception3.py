#!/usr/bin/python
# -*- coding: UTF-8 -*-

def mye(level):
    if level < 1:
        raise Exception,"Invalid level"

try:
    mye(0)
except Exception, err:
    print 1, err
else:
    print 2
