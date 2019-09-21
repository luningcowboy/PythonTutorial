from flask import Flask, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)
app.config.from_pyfile("config.txt",silent=True)

class TelephoneConveter(BaseConverter):
    regex = r'1[3458]\d{9}'

class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split("+")
    def to_url(self, value):
        return '+'.join(value)

app.url_map.converters['tel'] = TelephoneConveter
app.url_map.converters['list'] = ListConverter

@app.route('/my_tel/<tel:telephone>/')
def my_tel(telephone):
    return "你的手机号:{}".format(telephone)

@app.route('/posts/<boards>/')
def posts(boards):
    boards = boards.split('+')
    return str(boards)

@app.route('/')
def hello():
    return url_for('posts2',boards=['a', 'b'])

@app.route('/posts2/<list:boards>/')
def posts2(boards):
    return str(boards)

if __name__ == '__main__':
    app.run()
