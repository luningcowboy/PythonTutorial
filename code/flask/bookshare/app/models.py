from app import db
"""
'name':'呐喊1'
'author':'鲁迅1'
'id':0
'desc':'这是一本关于呐喊的书'
'contents':['xxxxx','xxxx','xxxx']
'download':['https://www.baidu.com','https://www.baidu.com']
'pic_url':'http://haodoo.net/covers/17Z7.jpg'
'state':'是否可用'
"""
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    tag = db.Column(db.Integer)
    download = db.Column(db.String)
    author = db.Column(db.String)
    contents = db.Column(db.String)
    pic = db.Column(db.String)
    def __repr__(self):
        return '<Book %r>'%(self.name)
class BookType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.Integer)
    name = db.Column(db.String)
    subtag = db.Column(db.Integer)
    def __repr__(self):
        return '<BookType %r>'%(self.name)

def getBooksByTag(tag):
    pass

