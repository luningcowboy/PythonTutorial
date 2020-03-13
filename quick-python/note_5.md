1. `str.format`的使用:
向`str.format`中传入对象
```python
class AssignValue(object):
    def __init__(self, value):
        self.value = value
        self.name = 'AssignValue'

my_value = AssignValue(6)
print("value = {0.value} ,name = {0.name}".format(my_value))#value = 6 ,name = AssignValue
```
2. 数字格式化
```python
print("{:.2f}".format(3.141592653))# 3.14
```
3. 三引号
```python
para_str = """这是一个多行实例
多行字符串可以使用制表符
TAB( \t )
也可以使用换行符( \n )
"""
print(para_str)
```
4. f-string 是3.6后添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
f-string不错，语法简单，类似js中的反引号格式化字符串
```python
name = 'world'
str_1 = f'Hello {name}' #Hello world
print(str_1)
print(f'{1 + 2}') # 3
w = {'name': 'BaiDu', 'url': 'www.baidu.com'}
str_2 = f'{w["name"]}: {w["url"]}'
print(str_2) #BaiDu: www.baidu.com
x = 1
print(f'{x + 1}') # python 3.6 =>2
#print(f'{x + 1=}') # python 3.8 => x + 1 = 2
```
5. py2中普通字符串是以8为ASCII编码存储的，而unicode字符串是以16位unicode字符串存储的，这样能够表示更多的字符集，使用语法是在字符串前面加`u`
在py3中所有的字符串都是unicode存储的
6. 字符串内建函数
- `capitalize` 将字符串的第一个字符转换位大写
- `center(width, fillchar)` 返回一个指定宽度的字符串，`fillchar`为填充字符, 默认为空格
- `count(str, beg=0, end=len(string))` 返回`str`在string中出现的次数
- `bytes.decode(encoding="urf-8", erors="strict")` python3中没有decode方法，使用bytes的decode方法来解码给定的`bytes`对象，这个`bytes`对象可以由`str.encode`来编码返回
- `encode(encoding='UTF-8', errors='strict')` 以encoding指定的编码格式来编码, 如果出错默认报一个ValueError异常，除非errors指定的是`ignore`或者`replace`
- `endswith(suffix, beg=0, end=len(string))` 检查字符串是否以suffix结束
- `expandtabs(tabsize=8)` 将字符串string中的tab符号转换为空格，tab默认的空格数为8
- `find(str, beg=0, end=len(string))` 检测str是否包含在字符串中，如果指定beg和end，就是在这两个范围内检查, 返回值为开始的索引, 否则返回-1
- `index(str, beg=0, end=len(string))` 跟`find`方法一样，只不过如果str不在字符串中会报一个异常
- `isalnum()` 如果字符串至少有一个字符，并且所有字符都是字母或者数字则返回True,否则返回False
- `isalpha()` 如果字符串中至少含有一个字符，并且所有的字符都是字母则返回True, 否则返回False
```python
str_1 = 'this is string example about capitalize.'
print(str_1.capitalize())#This is string example about capitalize.

str_1 = 'hello'
print(str_1.center(40, '*'))#*****************hello******************

str_1 = 'hello,hellopython hello hello he'
print(str_1.count('hell')) #4
print(str_1.count('hell', 7)) #2
print(str_1.count('hell', 7, 25)) #1

str_1 = 'Baidu'
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str_1)
print(f'utf8=>{str_utf8}')
print(f'gbg=>{str_gbk}')
print(f'utf8 decode:{str_utf8.decode("UTF-8","strict")}')
print(f'gbk decode:{str_gbk.decode("GBK", "strict")}')

str_1 = 'Baidu example ...wow!!!'
suffix = '!!'
print(str_1.endswith(suffix))
print(str_1.endswith(suffix, 20))

str_1 = "this is\tstring example...wow"
print(str_1)
print(str_1.expandtabs(18))
print(str_1.expandtabs(40))

str_1 = 'this is string example'
print(str_1.find('is')) # 2
print(str_1.index('is'))
#print(str_1.index('goo')) # error

str_1 = 'abc1ad'
print(str_1.isalnum()) # True
print('!@#$'.isalnum()) # False
print(''.isalnum()) # False
print(str_1.isalpha()) # False
print('abcd'.isalpha()) # True
```
