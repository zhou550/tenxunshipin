from flask import Flask, Blueprint, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
app = Flask(__name__, )


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Zhouhao96!@127.0.0.1:3306/tenxunvideo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # 显示生成的sql


app.config.from_object(Config)

db = SQLAlchemy(app)


class Video(db.Model):
    """用户基本信息表"""
    __tablename__ = 'video'

    id = db.Column('id', db.BigInteger, primary_key=True, doc='视频id')
    play_page = db.Column(db.String, doc='手机号')
    poster = db.Column(db.String, doc='手机号')
    banner = db.Column(db.String, doc='手机号')
    duration = db.Column(db.String, doc='手机号')
    score = db.Column(db.String, doc='手机号')
    title = db.Column(db.String, doc='手机号')
    sub_title = db.Column(db.String, doc='手机号')
    play_count = db.Column(db.String, doc='手机号')
    introduction = db.Column(db.String, doc='手机号')
    region = db.Column(db.String, doc='手机号')
    video_language = db.Column(db.String, doc='手机号')
    publish_time = db.Column(db.String, doc='手机号')

    def jsonstr(self):
        jsondata = {
            'id': self.id,
            'play_page': self.play_page,
            'poster': self.poster,
            'banner': self.banner,
            'duration': self.duration,
            'score': self.score,
            'title': self.title,
            'sub_title': self.sub_title,
            'play_count': self.play_count,
            'introduction': self.introduction,
            'region': self.region,
            'video_language': self.video_language,
            'publish_time': self.publish_time,
        }
        return jsondata



# 创建蓝图对象
index_bp = Blueprint('index', __name__)


@index_bp.route('/')
@index_bp.route('/hello')
def hello():
    return 'hello'


# 创建视频业务蓝图对象
video_bp = Blueprint('video', __name__)


def serialize(model):
    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]
    return dict((c, getattr(model, c)) for c in columns)


def returnjson(list):
    seriallist=[]
    for i in list:
        seriallist.append(serialize(i))
    return jsonify({"success": "1","data":seriallist})


@video_bp.route('/list')
def get_videos():
    offset = request.args.get('offset')
    pagesize = request.args.get('pagesize')

    query = Video.query.order_by(Video.id.desc())
    query = query.offset(offset).limit(pagesize)
    ret = query.all()
    print(ret)
    print(type(ret))
    return returnjson(ret)
    # return {"success": "1","data":ret}

# 注册蓝图
app.register_blueprint(index_bp)
app.register_blueprint(video_bp, url_prefix='/video')

if __name__ == '__main__':
    app.run()
