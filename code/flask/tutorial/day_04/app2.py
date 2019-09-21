from werkzeug.routing import BaseConverter
from flask import Flask
class TelephoneConveter(BaseConverter):
    regex = r'1[3458]\d{9}'
# 这里是定义数据类性的名字，并注册到url_map中
app = Flask(__name__)
app.config.from_pyfile("config.txt",silent=True)
app.url_map.converters['tel'] = TelephoneConveter
#然后我们就可以使用自定一的tel类型了
@app.route('/my_tel/<tel:telephone>')
def my_tel(telephone):
    return '您的手机号码是：{}'.format(telephone)

if __name__ == '__main__':
    app.run()
