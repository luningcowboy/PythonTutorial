from flask import Flask, request

app = Flask(__name__)
app.config.from_pyfile("config.txt",silent=True)
"""注意:
在定义url的时候，一定记得在最后加一个斜杠，
1、如果不加斜杠，那么在浏览器中访问这个url的时候最后加了斜杠，那么就访问不到了，用户体验不好
2、搜索引擎会将不加斜杠的和加斜杠的视为不同的url，而实际上是同一个，那么会给浏览器造成一个误解，加了斜杠就不会出现斜杠的问题
"""

@app.route("/")
def hello():
    return "hello"

@app.route("/article_list/")
def acticle_list():
    return "ActicleList"

@app.route("/article/<article_id>/")
def acticle_detail(article_id):
    return "您请求的文章是:{}".format(article_id)

# 限制参数类型
@app.route("/article2/<int:article_id>/")
def acticle_detail2(article_id):
    return "您请求的文章是:{}".format(article_id)
"""
类型可以设置提下几种：
　　string: 默认的数据类型，接收没有任何斜杠"\   /"的文本
　　int: 整数形
　　float: 浮点型
　　path: 和string类似，但是接受斜杠
　　uuid: 只接受uuid字符串
　　any: 可以指定多种路径，比如以下例子
"""
@app.route("/article3/<any(article,blog):url_path>/<id>/")
def acticle_detail3(url_path, id):
    if url_path == 'article':
        return "文章详情:{}".format(id)
    else:
        return "博客详情:{}".format(id)

"""
?key=value形式传参
"""
@app.route("/d/")
def d():
    wd = request.args.get("wd")
    return "你传递的参数是:{}".format(wd)


if __name__ == '__main__':
    app.run()
