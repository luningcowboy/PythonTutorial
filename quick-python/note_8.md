1. `str.title` 返回标题化的字符串
```python
STR_1 = 'this is a title'
print(STR_1.title()) #This Is A Title
```
2. `translate`方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中
```python
IN_TAB = 'aeiou'
OUT_TAB = '12345'
TRAN_TAB = str.maketrans(IN_TAB, OUT_TAB)
STR_1 = 'this is string example'
print(STR_1.translate(TRAN_TAB)) #th3s 3s str3ng 2x1mpl2
```
3. `str.upper` 将字符串中的小写字母修改为大写
```python
STR_1 = 'this is a string example'
print(STR_1.upper()) #THIS IS A STRING EXAMPLE
```
4. `str.zfill(width)` 返回指定长度的字符串，原字符串右对齐，前面填充0。 
`zero fill`
```python
STR_1 = 'this is a string'
print(STR_1.zfill(40))#000000000000000000000000this is a string
```

5. `str.isdecimal()` 检查字符串是否只包含十进制数字
```python
print('123'.isdecimal()) # True
print('a12'.isdecimal()) # False
```

6. list声明和访问:
```python
LIST_1 = [1, 2, 3, 4, 5]
print(LIST_1[0])#1
print(LIST_1[1:3])#[2,3]
print(LIST_1)#[1, 2, 3, 4, 5]
print(LIST_1[-1::-1])#[5, 4, 3, 2, 1]
print(LIST_1[::-1])#[5, 4, 3, 2, 1]
```
