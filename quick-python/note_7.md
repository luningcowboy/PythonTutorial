1. `rjust(width[,fillchar])` 返回一个原字符串右对齐，并使用空格填充至长度width的新字符串,长度小于指定长度则返回原字符
```python
str_1 = "abc"
print(str_1.rjust(10)) #        abc
print(str_1.rjust(10,"*")) # *******abc
```
2. `rstrip([chars])` 删除字符串右边的指定字符，默认为空格
```python
str_1 = 'abc   '
print(str_1.rstrip()) #abc
print('abc***'.rstrip('*')) #abc
```
3. `split(str="",num=string.count(str))` 通过分隔符对字符串进行切片
- `str` 分隔符
- `num` 分割次数，默认-1，即分割所有

```python
str_1 = 'abcxabcxabcxabcxabcxabc'
print(str_1.split('x')) # ['abc', 'abc', 'abc', 'abc', 'abc', 'abc']
print(str_1.split('x', 3)) #['abc', 'abc', 'abc', 'abcxabcxabc']
```

4. `str.splitlines([keepends])` 按照行分割(`\r, \r\n, \n`) 返回一个包含各行作为元素对列表，如果`keepends=False`不包含换行符,如果为True则保留换行符
```python
str_1 = 'ab c\n\nde fg\rkl\r\n'
print(str_1.splitlines()) #['ab c', '', 'de fg', 'kl']
print(str_1.splitlines(True)) #['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```

5. `str.startswidth(substr, beg=0, end=len(string))` 检查字符串是否以指定字符开头
```python
str_1 = 'this is string example'
print(str_1.startswith('this')) #True
print(str_1.startswith('string', 8)) #True
print(str_1.startswith('this', 2, 4)) #False
```

6. `str.strip([chars])` 用于移除字符串头尾指定对字符,默认为空格
```python
str_1 = '***abc***'
print(str_1.strip('*')) #abc
```

7. `str.swapcase()` 字符串中大写转换为小写，小写转换为大写
```python
str_1 = 'abcABC'
print(str_1.swapcase()) #ABCabc
```
