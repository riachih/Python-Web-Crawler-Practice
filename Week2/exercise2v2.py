#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests
import time
import pymongo
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost', 27017)
cellphonev2 = client['cellphonev2']
urlsv3 = cellphonev2['urlsv3']
productv2 = cellphonev2['productv2']

#level one: obtain the titles and link in the cell phone number page:
def get_link_from(pages,who_sells=0):
    #channel extract list
    #http://bj.58.com/diannao/0/pn2
    # who sells + page number
    url = 'http://bj.58.com/shoujihao/pn{}/'.format(str(pages))
    #channel replaces the first one, who sells replaces the second one.
    #str function: transform to character
    wb_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('#infolist > div > ul > div.boxlist > ul > li > a.t > strong')
    links = soup.select('#infolist > div > ul > div.boxlist > ul > li > a.t')

    for title, link in zip(titles, links):
        data = {
            # 由于标题的文本内容在<strong></strong>标签之间，用get_text()提取
            'title': title.get_text(),

            # 由于链接地址在标签的href属性里面，所以用get提取
            'url': link.get('href')
        }-

        print(data)
        urlsv3.insert_one(data)

# def get_links_from(page):
# 	# 根据列表页面链接规律，拼接列表页面地址
#     url = 'http://bj.58.com/shoujihao/pn{}/'.format(page)
#
#     # 请求列表页面地址
#     wb_data = requests.get(url)
#
#     # 延时一秒钟，太快容易被封IP
#     time.sleep(1)
#
#     # 开始解析网页数据
#     soup = BeautifulSoup(wb_data.text, 'lxml')
#
#     # 鼠标放到每个小方格的手机号上，右键，审查元素，再右键，提取Css Path
#     titles = soup.select('#infolist > div > ul > div > ul > li > a.t > strong')
#
#     # 鼠标再放到链接的标签上，右键，提取Css Path
#     links = soup.select('#infolist > div > ul > div > ul > li > a.t')
#
#     # 由于soup.select得到的是列表，需要用for一个个遍历出来
#     for title, link in zip(titles, links):
#         data = {
# 	        # 由于标题的文本内容在<strong></strong>标签之间，用get_text()提取
#             'title': title.get_text(),
#
#             # 由于链接地址在标签的href属性里面，所以用get提取
#             'url': link.get('href')
#         }
#
#         print(data)
#
#         # 插入数据库，注意不要搞混shoujihao和infos数据库
#         urlsver2.insert_one(data)


#get the single url from database
#visit these product links
#get data and save it in the second data base
def get_info(url):
    wb_data = requests.get(url)

    time.sleep(1)

    soup=BeautifulSoup(wb_data.text,'lxml')

    titles = soup.select('#main > div.col.detailPrimary.mb15 > div.col_sub.mainTitle > h1')

    prices = soup.select('#main > div.col.detailPrimary.mb15 > div.col_sub.sumary > ul > li > div.su_con > span')

    for title, price in zip(titles,prices):
        title_text = title.get_text()

        # 由于价格的文本内容在<span></span>标签之间，用get_text()提取
        price_text = price.get_text()

        data = {
            "url": url,
            # 提取的内容有很多空白字符，需要replace替换掉
            "title": title_text.replace("\n", "").replace("\t", "").replace(" ", ""),
            "price": price_text.replace("\n", "").replace("\t", "").replace(" ", "")
        }
        print(data)
        productv2.insert_one(data)

for i in range(1,3):
     get_link_from(i)

for info in urlsv3.find():
    link = info['url']

    get_info(link)
