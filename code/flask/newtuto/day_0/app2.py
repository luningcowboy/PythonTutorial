from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/user/<name>/')
def user_page(name):
    return "User: %s" % name

@app.route('/test/')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='user'))
    print(url_for('user_page',name='peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for',num = 2))
    return "Test page"

if __name__ == '__main__':
    app.run()

