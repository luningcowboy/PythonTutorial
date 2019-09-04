from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {"nickname":"Miguel"}
    posts = [
        {
            'author':{'nickname':'Jhon'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author':{'nickname':'Susan'},
            'body': 'The Avengers moie was so cool!'
        }
    ]
    return render_template('index5.html',
            title = "Home",
            user = user,
            posts = posts)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Requested fo OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
            title = 'Sign In',
            form = form)
