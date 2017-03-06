from bs4 import BeautifulSoup
import requests
import time


#get more pages
url = 'https://knewone.com/discover?page='

def get_page(url,data=None):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('a.cover-inner > img')
    titles = soup.select('section.content > h4 > a')
    links = soup.select('section.content > h4 > a')
#load a new section of page and observe
#lok at the new div: check the class
    if data==None:
        for img,title,link in zip(imgs,titles,links):
            data = {
                'img':img.get('src'),
                'title':title.get('title'),
                'link':link.get('href')
            }
            print(data)


#but we dont know how many pages are there

def get_more_pages(start,end):
    for one in range(start,end):
        get_page(url+str(one))
        time.sleep(2)


get_more_pages(1,10)