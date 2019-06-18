from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'
@app.route('/hello')
def hello_world():
    return 'Hello,World'
@app.route('/user/<username>')
def show_user_profiel(username):
    return 'User %s'%username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id
@app.route('/projects/')
def projects():
    return 'The projects page'
@app.route('/about')
def about():
    return 'The about Page'

if __name__ == '__main__':
    # 调试
    # app.debug = True
    # app.run(debug = True)
    app.run()
