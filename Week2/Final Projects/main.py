#!/usr/bin/env python
#-*- coding: utf-8 -*-

from multiprocessing import Pool
from channel_link_list import get_channel_link_list, get_product_info, link_list, product_info
from channel import channel_list

# db_urls = [item['url'] for item in link_list.find()]
# index_urls = [item['url'] for item in product_info.find()]
# x = set(db_urls)
# y = set(index_urls)
# rest_of_urls = x-y
print(channel_list.split())

def get_all_links_from(channel):
    for i in range(1,100):
        get_channel_link_list(channel, i)


if __name__ == '__main__':
    pool = Pool(processes=6)
    pool.map(get_product_info,set(channel_list.split())) # 抓取商品详情页
    pool.close()
    pool.join()
