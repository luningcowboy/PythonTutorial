import os
import sys
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import click
from flask_login import LoginManager, login_user, logout_user

prefix = 'sqlite:////'

app = Flask(__name__)
app.config.from_pyfile("config.py",silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, "data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(28))
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.cli.command()
@click.option('--username',prompt=True, help='The username useed to login.')
@click.option('--password',prompt=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('Updatint user...')
        user.username = username
        user.password = password
        user.set_password(password)
    else:
        click.echo('Creating user...')
        user = User(username=username, name="Admin")
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('Done.')

@app.cli.command()
@click.option('--drop', is_flag=True, help="Create after drop")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initialized database")

@app.cli.command()
def forge():
    db.create_all()
    name = 'Peter'
    movies = [
            {'title': 'My Neighbor Totoro', 'year': '1988'},
            {'title': 'Dead Poets Society', 'year': '1989'},
            {'title': 'A Perfect World', 'year': '1993'},
            {'title': 'Leon', 'year': '1994'},
            {'title': 'Mahjong', 'year': '1996'},
            {'title': 'Swallowtail Butterfly', 'year': '1996'},
            {'title': 'King of Comedy', 'year': '1999'},
            {'title': 'Devils on the Doorstep', 'year': '1999'},
            {'title': 'WALL-E', 'year': '2008'},
            {'title': 'The Pork of Music', 'year': '2012'}
    ]
    user = User(name = name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()

login_manager = LoginManager(app)
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            flash("Invalid input.")
            return redirect(url_for('login'))
        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash("Login succes")
            return redirect(url_for('index'))
        flash("Invalid username or password")
        return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("GoodBye")
    return redirect(url_for('index'))

@app.route('/')
def hello():
    return "hello"

@app.errorhandler(404)
def page_not_found(e):
    user = User.query.filter()
    return render_template('404.html', user=user), 404

@app.route('/index/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')
        if not title or not year or len(year) > 4 or len(title) > 60:
            flash("Invalid input")
            return redirect(url_for('index'))
        movie = Movie(title=title, year=year)
        db.session.add(movie)
        db.session.commit()
        flash("Item created")
        return redirect(url_for('index'))
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

if __name__ == "__main__":
    app.run()
