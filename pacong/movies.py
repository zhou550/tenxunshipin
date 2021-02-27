import requests
from bs4 import BeautifulSoup


def getMovies():
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
        "movie", 0, 30)
    # 打印需要登陆后才能访问的页面
    response = session.get(url, headers=headers)
    bs = BeautifulSoup(response.content.decode(), "html.parser")
    # 缩进格式
    # print(bs.prettify())
    list_items = bs.select("div.list_item")
    movies = []
    for list_item in list_items:
        playPage = list_item.select("a.figure")[0].get("href")
        poster = list_item.select("img.figure_pic")[0].get("src")
        print(poster)
        print(list_item.select("a.figure"))
        caption = list_item.select(".figure_caption")[0].get_text()

        score = list_item.select(".figure_score")[0].get_text()
        title = list_item.select("div.figure_detail>a.figure_title")[0].get_text()
        desc = list_item.select("div.figure_detail>.figure_desc")[0].get_text()
        playCount = list_item.select("div.figure_count")[0].get_text()
        movie = {
            "playPage": playPage,
            "poster": poster,
            "caption": caption,
            "score": score,
            "title": title,
            "desc": desc,
            "playCount": playCount,
        }
        movies.append(movie)
        return  movies


if __name__ == '__main__':
    getMovies()


