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
18. Tuple(元组)
元组与列表类似，不同之处在于元组的元素不能修改，元组写在`()`里。
```python
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple * 2)
print(tuple + tinytuple)
```
**注意:**
- 与字符串一样，元组的元素不能修改
- 元组也可以被索引和切片，方法一样
- 注意构造包行0/1个元素的元组的特殊语法规则
- 元组也可通过+和*进行拼接操作

19. Set(集合)
是由一个或数个形态各异的大小整体组成的，构成集合的食物或对象称为元素或是成员。
```python
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
if 'Rose' in student:
    print('Roese 在集合中')
else:
    print('Rose 不在集合中')
a = set('abcdefghijklmn')
b = set('abacdefad')

print(a)
print(a - b) # a 和 b 的差集
print(a | b) # 并集
print(a & b) # 交集
print(a ^ b) # 不同时存在的元素
```

20. Dictionary(字典)
```python
dict = {}
dict['one'] = '1 - 菜鸟教程'
dict[2] = '2 - 菜鸟工具'

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'])
print(dict[2])
print(dict.keys())
print(dict.values())
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
```

21. 数据类型转换

`int(x, base=10)` 用于将一个字符串或数字转换为整型
- x: 字符串或数字
- base: 进制数，默认10进制
```python
print(int())
print(int(3))
print(int(3.6))
print(int('12', 16))
print(int('0xa', 16))
print(int('10', 8))
```
`float([x])` 将整数或者字符串转换为浮点数
- x: 整数或字符串
```python
print(float(1))
print(float())
print(float('123'))
print(float(-123.4))
```
`complex([real[,imag]])`
- real: int, long, float或字符串
- imag: int, long, float
返回一个复数
```python
print(complex(1, 2))
print(complex(1))
print(complex('1'))
print(complex("1+2j"))# 不能加空格
```
`str(object='')`将对象转换为字符串
- object: 对象
```python
s = 'RUNOOB'
print(str(s))
dict = {'runoob': 'runoob.com', 'google': 'google.com'}
print(str(dict))
```
`repr(object)`将对象转换为供解释器读取的形式.
```python
s = 'RUNOOB'
dict = {'runoob': 'runoob.com', 'google': 'google.com'}
print(repr(s))
print(repr(dict))
```
`eval[expression[,globals[, locals]]]`
- expression: 表达式
- globals: 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象
- locals: 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
```python
x = 7
print(eval('3*x'))
print(eval('pow(2,2)'))
print(eval('2 + 2'))
n = 81
print(eval('n + 4'))
```
`tuple(iterable)` 将可迭代系列(如:List)转换为元组
- iterable: 需要转换为元组的可迭代序列
```python
list1 = ['Google', 'Taobao', 'Baidu']
tuple1 = tuple(list1)
print(tuple1)
```
`list(seq)` 用于将元组或字符串转换为列表。
```python
aTuple = (123, 'Google', 'Baidu', 'Taobao')
list1 = list(aTuple)
print(list1)
s = 'abcdeft'
list2 = list(s)
print(list2)
```
`set([iterable])`创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集，差集，并集。
- iterable: 可迭代对象
```python
x = set('runoob')
y = set('google')
print((x, y)) # 重复的元素被删除
print(x & y) # 交集
print(x | y) # 并集
print(x - y) # 差集
```
`dict()` 用于创建一个字典
- `dict(**kwarg)`
- `dict(mapping, **kwarg)`
- `dict(iterable, **kwarg)`
- `kwarg`: 关键字
- `mapping`: 元素的容器
- `iterable`: 可迭代对象
```python
print(dict())
print(dict(a = 'a', b= 'c', c = 1, d = 2))
print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))
print(dict([('one', 1), ('two', 2), ('three', 3)]))
```
`frozenset([iterable])`返回一个冰冻集合，不能添加或删除任何元素。
- iterable: 可迭代对象，比如:列表， 字典， 元组等. 
```python
a = frozenset(range(10))
print(a)
b = frozenset('runoob')
print(b)
```
`chr()`用范围在rang(256)内(就是0-255)的整数做参数，返回一个对应的字符。
```python
print(chr(0x30), chr(0x31), chr(0x61))
print(chr(48), chr(49), chr(97))
```
`ord(c)`获取一个字符的编码
- c: 字符
```python
print(ord('a'))
print(ord('b'))
print(ord('c'))
```
`hex(x)`用于将10进制整数转换成16进制字符串，以字符串形式表示。
- x: 10进制整数
```python
print(hex(255))
print(hex(-42))
print(hex(12))
print(type(hex(12)))
```

`oct(x)`将一个整数转换成8进制字符串.
```python
print(oct(10))
print(oct(20))
print(oct(15))
print(type(oct(15)))
```

21. 算数运算符:
- `+`加法运算符
- `-`减法运算符
- `*`乘法运算符
- `/`除法运算符
- `%`取模运算符
- `**`幂运算符
- `//`取整运算符
```python
a = 21
b = 10
c = 0
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
```
22. 比较运算符
- `==` 判断比较对象是否相等
- `!=` 不等于
- `>` 大于
- `<` 小于
- `>=` 大于等于
- `<=` 小于等于
```python
a = 21
b = 10
c = 0
if (a == b):
    print('a==b')
else:
    print('a!=b')

if (a != b):
    print('a!=b')
if (a < b):
    print('a < b')
if (a > b):
    print('a > b')
a = 5 
b = 20
if (a <= b):
    print('a <= b')
else:
    print('a > b')
if (b >= a):
    print('b >= a')
```
23. 赋值运算符
- `=` 简单的赋值运算符
- `+=` 加法赋值运算符
- `-=` 减法赋值运算符
- `*=` 乘法赋值运算符
- `/=` 除法赋值运算符
- `%=` 取模赋值运算符
- `**=` 幂赋值运算符
- `//=` 取整赋值运算符
- `:=` 还像运算符,可在表达式内部为变量赋值(3.8提供)
```python
a = 21
b = 10
c = 0
c = a + b
print(c)
c += a
print(c)
c *= a
print(c)
c /= a
print(c)
c = 2
c %= a
print(c)
c **= a
print(c)
c //= a
print(c)
```
24. 位运算符
- `&` 按位与运算符
- `|` 按位或运算符
- `^` 按位异或运算符
- `<<` 左移动运算符
- `>>` 右移动预算符
```python
a = 60
b = 13
c = 0
c = a & b
print(c)
c = a | b
print(c)
c = a ^ b
print(c)
c = ~a
print(c)
c = a << 2
print(c)
c = a >> 2
print(c)
```
25. 逻辑运算符
- and `x and y`
- or `x or y`
- not `not x`
```python
a = 10
b = 20
if (a and b):
    print('a and b true')
else:
    print('a and b false')
if (a or b):
    print('a or b true')
else:
    print('a or b false')

a = 0
if (a and b):
    print('a and b true')
else:
    print('a and b false')
if (a or b):
    print('a or b true')
else:
    print('a or b false')
if not (a and b):
    print('not (a and b) true')
else:
    print('not (a and b) false')
```
26. 成员运算符
- in 在制定序列中找到指定值返回`True`,否则返回`False`
- not in 在指定序列中没有找到指定值返回`True`, 否则返回`False`
```python
a = 10
b = 20
list1 = [1, 2, 3, 4, 5]
print(a in list1)
print(a not in list1)
```
27. 身份运算符
- is 判断两个标识符是不是引用字一个对象
- is not 判断两个标识符是不是引用字不同对象
```python
a = 20
b = 20
if (a is b):
    print('a is b')
else:
    print('a is not b')
if (id(a) == id(b)):
    print('相同标识')
else:
    print('不同标识')
```

28. Number(数字)
数字不允许改变，如果修改数字数据类型的值，**将重新分配内存空间**。
创建数字对象
```python
var1 = 1
var2 = 10
```
使用`del var1[, var2[,var3[..., varN]]]` 删除数字对象的引用.
```python
var1 = 1
var2 = 10
print(var1, var2)
del var1, var2
print(var1, var2) # 这里会报错:NameError: name 'var1' is not defined
```
三种数据类型:
- `整型(int)`:py3中没有`Long`, 整型没有大小限制，可以当作`Long`使用
- `浮点型(float)`:由整数和小数组成，也可以使用科学计数法表示
- `复数(complex)`:由实数和虚数部分组成

29. 数字转换:
- `int(x)`:将x转换为整数
- `float(x)`:将x转换为浮点数
- `complex(x)`:将x转换为复数
- `complex(x, y)`:将x,y转换到一个复数
30. 数字函数:
- `abs(x)` 返回数字的绝对值
- `ceil`: 返回数字的上入整数`math.ceil(4.1)`返回5,也就是向上取整
- `cmp(x, y)`: python3已经弃用
- `exp(x)`: 返回e的x次幂
- `fabs(x)`:返回数字的绝对值
- `floor(x)`: 返回数字的下舍整数,即向下取整
- `log(x)`: `math.log(100, 10)`返回2.0
- `log10(x)`:返回以10为基数的x的对数
- `max(x1, x2...)`: 返回给定序列的最大值
- `min(x1, x2...)`: 返回给定序列的最小值
- `modef(x)`: 返回x的整数部分与小数部分
- `pow(x, y)`: x**y运算后的值
- `round(x[,n])`: 返回x的四舍五入值
- `sqrt(x)`:返回数字的x平方根
**注意:**
`fabs`和`abs`的区别:
- `abs`是一个内置函数，而`fabs`在`math`模块中
- `fabs`只适用于`float`和`integer`类型，而`abs`可用于复数
```python
print(abs(-40))
print(abs(-1.02))
import math
print(math.fabs(-40))
print(math.fabs(-1.02))
print(math.ceil(1.1)) # 2
print(math.ceil(-1.1)) # -1
print(math.exp(100))
print(math.floor(1.8)) # 1
print(math.floor(-1.8)) # -2
print(math.log(100, 10)) # 2.0
print(max(1,2,3,4,5)) # 5
print(max([1,2,30,4,5])) # 30
print(min(1, 2, 3, 4, 5)) # 1
print(min([1,2,30,4,5])) # 1
print(math.modf(1.21)) # (小数部分，整数部分)
print(pow(2, 3))
print(round(1.3), round(1.8))
print(math.sqrt(100))
```
31. 随机函数
- `choice(seq)`: 从序列元素中随机挑选一个元素
- `randrange([start,], stop [, step])`:从指定范围按指定基数递增的集合中获取一个随机数,基数默认值为1
- `random`: 随机生成下一个实数
- `seed(x)`: 改变随机数生成器的种子`seed`
- `shuffle(list)`: 洗牌算法
- `uniform(x, y)`: 随机生成下一个实数,在[x,y]范围内
```python
import random
print(random.choice([1,2,3,4,5]))
print(random.choice(range(100)))
print(random.choice('HelloPython'))
print(random.randrange(2, 10, 2))
print(random.random())
random.seed(10)
print(random.random())
random.seed(10)
print(random.random())
l = [1,2,3,4,5]
print(l)
random.shuffle(l)
print(l)
random.seed()
```

32. 三角函数:`sin, cos, tan, asin, acos, atan`
- `atan2(y, x)`: 给定x,y坐标的反正切值
- `hypot(x, y)`: 欧几里得范数sqrt(x*x + y*y)
- `degrees(x)`: 弧度转换为角度
- `radians(x)`: 角度转换为弧度

33. 数字常量:
- `pi`
- `e`: 数字常量e, e即自然常数


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
