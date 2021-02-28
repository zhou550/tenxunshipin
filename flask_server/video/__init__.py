from flask import Blueprint

# 创建视频业务蓝图对象
video_bp = Blueprint('video', __name__)

from . import views

