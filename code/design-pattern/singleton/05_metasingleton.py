class MetaSingle(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingle, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
class Sql():
    def __init__(self):
        self.id = 0
        self.name = 'sql'
class Datebase(metaclass=MetaSingle):
    connection = None
    def connnect(self):
        if self.connection is None:
            self.connection = 'connection'
            self.cursorobj = Sql()
        return self.cursorobj

print(Datebase().connnect())
print(Datebase().connnect())
