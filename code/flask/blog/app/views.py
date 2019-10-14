from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requreted for OpenID=' + form.openid.data + ', remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title="Sign In",form=form)
