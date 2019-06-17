#!/usr/bing/python
# -*- coding: UTF-8 -*-

import time;

ticks = time.time()
print ticks

localtime= time.localtime(ticks)
print localtime

localtime = time.asctime(localtime)
print localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

import calendar
cal = calendar.month(2019,6)
print cal
