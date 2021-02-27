from flask import Flask, Blueprint

app = Flask(__name__, )

# 创建蓝图对象
index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@index_bp.route('/hello')
def hello():
    return 'hello'


# 注册蓝图
app.register_blueprint(index_bp)
# app.register_blueprint(user_bp, url_prefix='/user')


if __name__ == '__main__':
    app.run()
