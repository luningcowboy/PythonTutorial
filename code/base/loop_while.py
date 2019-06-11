#!/usr/bin/python
# -*- coding: UTF-8 -*-
count = 0
while (count < 9):
    print 'The count is:', count
    count += 1
print 'End'

i = 1
while i < 10:
    i += 1
    if i%2 > 0:
        continue
    print i

i = 1
while 1:
    print i
    i += 1
    if (i > 10):
        break

'''
var = 1
while var == 1:
    num = raw_input('Enter a number :')
    print 'your input ', num
print 'GoogBye'
'''
count = 0
while count < 5:
    print count, ' is less than 5'
    count = count + 1
else:
    print count, ' is not less than 5'

flat = 1
while (flat): print 'Give flat is really true!'
print 'GoodBye'
