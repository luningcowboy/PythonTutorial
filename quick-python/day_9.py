#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: luning
# Created Time : 三  4/ 8 09:09:32 2020
# File Name: day_9.py
# Description:
"""
# 删除列表元素
l1 = [1, 2, 3, 4]
print(l1)
del l1[0]
print(l1)
# 获取列表长度
print(len(l1))
# 列表组合
l2 = [11, 12, 13]
l3 = l1 + l2
print(l3)
# 列表重复
print(l2 * 3)
# 判断元素是否存在于列表中
print(11 in l2)
print(11 not in l2)
# 列表迭代
for x in l2:
    print(x, end=" ")
# 列表截取和分割
print(l2[1])
print(l2[-2])
print(l2[1:])
# 嵌套列表
l4 = [[1,2],3,4,[5,6]]
print(l4)
print(l4[0])
# 返回列表最大元素值
print(max(l2))
# 获取列表最小值
print(min(l2))
# 元组转换为列表
print(list((1,2,3)))
# 列表操作
l5 = []
# 添加元素
l5.append(1)
l5.append(1)
print(l5)
# 统计某个元素的数量
print(l5.count(1))
# 追加元素
l5.extend(range(5))
print(l5)
l5.extend([3,2,1])
print(l5)
# 返回列表中指定元素的第一个匹配项的索引值
print(l5.index(3))
# 插入
l5.insert(1, 'abc')
print(l5)
# 移除列表的一个元素并返回其值,默认最后一个元素
print(l5.pop())
print(l5)
print(l5.pop(1))
print(l5)
# 移除列表某个值的第一个匹配项
l5.remove(1)
print(l5)
# 反向列表
l6 = [1,2,3,4]
l6.reverse()
print(l6)
# 对原列表进行排序
l7 = [1,3,2,4,6,5]
l7.sort()
print(l7)
l7 = [1,3,2,4,6,5]
l7.sort(reverse=True)
print(l7)

def takeSecond(ele):
    return ele[1]
random = [(2,2),(3,4),(4,5),(5,1)]
random.sort(key=takeSecond)
print(random)

# 情况列表
l8 = [1,2,3]
print(l8)
l8.clear()
print(l8)

# 复制列表
l9 = [1,2,3,4]
l10 = l9.copy()
l11 = [1,2,3,4]
print(l10)
print(l10 == l9)
print(l11 == l9)
