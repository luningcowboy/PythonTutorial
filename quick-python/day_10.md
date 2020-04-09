1. 元组定义:
**不加逗号为int,加上逗号为元组**
```python
tup1 = (50)
print(type(tup1)) #<class 'int'>
tup1 = (50,)
print(type(tup1)) #<class 'tuple'>
```

2. 访问元组:
```python
tup1 = (1,2,3,4,5)
print(tup1[0]) # 1
```

3. 修改元组:
元组中的元素不允许修改，但是可以用多个元组组合成一个元素
```python
tup1 = (1, 2, 4)
tup2 = ('a', 'b', 'c')
tup3 = tup1 + tup2
print(tup3) # (1, 2, 4, 'a', 'b', 'c')
```

4. 删除元组
元组中的元素不允许删除，但是，可以删除整个元组
```python
tup4 = (1, 2, 3)
del tup4
#print(tup4)#NameError: name 'tup4' is not defined
```

5. 元组运算符符号:

```python
print(len(tup3)) # 6
print((1,2,3) + (4,5,6)) #(1, 2, 3, 4, 5, 6)
print((1,2,4) * 3) #(1, 2, 4, 1, 2, 4, 1, 2, 4)
print(3 in (1,2,3)) # True
print(3 not in (1,2,3)) # False
for x in (1,2,3):
    print(x, end=" ") # 1 2 3
```

6. 元组索引和截取
```python
tup5 = (1,2,3,4,5)
print(tup5[0]) # 1
print(tup5[-1]) # 5
print(tup5[1:]) # (2, 3, 4, 5)
```

7. 元组内置函数

```python
print(len(tup5)) # 5
print(max(tup5)) # 5
print(min(tup5)) # 1
print(tuple([1,2,3,4])) # (1, 2, 3, 4)
```

**所谓元组的不可变指的是元组所指向的内存中的内容不可变。**
```python
tup6 = (1,2,3)
print(id(tup6)) #4436455784
tup6 = ('a', 'b', 'c')
print(id(tup6)) #4454681624
```
