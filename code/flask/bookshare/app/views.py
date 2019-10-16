from flask import render_template, url_for
from app import app

books = [
        {'name':'呐喊1','author':'鲁迅1','url':'http://www.baidu.com'},
        {'name':'呐喊2','author':'鲁迅2','url':'http://www.baidu.com'},
        {'name':'呐喊3','author':'鲁迅3','url':'http://www.baidu.com'},
        {'name':'呐喊4','author':'鲁迅4','url':'http://www.baidu.com'}
        ]
types = [
        {'name':'计算机','url':'type','tag':'1'},
        {'name':'小说','url':'type','tag':'2'}]

@app.route("/")
@app.route("/index/")
def index():
    for t in types:
        t['url'] = url_for('type', type=t['tag'])
    return render_template('index.html',types=types)

@app.route("/type/<type>")
def type(type):
    return render_template('type.html', type=type,books=books,types=types)
