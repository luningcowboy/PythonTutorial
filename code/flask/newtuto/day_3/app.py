from flask import Flask, render_template

app = Flask(__name__)
app.config.from_pyfile("config.py",silent=True)

@app.errorhandler(404)
def page_not_found(e):
    #user = User.query.first()
    return render_template('404.html', user='peter')

if __name__ == "__main__":
    app.run()
