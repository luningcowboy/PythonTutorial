from app import db
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    booktype = db.Column(db.String)
    download = db.Column(db.String)
    author = db.Column(db.String) 
    contents = db.Column(db.Text)
    pic = db.Column(db.String)
    def __repr__(self):
        return '<Book %r>'%(self.name)
    def getContents(self):
        return self.contents.split('\n')
    def getDownloads(self):
        return self.downloads.split(',')

