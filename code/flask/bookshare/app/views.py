from flask import render_template, url_for, redirect
from app import app

books = [
        {'name':'呐喊1','author':'鲁迅1','id':0,'desc':'这是一本关于呐喊的书','contents':['xxxxx','xxxx','xxxx'],'download':['https://www.baidu.com','https://www.baidu.com']},
        {'name':'呐喊2','author':'鲁迅2','id':1,'desc':'这是一本关于呐喊的书','contents':['xxxxx','xxxx','xxxx'],'download':['https://www.baidu.com','https://www.baidu.com']},
        {'name':'呐喊3','author':'鲁迅3','id':2,'desc':'这是一本关于呐喊的书','contents':['xxxxx','xxxx','xxxx'],'download':['https://www.baidu.com','https://www.baidu.com']},
        {'name':'呐喊4','author':'鲁迅4','id':3,'desc':'这是一本关于呐喊的书','contents':['xxxxx','xxxx','xxxx'],'download':['https://www.baidu.com','https://www.baidu.com']}
        ]
types = [
        {'name':'计算机','tag':'1'},
        {'name':'小说','tag':'2'}]
def getTypes():
    ret = []
    for t in types:
        t['url'] = url_for('type', type=t['tag'])
        ret.append(t)
    return ret
def getBooks():
    ret = []
    for b in books:
        b['url'] = url_for('book_desc', book_id=b['id'])
        ret.append(b)
    return ret

@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html',types=getTypes())

@app.route("/type/<type>")
def type(type):
    tmpBooks = getBooks()
    return render_template('type.html', type=type,books=books,types=getTypes())

@app.route("/book_desc/<book_id>")
def book_desc(book_id):
    if not book_id:
        return redirect(url_for('index.html'))
    tmpBooks = getBooks()
    bookInfo = tmpBooks[int(book_id)]
    app.logger.info("book_desc", bookInfo['url'])
    return render_template('book_desc.html', bookInfo=bookInfo, types=getTypes())
