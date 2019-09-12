1. 数值交换
```python
# 错误的定义
tmp = a
a = b
b = tmp
# 更好的方法
a, b = b, a
```
2. 遍历
```python
# 错误的使用
length = len(alist)
i = 0
while i < length:
  dosomething(alist[i])
  i += 1
# 更好的方法
for i in alist:
  dosomething(i)
```
3. 安全的关闭文件描述符
```python
with open(path, 'r') as f:
  dosomething(f)
```
4. 应该充分利用python语法，但不应该过分追求奇技淫巧
```python
# 错误的用法
a = [1,2,3,4]
b = 'abcdef'
print(a[::-1])
print(b[::-1])
# 更好的方法
print (list(reversed(a)))
print (list(reversed(b)))
```
5. 字符串的格式化
```python
# 不好的方法
print('Hello %s'%('Tom'))
# %s是非常影响可读性的，因为数量多了以后很难清楚哪一个占位符对应哪一个实参
# 更好的方法
print('Hello %(name)s'%{'name':'Tom'})
value = {'greet':'Hello world','language':'python'}
print('%(greet)s from %(language)s'%value)
# 最好的方法
print('{greet} from {language}'.format(greet='Hello World', language='Python'))
```
6. 库和框架的规范
- 包和模块的命名采用小写和单数形式，而且短小
- 包通常仅作为命名空间，如只包含空的`__init__.py`文件
7. 避免劣化代码
- 避免只用大小写来区分不同的对象
- 避免使用容易引起混淆的名称
- 不要害怕过长的变量名
8. 三目运算符
```python
x = 0
y = -2
print(x if x < y else y)
```
9. `switch..case`
python中没有`switch...case`,但是有相应的替换方案:
```python
# 方案1:
x = ''
if n == 0:
  x = '0000'  
elif n == 1:
  x = '1111'  
else:
  x = 'xxxx'  
# 方案2
def func(x):
  return {
    0: "0000",
    1: "1111"
  }.get(x,'xxxxx')
```
10. 注释
- 块注释
- 行注释
- 文档注释

**注意:**
- 使用**块注释**和**行注释**的时候仅仅注释那些复杂的操作，算法，还有别人难以理解的技巧或者不够一目了然的代码。
- 注释和代码之间隔开一定的距离，同时在块注释后最好多留几行空白再写代码
- 给外部可访问的函数和方法(无论是否简单)添加文档注释，注释要清楚的描述方法的功能，并对参数，返回值以及可能发生的异常进行说明，使得外部调用他的人员仅仅看docstring就能正确使用。
- 在文件头添加copyright申明，模块描述，如果有必要，加入作者和变更记录
- 注释应该用来解释代码的功能，原因和想法，而不是对代码本身的解释
