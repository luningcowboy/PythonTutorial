from flask import Flask, url_for, request, redirect

app = Flask(__name__)
app.config.from_pyfile("config",silent=True)

@app.route("/list/", methods=["GET", "POST"])
def my_list():
    return 'list'

@app.route("/login/", methods=["GET", "POST"])
def login():
    return 'login page'

@app.route("/profile/", methods=["GET", "POST"])
def profile():
    name = request.args.get("name")
    if not name:
        return redirect(url_for('login'))
    else:
        return name

if __name__ == '__main__':
    app.run()
