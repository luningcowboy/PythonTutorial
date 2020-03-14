1. `isdigit()` 如果字符串只包含数字则返回`True`,否则返回`false`
```python
str_1 = '1223'
print(str_1.isdigit()) # True
print('a12b'.isdigit()) # False
```
2. `islower()`如果字符传中包含一个区分大小写的字符，那么，所有的区分大小写的字符都是小写，返回`True`
- 必须包含区分大小写的字符
- 区分大小写的字符必须全是小写
```python
print('aB12d'.islower()) # False
print('1234'.islower()) # False
print('1234abc'.islower()) # True
```
3. `isnumeric()` 如果字符串中只包含数字则返回True
```python
print('123'.isnumeric()) # True
print('123a'.isnumeric()) # False
print('123#'.isnumeric()) # False
```
4. `isspace()` 如果字符串中只包含空白字符则返回True
```python
print('123'.isspace()) # False
print('1 23'.isspace()) # False
print(''.isspace()) # False
print('    '.isspace()) # True
```
5. `istitle()` 如果字符串每个单词的第一个字母都是大写返回True
```python
str_1 = 'This Is Title!'
print(str_1.istitle()) # True
print('This is title'.istitle()) # False
print('This Is Title #123'.istitle()) # True 
print('This Is 231#Title #123'.istitle()) # True 
print('This Is 231#title #123'.istitle()) # False
```
6. `isupper()` 如果字符串中至少包含一个区分大小写的字符，并且，所有区分大小写的字符都是大写，返回True
```python
print('123'.isupper()) # False
print('ABC123'.isupper()) # True
print('abc'.isupper()) # False
print('Abc'.isupper()) # False
```
7. `join(seq)` 以指定字符作为分隔符，将seq中的所有元素合并为一个新的字符串
```python
print('*'.join('abcd')) # a*b*c*d
print('*'.join(['a','b','c'])) # a*b*c
print(''.join('a b c')) # a b c
```
8. `len(string)` 获取字符串的长度
```python
print(len('abc')) #3
```
9. `ljust(width[,fillchar])` 返回一个原字符串左对齐，并且使用fillchar填充到指定长度的新字符串,fillchar默认为空格
```python
print('abc'.ljust(10,'*')) #abc*******
```
10. `lstrip()` 裁到字符串左边的空格或指定字符
```python
print('   abc  a***'.lstrip()) #abc  a***
print('***abc***'.lstrip('*')) #abc***
```
11. `maketrans()` 用于创建字符映射的转换表，对于接收两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标
`str.maktrans(intab,outtab)`:
- intab: 字符串中要替代的字符组成的字符串
- outtab: 映射字符的字符串
```python
intab = 'aeiou'
outtab = '12345'
trantab = str.maketrans(intab, outtab)
str_1 = 'this is string example ...wow!!!'
print(str_1.translate(trantab))#th3s 3s str3ng 2x1mpl2 ...w4w!!!
```
12. `max(str)` 返回字符串中最大的字符
13. `min(str)` 返回字符串中最新的字符
```python
print(max('abcdef')) # f
print(min('abcdef')) # a
print(min('012abcdef')) # 0
```
14. `replace(old, new[,max])` 将指定字符串中的old替换成new,如果max指定，则替换不能超过max次
```python
print('abc-abc-abc'.replace('abc', 'cba')) #cba-cba-cba
print('abc-abc-abc'.replace('abc', 'cba', 2)) #cba-cba-abc
```
15. `rfind(str, beg=0, end=len(string))` 类似find,只不过从右边开始查找, 返回字符串最后一次出现的位置
```python
print('abca'.rfind('a')) # 3
print('abca'.find('a')) # 0
```
16. `rindex(str, beg=0, end=len(string))` 类似index,不过是从右边开始找
```python
print('abca'.rindex('a')) # 3
print('abca'.index('a')) # 0
```
