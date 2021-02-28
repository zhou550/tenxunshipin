from . import video_bp


@video_bp.route('/list')
def get_goods():
    return 'get goods'