from bs4 import BeautifulSoup
import requests,urllib.request
import time


folder_path='/Users/riachih/Desktop/Tyler Swift/'

def get_data(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('#main-container > div.grid.grid-no-margins > div.col.span-content > div > div > div > div > div > a > img')

    for img in imgs:
        src = img.get("src")
        filename = src.split("?")[0].split("/")[-2]+'.jpg'
        urllib.request.urlretrieve(src, folder_path+ filename)
        print(filename)

#def get_pages():

urls = ["http://weheartit.com/inspirations/taylorswift?page={}".format(str(i)) for i in range(1, 11)]
for url in urls:
    time.sleep(2)
    get_data(url)

