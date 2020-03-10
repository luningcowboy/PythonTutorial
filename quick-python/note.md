# 语法整理
## 基础语法
1. 输出`print([params])`
2. 注释
```python
# 单行注释
"""
多行注释
多行注释
"""
'''
多行注释
多行注释
'''
```
3. 指定编码`# -*- coding: utf-8 -*-`
4. 条件判断:
```python
if True:
    print('true')
else:
    print('false')
```
5. 多行语句:
**注意:** 在`[],{},()`中包含多多行语句，不需要使用`\`来实现多行语句。
```python
total = item_one + \
        item_two
total = 1 + \
    2 \
    + 3
total = [1, 2, 
         3, 4,
         5]
```
6. 数字类型:
- `int` 整数，py3中只有长整数，没有py2中多`Long`
- `bool` 布尔值(`True`或`False`)
- `float` 浮点数(1.23 3E-2)
- `complex` 复数(1+2j, 1.1 + 2.2j)
7. 字符串:
- python中使用单引号或双引号完全相同
- 三引号(`'''`或`"""`)指定多行字符串
- 转义字符`\`
- 反斜杠可以用了转移，使用r可以让反斜杠不发生转义`r"this is a line with \n"`
- 使用`+`连接字符串，使用`*`重复字符串
- 字符串有两种索引方式:从左往右，从0开始，从右往左，从-1开始
- Python中字符串不能改变
- Python中没有单独多字符类型，一个字符长度就是1的字符串
- 字符串截取:`变量[头下标:尾下标:步长]`
8. 不换行输出, `end=`可以替换输出的结尾.
`print("x = ", a, end=" ")`
9. `import`和`from...import`倒入模块
`import` 倒入某个模块
`from ... import ...`从某个模块中倒入指定部分
10. 命令行参数:
使用`python -h`来查看命令行帮助信息
`python test.py arg1 arg2 arg3`运行时传入参数可以通过`sys.argv`获取传入的参数列表
`len(sys.argv)`获取传入的参数个数
`sys.argv[0]`表示脚本名称
11. 赋值操作: `counter = 100`
12. 多变量赋值: 
 ```python
 a = b = c = 1
 a, b, c = 1, 2, 'hello,world'
 ```
13. 数据类型:
标准数据类型: 
- Number(数字)
- String(字符串)
- List(列表)
- Tuple(元组)
- Set(集合)
- Dictionary(字典)
不可变数据: Number, String, Tuple
可变数据: List, Dictionary, Set
Number:
py3支持int, float, bool, complex(复数), 整型只有int,没有py2中的Long.
```python
a, b, c, d = 10, 1.1, False, 4+3j
print(type(a), type(b), type(c), type(d))
print(isinstance(a, int), isinstance(b, float), isinstance(c, bool), isinstance(d, complex))
```
**注意:**
a. 变量类型判断`type(v)`或者`isinstance(v, type)`,
`type`和`isinstance`的区别:
- `type`认为子类和父类不是同一类型
- `isinstance`认为子类是一种父类的类型
b. 在py2中是没有布尔类型的，它用数字0表示`False`,用1表示`True`.在py3中，把`True`和`False`定义成关键字了，但是，他们的值还是1和0,他们可以和数字相加。
14. `del`运算:可以使用`del`语句删除一些对象的引用
`del var1[,var2, var3[..., varN]]`
```python
del var
del var_1, var_2, var_3
```
15. 数值计算:
```python
a, b, c, d = 1, 2, 3, 4
print(a + b) # 加法
print(c - a) # 减法
print(c / b) # 除法，得到一个浮点数
print(c // b) # 除法， 得到一个整数
print(c % b) # 取余数
print(b ** c) # 乘方
```
**注意:**
- Python可以同时为多个变量赋值: `a = b = c = 1`, `a, b = 1, 2`
- 一个变量可以通过赋值指向不同类型的对象:
```python
a = 1
print(a)
a = 'hello'
print(a)
```
- 数值的除法包含两个运算符: `/`返回一个浮点数，`//`返回一个整数
- 在混合计算时，Python会把整型转换为浮点型

16. String(字符串)
字符串使用'或"括起来
```python
str = 'Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str + "TEST")
print('Ru\noob')
print(r'Ru\noob')
```
**注意:**
- 反斜杠可以用来转义,使用r可以让反斜杠不生效
- 字符串可以用+连接成一个字符串，可以用*重复
- 字符串有两种索引方式，从左到右以0开始，从右往左以-1开始
- python中的字符串不可以改变

17. List(列表)
```python
list = ['abcd', 123, 0.01, 'hello']
l2 = ['ddd', 1001]
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(l2 + list)
print(l2 * 2)
l3 = l2 * 2
print(l3)
```
**注意:**
- List写在方括号之间，元素用逗号隔开,没有类型限制
- 跟字符串一样可以被索引和切片
- 可以用加号拼接
- List中的元素是可以改变的
```python
def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output
print(reverseWords('I like runoob'))
```



## 库相关
1. 获取python保留字
```python
import keyword
print(keyword.kwlist)
```
2. `getopt`模块
`getopt`模块时专门用来处理命令行参数的模块，用于获取命令行选项和参数，也就是`sys.argv`.
支持短项模式(`-`)和长项模式(`--`)
`getopt.getopt(args, options[, long_options])`
- `args`: 命令行参数列表
- `options`: 以字符串的格式定义
- `long_options`: 以列表的格式定义
```python
import sys
import getopt
def usage():
    info = '''
    help info:
    -h hlep
    -i ip address
    -p port number
    '''

    print(info)

def main(argv):
    print('Test getopt')
    #print(getopt.__doc__)
    try:
        opts, args = getopt.getopt(argv, "hi:p:", ['help', 'ip=', 'port='])
        for name, value in opts:
            if name in ('-h', '--help'):
                usage()
            elif name in ('-i', '--ip'):
                print('ip = ', value)
            elif name in ('-p', '--port'):
                print('port = ', value)

    except getopt.GetoptError:
        usage()


if __name__ == '__main__':
    main(sys.argv[1:])
```
**说明:**
`opts, args = getopt.getopt(argv, "hi:p:", ['help', 'ip=', 'port='])`
这是核心语句，`h`后没有跟`:`表示这个命令不带参数,`hi:p:`这是短命令,`['help', 'ip=', 'port=']`这是长命令。
短命令后带有`:`,说明这个必须要有参数,长命令后带有`=`也是这个意思。
