## 字符串
1. 使用`'`或`"`来创建字符串
```python
str1 = 'Hello World'
str2 = "Hello Python"
```
2. 访问字符串中的值
python不支持单字符类型，也就是说不像其他语言有`char`类似的字符类型.
Python访问字符串，可以使用方括号来截取字符串
```python
str1 = 'Hello World'
str2 = 'Python'
print("str1[0]:", str1[0])
print("str2[1:5]:", str2[1:5])
```
3. 字符串更新
你可以截取字符串的一部分，跟其他字符串进行拼接。
```python
str1 = 'Hello World'
print('新字符串:', str1[:6] + 'AABBCC')
```
4. Python转义字符
- \ 在行为时， 续行符号
- \\ 反斜杠符号
- \' 单引号
- \" 双引号
- \a 响铃
- \b 退格
- \000 空
- \n 换行
- \v 纵向制表符
- \t 横向制表符
- \r 回车
- \f 换页
- \oyy 八进制数,yy表示字符,eg: \o12
- \xyy 十六进制数， yy 表示字符: eg: \x0A
- \other 其他字符以普通格式输出
5. 字符串运算符
- `+` 字符串拼接
- `*` 字符串重复输出
- `[]` 通过索引获取字符串中的字符
- `[:]` 截取字符串中的一部分,str[0,2]只有0,1这两个字符
- `in` 成员运算，如果包含则返回True
- `not in` 成员运算符,如果不包含则返回True
- `r/R` 原始字符串，所有字符串直接按照字面意思来使用，其中的转义字符无效
- `%` 格式化字符串

```python
a = 'Hello'
b = 'Python'
print('a + b :', a + b)
print('a * 2 :', a * 2)
print('a[1]:', a[1])
print('a[1:4]', a[1:4])
if 'H' in a :
    print('H in a')
else:
    print('H not in a')
if 'M' not in a:
    print('M not in a')
else:
    print('M in a')

print(r'\n')
print(R'\n')
```
6. 字符格式化
```python
print('我叫 %s 今年 %d 岁!'%('小明', 10))
```
- `%c` 格式化字符及其ASCII码
- `%s` 格式化字符串
- `%d` 格式化整数
- `%u` 格式化无符号整型
- `%o` 格式化八进制数
- `%x` 格式化16进制数
- `%X` 格式化16进制数(大写)
- `%f` 格式化浮点数
- `%e` 用科学计数法格式化浮点数
- `%E` 通%e
- `%g` %f和%e的简写
- `%G` %f和%E的简写
- `%p` 用16进制数格式化变量的地址
辅助操作指令:
- `*` 制定宽度或小数点精度
- `- `用作左对齐
- `+` 在正数前面显示加号
- `<sp>` 在正数前面显示空格
- `#` 在八进制前面显示0
- `0` 显示的数字前面显示0而不是默认的空格
- `%` %%输出一个%
- `(var)` 映射变量
- `m.n.` m是显示的最小总宽度， n是小数点后的为啥
python2.6后增加了格式化字符串的函数`str.format`,增强了字符格式化的功能.
```python
print("{} {}".format('hello', 'world'))
print("{0} {1}".format('hello', 'world'))
print("{0} {1} {0}".format('hello', 'world'))
print("NAME:{name},URL:{url}".format(name='百度', url='www.baidu.com'))
site = {"name": '百度', "url": 'www.baidu.com'}
print("Name: {name}, URL: {url}".format(**site))
my_list = ['百度', 'www.baidu.com']
print('Name: {0[0]}, URL: {0[1]}'.format(my_list)) # 0是必须的
```
