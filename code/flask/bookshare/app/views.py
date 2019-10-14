from flask import render_template
from app import app

books = [
        {'name':'呐喊1','author':'鲁迅1','url':'http://www.baidu.com'},
        {'name':'呐喊2','author':'鲁迅2','url':'http://www.baidu.com'},
        {'name':'呐喊3','author':'鲁迅3','url':'http://www.baidu.com'},
        {'name':'呐喊4','author':'鲁迅4','url':'http://www.baidu.com'}
        ]

@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html')

@app.route("/type/<type>")
def type(type):
    return render_template('type.html', type=type,books=books)
    #return "type:%s" % type
