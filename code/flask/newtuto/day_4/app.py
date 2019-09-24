import os
import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import click

prefix = 'sqlite:////'

app = Flask(__name__)
app.config.from_pyfile("config.py",silent=True)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, "data.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

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

@app.route('/')
def hello():
    return "hello"

@app.errorhandler(404)
def page_not_found(e):
    user = User.query.filter()
    return render_template('404.html', user=user), 404

@app.route('/index/')
def index():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

if __name__ == "__main__":
    app.run()
