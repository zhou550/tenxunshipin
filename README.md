# tenxunshipin
模仿腾讯视频，爬虫程序
#1项目介绍
本项目为对腾讯视频网页的爬虫系统，包括爬虫程序，提供爬取数据的服务端程序及展示爬取信息的前端项目三个部分。
#2 选用的技术
采用Python语言来开发系统+vue构建页面
爬虫：requests+BeautifulSoup+pymysql
前端：vue（router，axios），ElementUI
后台：flask+flask_sqlalchemy

#3 安装与使用
1，数据库
创建数据库tenxunvideo，执行tenxunvideo.sql。

2，爬虫
pacong文件夹为爬虫项目，运行scrapvideos.py爬取视频数据，运行index.py爬取首页信息。

3，flask服务器
flask_server文件夹为flask服务器项目，运行app.py开启服务器。

4，vue客户端
vue_client为vue项目。
切换到该目录。
执行：
npm install #安装项目
npm run dev #运行项目

#截图

![avatar](https://github.com/zhou550/tenxunshipin/blob/main/vue_client/pic_index.png)
![avatar](https://github.com/zhou550/tenxunshipin/blob/main/vue_client/pic_videos.png)
