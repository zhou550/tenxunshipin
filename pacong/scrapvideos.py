import requests
from bs4 import BeautifulSoup
import pymysql

from pacong.video import Video


def scrapVideos(type, offset, pagesize):
    # 构造请求头字典
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    }
    # 实例化session对象
    session = requests.session()
    # 构造登陆请求参数字典
    data = {
    }
    url = "https://v.qq.com/x/bu/pagesheet/list?append=1&channel=%s&itype=100062&listpage=2&offset=%d&pagesize=%d" % (
        type, offset, pagesize)
    # 打印需要登陆后才能访问的页面
    response = session.get(url, headers=headers)
    bs = BeautifulSoup(response.content.decode(), "html.parser")
    # 缩进格式
    # print(bs.prettify())
    list_items = bs.select("div.list_item")
    videos = []
    for list_item in list_items:
        if len(list_item.select("a.figure")) > 0:
            playPage = list_item.select("a.figure")[0].get("href")
        if len(list_item.select("img.figure_pic")) > 0:
            poster = list_item.select("img.figure_pic")[0].get("src")
        if len(list_item.select(".figure_caption")) > 0:
            caption = list_item.select(".figure_caption")[0].get_text()
        if len(list_item.select(".figure_score")) > 0:
            score = list_item.select(".figure_score")[0].get_text()
        if len(list_item.select("div.figure_detail>a.figure_title")) > 0:
            title = list_item.select("div.figure_detail>a.figure_title")[0].get_text()
        if len(list_item.select("div.figure_detail>.figure_desc")) > 0:
            desc = list_item.select("div.figure_detail>.figure_desc")[0].get_text()
        if len(list_item.select("div.figure_count")) > 0:
            playCount = list_item.select("div.figure_count")[0].get_text()
        video = Video()
        video.play_page = playPage
        video.poster = poster
        video.score = score
        video.title = title
        video.sub_title = desc
        video.play_count = playCount
        video.duration=caption
        videos.append(video)
    return videos


def insertVideos(videos):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    # values插入的字符串要加‘’      ！！！
    sql = """INSERT INTO VIDEO(play_page,poster,banner,duration,score,title,sub_title,play_count,introduction,region,video_language,publish_time)
                        VALUES ('%s','%s', '%s','%s','%s','%s', '%s', '%s', '%s','%s','%s','%s')"""
    try:
        # 执行sql语句
        for video in videos:
            exesql = sql % (
                video.play_page, video.poster, video.banner, video.duration, video.score, video.title, video.sub_title,
                video.play_count, video.introduction, video.region, video.video_language, video.publish_time)
            print(exesql)
            cursor.execute(exesql)
            # 提交到数据库执行
            db.commit()
    except Exception as ex:
        print("出现如下异常%s" % ex)
        # 如果发生错误则回滚
        db.rollback()


if __name__ == '__main__':

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "Zhouhao96!", "tenxunvideo")

    start = 0
    end = 3000
    pagesize = 30
    type = "movie"
    cur = start
    while cur < end:
        videos = scrapVideos(type, cur, pagesize)
        cur += pagesize

        insertVideos(videos)

    # 关闭数据库连接
    db.close()
