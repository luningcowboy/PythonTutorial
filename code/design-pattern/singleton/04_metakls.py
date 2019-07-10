# 元类: 一个类的类
class MyInt(type):
    def __call__(cls, *args, **kwds):
        print('MyInt call')
        return type.__call__(cls, *args, **kwds)
class int(metaclass=MyInt):
    def __init__(self,x,y):
        self.x = x
        self.y = y

i = int(4,5)
print(i)
