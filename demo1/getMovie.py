#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : trimph
# @Site    :
# @File    :  获取网站电影的详细信息，并且保存下来
# @Software: PyCharm Community Edition

import requests
from  bs4 import BeautifulSoup


class GetMovies(object):


    def __init__(self):
        pass


    def initPage(self):

        response=requests.get("https://movie.douban.com/top250?start=0&filter=")
        esult = []
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            res_html = soup.prettify()  ## 装饰html

            #css 选择器 content > div > div.article > ol > li
            #// *[ @ id = "content"] / div / div[1] / ols / li[1]

            itemElement=soup.select("div.article > ol > li")

            print(len(itemElement))
            for ele in itemElement:
                 pciEle=ele.select("div.pic > a")
                 for picEle in pciEle:
                     # print(picEle.attrs["href"])
                     print(picEle.select_one("img").attrs["src"])

            # print(res_html)

if __name__ == '__main__':
    getMovie=GetMovies();
    getMovie.initPage()



