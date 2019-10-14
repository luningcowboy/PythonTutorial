# -*- coding: utf-8 -*-
import os
try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin
from jinja2 import escape
from jinja2.utils import generate_lorem_ipsum
from flask import Flask, make_response, request, redirect, url_for, abort, session, jsonify

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')

@app.route('/')
@app.route('/hello/')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','Humans')
    response = '<h1> Hello , %s!</h1>' % escape(name)
    if 'logged_in' in session:
        response += '[Authenticated]'
    else:
        response += '[Not Authenticated]'
    return response

@app.route('/hi/')
def hi():
    return redirect(url_for('hello'))

@app.route('/goback/<int:year>/')
def go_back(year):
    return "welcome to %d" % (2019 - year)

@app.route('/colors/<any(blue, white, red):color>/')
def three_colors(color):
    return '<p>Love is patient and kind. Love is not jealous or boastful or proud or rude.</p>'

@app.route('/brew/<drink>/')
def teapot(drink):
    if drink == 'coffe':
        abort(418)
    else:
        return 'A drop of tea.'

@app.route('/404/')
def not_found():
    abort(404)

@app.route('/note', defaults={'content-type': 'text'})
@app.route('/note/<content_type>/')
def note(content_type):
    content_type = content_type.lower()
    if content_type == 'text':
        body = '''Note
        to: Peter
        from: Jane
        heading: Reminder
        body: Don't forget the party
        '''
        response = make_response(body)
        response.mimetypes = 'text/plain'
    elif content_type == 'html':
        body = '''
        <!DOCTYPE html>
        <html>
        <body>
  <h1>Note</h1>
  <p>to: Peter</p>
  <p>from: Jane</p>
  <p>heading: Reminder</p>
  <p>body: <strong>Don't forget the party!</strong></p>
</body>
        </html>
        '''
        response = make_response(body)
        response.mimetype = 'text/html'
    elif content_type == 'xml':
        body = '''
        <?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Peter</to>
  <from>Jane</from>
  <heading>Reminder</heading>
  <body>Don't forget the party!</body>
</note>
        '''
        response = make_response(body)
        response.mimetype = 'text/html'
    else:
        abort(400)
    return response

if __name__ == '__main__':
    app.run()
