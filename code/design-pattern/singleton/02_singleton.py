class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print('not init')
        else:
            print('created')
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
s1 = Singleton()
print(s1)
s2 = Singleton.getInstance()
print(s2)
