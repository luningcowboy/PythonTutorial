from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run()
