#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
import requests
import pymongo
import random

client = pymongo.MongoClient('localHost', 27017)
ganji = client['ganji']
link_list = ganji['link_list']
product_info = ganji['product_info']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection': 'keep-alive'
}

# http://cn-proxy.com/
proxy_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
]
# 随机获取代理ip
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}


# 获取所有的列表页面链接
def get_channel_link_list(channel, page, who_sell='o'):
    # http://bj.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    url = '{}{}{}/'.format(channel, who_sell, page)
    wb_data = requests.get(url, headers=headers, proxies=proxies)
    print('yes')
    # 检查页面是否不存在，或者被封ip
    if wb_data.status_code == 200:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        for link in soup.select('.fenlei dt a'):
            item_link = link.get('href')
            link_list.insert_one({'url': item_link})
            print(1)
            get_product_info(item_link)
            print(item_link)


# 获取指定链接页面详细信息
def get_product_info(url, data=None):
    wb_data = requests.get(url, headers=headers)
    # 检查页面是否不存在，或者被封ip
    if wb_data.status_code != 200:
        return

    soup = BeautifulSoup(wb_data.text, 'lxml')

    prices = soup.select('.f22.fc-orange.f-type')
    pub_dates = soup.select('.pr-5')
    areas = soup.select('ul.det-infor > li:nth-of-type(3) > a')
    cates = soup.select('ul.det-infor > li:nth-of-type(1) > span')

    data = {
        'title': soup.title.text.strip(),
        'price': prices[0].text.strip() if len(prices) > 0 else 0,
        'pub_date': pub_dates[0].text.strip().split(' ')[0] if len(pub_dates) > 0 else "",
        'area': [area.text.strip() for area in areas if area.text.strip() != "-"],
        'cates': [cate.text.strip() for cate in cates],
        'url': url
    }
    print(data)
    product_info.insert_one(data)

get_channel_link_list('http://bj.ganji.com/wupinjiaohuan/',1)

# # headers  = {
# #     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
# #     'Connection':'keep-alive'
# # }
# #
# # # http://cn-proxy.com/
# # proxy_list = [
# #     'http://117.177.250.151:8081',
# #     'http://111.85.219.250:3129',
# #     'http://122.70.183.138:8118',
# #     ]
# #
# # proxy_ip = random.choice(proxy_list)
# # proxies = {'http': proxy_ip}
# #
# # #get link list under different channels
# # def get_channel_link_list(channel,page,who_sell='o'):
# #     single_link = '{}{}{}/'.format(channel, who_sell, page)
# #     #http://bj.ganji.com/yingyouyunfu/o3/
# #     #http://bj.ganji.com/wupinjiaohuan/
# #     wb_data = requests.get(single_link, headers=headers, proxies=proxies)
# #     time.sleep(1)
# #     soup = BeautifulSoup(wb_data.text,'lxml')
# #     #check if the link list page is valid
# #     if wb_data.status_code == 200:
# #         soup = BeautifulSoup(wb_data.text, 'lxml')
# #         links = soup.select('.fenlei dt a')
# #         for link in links:
# #             item_link = link.get('href')
# #             link_list.insert_one({'url': item_link})
# #             get_product_info(item_link)
# #             print(item_link)
# #
# # def get_product_info(url):
# #     #now we go into the product page
# #     wb_data = requests.get(url,headers=headers)
# #     no_longer_exit = (wb_data.status_code != 200)
# #     if no_longer_exit:
# #         pass
# #     else:
# #         soup = BeautifulSoup.get(wb_data.text, 'lxml')
# #     #title, released date, category, price, area, new/old degree
# #         # titles = soup.select('#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > h1')
# #         # dates = soup.select('#wrapper > div.content.clearfix > div.leftBox > div > div > ul > li > i')
# #         # areas = soup.select('#wrapper > div.content.clearfix > div.leftBox > div > div > ul > li ')
# #         # prices = soup.select('#wrapper > div.content.clearfix > div.leftBox > div > div > ul > li > i')
# #         prices = soup.select('.f22.fc-orange.f-type')
# #         pub_dates = soup.select('.pr-5')
# #         areas = soup.select('ul.det-infor > li:nth-of-type(3) > a')
# #         cates = soup.select('ul.det-infor > li:nth-of-type(1) > span')
# #         data = {
# #             'title': soup.title.text.strip(),
# #             'price': prices[0].text.strip() if len(prices) > 0 else 0,
# #             'pub_date': pub_dates[0].text.strip().split(' ')[0] if len(pub_dates) > 0 else "",
# #             'area': [area.text.strip() for area in areas if area.text.strip() != "-"],
# #             'cates': [cate.text.strip() for cate in cates],
# #             'url': url
# #         }
# #         print(data)
# #         product_info.insert_one(data)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
#     'Connection': 'keep-alive'
# }
# 
# # http://cn-proxy.com/
# proxy_list = [
#     'http://117.177.250.151:8081',
#     'http://111.85.219.250:3129',
#     'http://122.70.183.138:8118',
# ]
# # 随机获取代理ip
# proxy_ip = random.choice(proxy_list)
# proxies = {'http': proxy_ip}
# 
# 
# # 获取所有的列表页面链接
# def get_channel_link_list(channel, page, who_sell='o'):
#     # http://bj.ganji.com/ershoubijibendiannao/o3/
#     # o for personal a for merchant
#     url = '{}{}{}/'.format(channel, who_sell, page)
#     wb_data = requests.get(url, headers=headers, proxies=proxies)
#     # 检查页面是否不存在，或者被封ip
#     if wb_data.status_code == 200:
#         soup = BeautifulSoup(wb_data.text, 'lxml')
#         for link in soup.select('.fenlei dt a'):
#             item_link = link.get('href')
#             link_list.insert_one({'url': item_link})
#             get_product_info(item_link)
#             print(item_link)
# 
# 
# # 获取指定链接页面详细信息
# def get_product_info(url, data=None):
#     wb_data = requests.get(url, headers=headers)
#     # 检查页面是否不存在，或者被封ip
#     if wb_data.status_code != 200:
#         return
# 
#     soup = BeautifulSoup(wb_data.text, 'lxml')
# 
#     prices = soup.select('.f22.fc-orange.f-type')
#     pub_dates = soup.select('.pr-5')
#     areas = soup.select('ul.det-infor > li:nth-of-type(3) > a')
#     cates = soup.select('ul.det-infor > li:nth-of-type(1) > span')
# 
#     data = {
#         'title': soup.title.text.strip(),
#         'price': prices[0].text.strip() if len(prices) > 0 else 0,
#         'pub_date': pub_dates[0].text.strip().split(' ')[0] if len(pub_dates) > 0 else "",
#         'area': [area.text.strip() for area in areas if area.text.strip() != "-"],
#         'cates': [cate.text.strip() for cate in cates],
#         'url': url
#     }
#     print(data)
#     product_info.insert_one(data)
