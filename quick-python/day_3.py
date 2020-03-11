#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Created Time : 三  3/11 16:07:45 2020
# File Name: day_3.py
# Description:
"""

var1 = 1
var2 = 10
print(var1, var2)
del var1, var2
#print(var1, var2) # 这里会报错:NameError: name 'var1' is not defined

print(abs(-40))
print(abs(-1.02))
import math
print(math.fabs(-40))
print(math.fabs(-1.02))
print(math.ceil(1.1)) # 2
print(math.ceil(-1.1)) # -1
print(math.exp(100))
print(math.floor(1.8)) # 1
print(math.floor(-1.8)) # -2
print(math.log(100, 10)) # 2.0
print(max(1,2,3,4,5)) # 5
print(max([1,2,30,4,5])) # 30
print(min(1, 2, 3, 4, 5)) # 1
print(min([1,2,30,4,5])) # 1
print(math.modf(1.21)) # (小数部分，整数部分)
print(pow(2, 3))
print(round(1.3), round(1.8))
print(math.sqrt(100))

import random
print(random.choice([1,2,3,4,5]))
print(random.choice(range(100)))
print(random.choice('HelloPython'))
print(random.randrange(2, 10, 2))
print(random.random())
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
l = [1,2,3,4,5]
print(l)
random.shuffle(l)
print(l)
random.seed()
print(random.uniform(1, 5))
