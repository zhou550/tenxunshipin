import requests
from bs4 import BeautifulSoup


def scrapyrank(program):
    siderank = program.select("div.mod_column_side")[0]
    ranlitems = siderank.select(".mod_rank_list>a.rank_item")
    rankdict = {}
    ranklist = []
    for rankitem in ranlitems:
        rank_num = rankitem.select(".rank_num")[0].get_text()
        rank_title = rankitem.select(".rank_title")[0].get_text()
        rank_desc = rankitem.select(".rank_desc")[0].get_text()
        rank_update = rankitem.select(".rank_update")[0].get_text()
        rankitemdict = {"rank_num": rank_num, "rank_title": rank_title, "rank_desc": rank_desc,
                        "rank_update": rank_update}
        ranklist.append(rankitemdict)
    rankdict["name"] = siderank.h2.string
    rankdict["list"] = ranklist
    return rankdict


def scrapyprograme(program):
    mainprogram = program.select("div.mod_column_main")[0]
    programname = mainprogram.select("h2.mod_title>a")[0].get_text().replace("\n", "").replace(" ", "")
    programitems = mainprogram.select(".list_item")
    mainprogramlist = []
    for programitem in programitems:
        poster = programitem.select("img.figure_pic")[0].get("src")
        figure_title = programitem.select(".figure_detail>.figure_title")[0].get_text()
        figure_desc = programitem.select(".figure_detail>.figure_desc")[0].get_text()

        programitemdict = {"poster": poster, "figure_title": figure_title, "figure_desc": figure_desc}
        mainprogramlist.append(programitemdict)
    mainprogramdict = {"name": programname, "list": mainprogramlist}
    return mainprogramdict


def scrapysliders(bs):
    sliders = bs.select("div.site_slider>.slider_nav>.nav_link")[1:]
    sliderlist = []
    for slider in sliders:
        poster = slider.get("data-bgimage")
        title = slider.select(".title_text")[0].get_text()
        subtitle = slider.select(".text2")[0].get_text()
        subtitle = subtitle.replace(title, "")
        sliderdict = {"poster": poster, "title": title, "subtitle": subtitle}
        sliderlist.append(sliderdict)
    return  sliderlist


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

    # 缩进格式
    # print(bs.prettify())

    #


    program = bs.select("div#new_vs_hot_tv")[0]








