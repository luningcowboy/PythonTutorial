from flask import Flask

app = Flask(__name__)
# 开启debug的第二种方法
#app.config.update(DEBUG=True)
# 开启debug的第三种方法
#app.config.debug = True
# 开启debug的第四种方法
#import config
#app.config.from_object(config)
'''
开启debug的第四种方法
1、这种方式加载配置，不局限于只能使用py文件，普通的txt文件同样适用
2、这个方式，可以传递silent=True，当这个配置文件没有找到的时候，不会抛出异常
'''
app.config.from_pyfile("config.txt",silent=True)
@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    #app.run()
    # 修改端口号
    #app.run(port=8000)
    # 修改绑定ip, 局域网内其他电脑也能访问
    app.run(host='0.0.0.0')
    # 开启debug模式
    #app.run(debug=True)
