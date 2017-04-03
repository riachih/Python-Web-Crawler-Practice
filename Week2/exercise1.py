#!/usr/bin/env python
#-*- coding: utf-8 -*-


import pymongo
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost',27017)
rental = client['rental']
xiaozhu = rental['xiaozhu']


def get_data(href):
    wb_data = requests.get(href)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('span.result_title')
    prices = soup.select('span.result_price > i')
    for title, price in zip(titles, prices):
        info = {
            'title': title.get_text(),
            'price': int(price.get_text())
        }
        xiaozhu.insert_one(info)


def get_link(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select("#page_list > ul > li > a")
    for link in links:
        href = link.get("href")  # !! notice
        get_data(href)

def find_xiaozhu():
    # 从xiaozhu数据库的fangzi表，查询所有数据，用find()函数
    for info in xiaozhu.find():
        # info 我们插入的数据都有title和price，我们取出每条信息的price，用来比较
        if info['price'] >= 500:
            print(info)


urls = ["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(str(i)) for i in range(1, 3)]
for url in urls:
        # 把得到的列表页面链接，传给函数，这个函数提取房子的标题和价格
    get_data(url)

#put it in the collection
