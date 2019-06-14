#!/usr/bing/python
# -*- coding: UTF-8 -*-
import math
import cmath
import random
import datetime


print dir(math)
print dir(cmath)

"""
数学函数
"""
# abs 返回数字的绝对值
print 'test abs'
print 'abs -45', abs(-45)
print 'abs 100.12', abs(100.12)
print 'abs 119L', abs(119L)
print 'test abs end'

# ceil 返回数字的上入整数
print 'test ceil'
print 'math.ceil(-45.17)', math.ceil(-45.17)
print 'math.ceil(100.12)', math.ceil(100.12)
print 'math.ceil(100.72)', math.ceil(100.72)
print 'math.ceil(119L)', math.ceil(119L)
print 'math.ceil(math.pi)', math.ceil(math.pi)
print 'test ceil end'

# cmp(x,y) 比较两个对象 x<y return -1, x==y return 0, x > y return 1
print 'test cmp'
print 'cmp(80, 100)', cmp(80, 100)
print 'cmp(80, 80)', cmp(80, 80)
print 'cmp(90, 80)', cmp(90, 80)
print 'end test cmp'

# exp(x) 返回x的指数
print 'test exp'
print 'math.exp(-45.17)', math.exp(-45.17)
print 'math.exp(100.12)', math.exp(100.12)
print 'math.exp(100.72)', math.exp(100.72)
print 'math.exp(119L)', math.exp(119L)
print 'math.exp(math.pi)', math.exp(math.pi)
print 'end test exp'

# fabs() 返回数字的绝对值,float类型
print 'test fabs'
print 'math.fabs(10)', math.fabs(10)
print 'math.fabs(100.12)', math.fabs(100.12)
print 'math.fabs(-100.72)', math.fabs(-100.72)
print 'math.fabs(119L)', math.fabs(119L)
print 'math.fabs(math.pi)', math.fabs(math.pi)
print 'end test fabs'

# floor() 返回数字的下舍整数
print 'test math.floor'
print 'test math.floor(-45.17)', math.floor(-45.17)
print 'test math.floor(100.12)', math.floor(100.12)
print 'test math.floor(100.72)', math.floor(100.72)
print 'test math.floor(119L)', math.floor(119L)
print 'end test math.floor'

# log(x) 返回x的自然对数
print 'test log'
print 'math.log(100.12)', math.log(100.12)
print 'math.log(100.72)', math.log(100.72)
print 'math.log(119L)', math.log(119L)
print 'math.log(math.pi)', math.log(math.pi)
print 'math.log(10, 2)', math.log(10, 2)
print 'end test log'

# log10(x) 以10为基数的x的对数
print 'test log10'
print 'math.log10(100.12)', math.log10(100.12)
print 'math.log10(100.72)', math.log10(100.72)
print 'math.log10(119L)', math.log10(119L)
print 'math.log10(math.pi)', math.log10(math.pi)
print 'end test log10'

# max 返回给定参数的最大值,参数可以为序列
print 'test max'
print 'max(80, 100, 100)', max(80, 100, 1000)
print 'max(-20, 100, 400)', max(-20, 100, 400)
print 'max(-80, -20, -10)', max(-80, -20, -10)
print 'max(0, 100, -400)', max(0, 100, -400)
print 'end test max'

# min 返回给定参数的最小值,参数可以是列表
print 'test min'
print 'min(80, 100, 400)', min(80, 100, 400)
print 'min(-80, 100, 400)', min(-80, 100, 400)
print 'min(-80, -20, -10)', min(-80, -20, -10)
print 'min(0, 100, -400)', min(0, 100, -400)
print 'end test min'

# modf() 返回参数的整数部分与小数部分，两部分与参数的符号相同，整数部分以浮点型表示
print 'test modf'
print 'math.modf(1.15)', math.modf(1.15)
print 'math.modf(-1.15)', math.modf(-1.15)
print 'math.modf(0.15)', math.modf(0.15)
print 'math.modf(math.pi)', math.modf(math.pi)
print 'end test modf'

# pow(x,y) 返回x的y次方
print 'test pow'
print 'math.pow(2,10)', math.pow(2,10)
print 'math.pow(2,-10)', math.pow(2,-10)
print 'math.pow(3,0)', math.pow(3,0)
print 'math.pow(3,math.pi)', math.pow(3,math.pi)
print 'end test pow'

# round 返回参数的四舍五入值
print 'test round'
print 'round(1.1)', round(1.1)
print 'round(-1.1)', round(-1.1)
print 'round(1.5)', round(1.5)
print 'round(-1.5)', round(-1.5)
print 'round(80.123523,2)', round(80.123521,2)
print 'round(80.123523,3)', round(80.123521,3)
print 'round(80.123523,4)', round(80.123521,4)
print 'end test round'

# sqrt 返回参数的平方根
print 'test sqrt'
print 'math.sqrt(4)', math.sqrt(4)
print 'math.sqrt(7)', math.sqrt(7)
print 'math.sqrt(math.pi)', math.sqrt(math.pi)
print 'end test sqrt'

"""
随机数函数
"""

# choice() 返回一个列表，元组或字符串的随机项
print 'test choice'
print "random.choice([1,2,3,4,5,6])",random.choice([1,2,3,4,5,6])
print "random.choice([1,2,3,4,5,6])",random.choice([1,2,3,4,5,6])
print "random.choice([1,2,3,4,5,6])",random.choice([1,2,3,4,5,6])
print "random.choice('A string')",random.choice('A string')
print "random.choice('A string')",random.choice('A string')
print "random.choice('A string')",random.choice('A string')
print 'end test choice'

# randrange 返回递增基数集合中的一个随机数，基数缺省值为1
# randrange(start, stop, step) start <= ret < stop step 递增基数
print 'test randrange'
print 'random.randrange(1,3,1)', random.randrange(1,3,1)
print 'random.randrange(100,1000,2)', random.randrange(100,1000,2)
print 'random.randrange(100,1000,3)', random.randrange(100,1000,3)
print 'end test randrange'

# random 随机生成一个实数 0 <= ret < 1
print 'test random'
print 'random', random.random()
print 'random', random.random()
print 'end test random'

# seed 改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数
print 'test seed'
random.seed(10)
print 'random, while seed = 10 ', random.random()
random.seed(20)
print 'random, while seed = 20 ', random.random()
random.seed(10)
print 'random, while seed = 10 ', random.random()
print 'end test seed'

# shuffle 将列表的所有元素随机排序, 洗牌算法
print 'test shuffle'
list = [1,2,3,4,5]
print 'before shuffle ', list
random.seed(datetime.datetime.now())
random.shuffle(list)
print 'after shuffle ', list
print 'end test shuffle'

# uniform(x,y) 将随机生成一个实数，在[x,y]范围内
print 'test uniform'
print 'random.uniform(5,10)', random.uniform(5,10)
print 'random.uniform(5,10)', random.uniform(5,10)
print 'end test uniform'

"""
三角函数
"""





















