#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 20
b = 20

if (a is b):
    print 'a, b 有相同的标识'
else:
    print 'a, b 有不同的标识'

if (a is not b):
    print 'a, b 有不同的标识'
else:
    print 'a, b 有相同的标识'

b = 30
if (a is b):
    print 'a, b 有相同的标识'
else:
    print 'a, b 有不同的标识'

if (a is not b):
    print 'a, b 有不同的标识'
else:
    print 'a, b 有相同的标识'
