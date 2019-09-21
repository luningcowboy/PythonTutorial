from flask import Flask, url_for



app = Flask(__name__)
app.config.from_pyfile("config.txt",silent=True)

@app.route('/')
def hello():
    return url_for("my_list")

@app.route('/list/')
def my_list():
    return "list package"

@app.route("/hello2/")
def hello2():
    return url_for("my_list2",page_id=2, count=2)

@app.route('/list2/<page_id>/')
def my_list2(page_id):
    return "list page2"

if __name__ == "__main__":
    app.run()
