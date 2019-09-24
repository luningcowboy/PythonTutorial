from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("config.py",silent=True)

@app.errorhandler(404)
def page_not_found():
    user = User.query.first()
    return render_template('404.html', user=user)

if __name__ == "__main__":
    app.run()
