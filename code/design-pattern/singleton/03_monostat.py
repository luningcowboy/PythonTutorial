# 状态共享
class Borg:
    __shared_state={'1':'2'}
    def __init__(self):
        self.__dict__ = self.__shared_state

b = Borg()
b1 = Borg()
print(b,b1)
