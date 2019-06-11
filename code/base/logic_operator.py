#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = 21
b = 10
c = 0
if a and b:
    print 'a, b 都为true'
else:
    print 'a, b中有一个不为true'

if a or b:
    print 'a, b 中有一个为true'
else:
    print 'a, b 都不为true'

a = 0
if a and b:
    print 'a, b 都为true'
else:
    print 'a, b 中有一个不为true'

if a or b:
    print 'a, b 中有一个为true'
else:
    print 'a, b 都不为true'

if not(a and b):
    print 'a,b都为false, 或者其中一个位false'
else:
    print 'a,b都为true'
