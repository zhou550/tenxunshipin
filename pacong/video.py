# 版本二，使用装饰器property和setter
class Video:

    # 构造函数
    def __init__(self, play_page=None, poster=None, banner=None, duration=None, score=None, title=None, play_count=None,
                 region=None, introduction=None, sub_title=None,
                 video_language=None, publish_time=None):
        '''用双下划线开头的变量，表示私有变量，外部程序不可直接访问'''
        self.__play_page = play_page
        self.__poster = poster
        self.__banner = banner
        self.__duration = duration
        self.__score = score
        self.__title = title
        self.__video_language = video_language
        self.__publish_time = publish_time
        self.__play_count = play_count
        self.__region = region
        self.__introduction = introduction
        self.__sub_title = sub_title

    # getter
    @property
    def play_page(self):
        return self.__play_page

    # settter
    @play_page.setter
    def play_page(self, play_page):
        self.__play_page = play_page

    @property
    def poster(self):
        return self.__poster

    @poster.setter
    def poster(self, poster):
        self.__poster = poster

    @property
    def banner(self):
        return self.__banner

    @banner.setter
    def banner(self, banner):
        self.__banner = banner

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration):
        self.__duration = duration

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def poster(self):
        return self.__poster

    @poster.setter
    def poster(self, poster):
        self.__poster = poster

    @property
    def sub_title(self):
        return self.__sub_title

    @sub_title.setter
    def sub_title(self, sub_title):
        self.__sub_title = sub_title

    @property
    def play_count(self):
        return self.__play_count

    @play_count.setter
    def play_count(self, play_count):
        self.__play_count = play_count

    @property
    def video_language(self):
        return self.__video_language

    @video_language.setter
    def video_language(self, video_language):
        self.__video_language = video_language

    @property
    def introduction(self):
        return self.__introduction

    @introduction.setter
    def introduction(self, introduction):
        self.__introduction = introduction

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, region):
        self.__region = region

    @property
    def publish_time(self):
        return self.__publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        self.__publish_time = publish_time

    # 相当于java的toString方法
    def __str__(self):
        return "title:%s subtitle%s" % (self.__title, self.__sub_title)

    # 相当于java的toString方法
    def __repr__(self):
        return "姓名:%s 年龄%s" % (self.__name, self.__age)

    # 相当于java的equals方法
    def __eq__(self, other):
        if self.__name == other.name:  # 注意这里是改进之前的版本！！使用getter
            return True
        else:
            return False
