# -*- coding: utf-8 -*-

#get channel url at the bottom of the page
#get 'individual' part link list under different channel
#from the link list, get the info page and obtain following information:
#title, released date, category, price, area, new/old degree

from bs4 import BeautifulSoup
import time
import requests

#first get the channel url
main_page='http://bj.ganji.com/wu/'

def channel_extract():
    main_page = 'http://bj.ganji.com/wu/'
    wb_data = requests.get(main_page)
    soup = BeautifulSoup(wb_data.text,'lxml')
    channels = soup.select('#wrapper > div.content > div > div > dl > dt > a')
    for channel in channels:
        channel_text = channel.get("href")
        channel_url='http://bj.ganji.com'+ channel_text
        print(channel_url)

channel_extract()

channel_list = '''
http://bj.ganji.com/jiaju/
http://bj.ganji.com/rirongbaihuo/
http://bj.ganji.com/shouji/
http://bj.ganji.com/shoujihaoma/
http://bj.ganji.com/bangong/
http://bj.ganji.com/nongyongpin/
http://bj.ganji.com/jiadian/
http://bj.ganji.com/ershoubijibendiannao/
http://bj.ganji.com/ruanjiantushu/
http://bj.ganji.com/yingyouyunfu/
http://bj.ganji.com/diannao/
http://bj.ganji.com/xianzhilipin/
http://bj.ganji.com/fushixiaobaxuemao/
http://bj.ganji.com/meironghuazhuang/
http://bj.ganji.com/shuma/
http://bj.ganji.com/laonianyongpin/
http://bj.ganji.com/xuniwupin/
http://bj.ganji.com/qitawupin/
http://bj.ganji.com/ershoufree/
http://bj.ganji.com/wupinjiaohuan/
'''