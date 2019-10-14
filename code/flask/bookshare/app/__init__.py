from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
from app import views, models

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop')
def initDB(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')

