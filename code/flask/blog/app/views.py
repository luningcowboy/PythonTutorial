from flask import render_template
from app import app

@app.route('/')
@app.route('/index/')
def index():
    user = {'nickname':'CowBoy'}
    posts = [
            {
                'author':{'nickname':'John'},
                'body':'Beautiful day in Portland!'
            },
            {
                'author':{'nickname':'Suan'},
                'body':'Beautiful day in Portland!'
            } ]
    #return render_template('index.html', user=user,title='Home')
    return render_template('index.html', user=user,posts=posts)