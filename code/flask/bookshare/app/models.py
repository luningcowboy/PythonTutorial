from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    desc = db.Column(db.String)
    tag = db.Column(db.Integer)
    url = db.Column(db.String)
    author = db.Column(db.String)
    pic_url = db.Column(db.String)
    def __repr__(self):
        return '<Book %r>'%(self.name)

def getBooksByTag(tag):
    pass

