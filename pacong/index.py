import datetime

import requests
from bs4 import BeautifulSoup
import pymysql


# 爬取排名
def getrank(program):
    siderank = program.select("div.mod_column_side")[0]
    ranlitems = siderank.select(".mod_rank_list>a.rank_item")
    ranklist = []
    for rankitem in ranlitems:
        rank_num = rankitem.select(".rank_num")[0].get_text()
        rank_title = rankitem.select(".rank_title")[0].get_text()
        rank_desc = rankitem.select(".rank_desc")[0].get_text()
        rank_update = rankitem.select(".rank_update")[0].get_text()
        rankitemdict = {"sort": rank_num, "title": rank_title, "caption": rank_desc,
                        "description": rank_update}
        ranklist.append(rankitemdict)
    return ranklist


# 爬取节目（电影，电视剧等）
def getprograme(program):
    mainprogram = program.select("div.mod_column_main")[0]
    # programname = mainprogram.select("h2.mod_title>a")[0].get_text().replace("\n", "").replace(" ", "")
    programitems = mainprogram.select(".list_item")
    mainprogramlist = []
    for programitem in programitems:
        poster = programitem.select("img.figure_pic")[0].get("src")
        figure_title = programitem.select(".figure_detail>.figure_title")[0].get_text()
        figure_desc = programitem.select(".figure_detail>.figure_desc")[0].get_text()

        programitemdict = {"poster": poster, "title": figure_title, "figure_desc": figure_desc}
        mainprogramlist.append(programitemdict)
    return mainprogramlist


# 爬取轮播图
def scrapysliders(bs):
    sliders = bs.select("div.site_slider>.slider_nav>.nav_link")[1:]
    sliderlist = []
    for slider in sliders:
        poster = slider.get("data-bgimage")
        title = slider.select(".title_text")[0].get_text()
        subtitle = slider.select(".text2")[0].get_text()
        subtitle = subtitle.replace(title, "")
        sliderdict = {"img": poster, "title": title, "caption": subtitle}
        sliderlist.append(sliderdict)
    return sliderlist


def sqldictpara(dict, key):
    if key in dict:
        # if isinstance(dict[key],str):
        #     return dict[key]
        return dict[key]
    else:
        return None


def insertIndexs(indexs, indextype, indexdate):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 插入语句
    # values插入的字符串要加‘’      ！！！
    sql = """INSERT INTO indexitem(indextype,img,title,caption,description,link,sort,indexdate) VALUES (%s,      %s, %s,     %s,   %s,           %s, %s,  %s)"""
    try:
        # 执行sql语句
        for index in indexs:
            # exesql = sql % (
            #     indextype, sqldictpara(index,"img"),sqldictpara(index,"title"), sqldictpara(index,"caption"), sqldictpara(index,"description"),sqldictpara(index,"link"),sqldictpara(index,"sort"),indexdate )
            # print(exesql)
            # cursor.execute(exesql,(indextype, sqldictpara(index,"img"),sqldictpara(index,"title"), sqldictpara(index,"caption"), sqldictpara(index,"description"),sqldictpara(index,"link"),sqldictpara(index,"sort"),indexdate))
            # cursor.execute(exesql, (indextype, None,None,None,None,None,None,None))
            cursor.execute(
                "INSERT INTO indexitem(indextype,img,title,caption,description,link,sort,indexdate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (indextype, sqldictpara(index, "img"), sqldictpara(index, "title"), sqldictpara(index, "caption"),
                 sqldictpara(index, "description"), sqldictpara(index, "link"), sqldictpara(index, "sort"), indexdate))
            # 提交到数据库执行
            db.commit()
    except Exception as ex:
        print("出现如下异常%s" % ex)
        # 如果发生错误则回滚
        db.rollback()


if __name__ == '__main__':
    # 构造请求头字典
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    }

    # 实例化session对象
    session = requests.session()

    # 构造登陆请求参数字典
    data = {

    }

    # 打印需要登陆后才能访问的页面
    response = session.get('https://v.qq.com/', headers=headers)

    bs = BeautifulSoup(response.content.decode(), "html.parser")

    program = bs.select("div#new_vs_hot_tv")[0]
    tv_ranks = getrank(program)
    sliders=scrapysliders(bs)

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "Zhouhao96!", "tenxunvideo")

    insertIndexs(tv_ranks, "tv_rank", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    insertIndexs(sliders, "index_slider", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # 关闭数据库连接
    db.close()
