from bs4 import BeautifulSoup

with open('/Users/riachih/Desktop/Plan-for-combating-master/week1/1_2/1_2answer_of_homework/index.html', 'r') as wb_data:
    Soup = BeautifulSoup(wb_data,'lxml')
    #images=Soup.find_all('img')
    #body > div: nth - child(2) > div > div.col - md - 9 > div:nth - child(2) > div: nth - child(1) > div > img
    #body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(8) > div > img
    #body > div: nth - child(2) > div > div.col - md - 9 > div:nth - child(2) > div: nth - child(2) > div > img
    #body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(8) > div > img
    images = Soup.select("body > div > div > div.col-md-9 > div > div > div > img") #把前面所有的n-of-type删除
    prices = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right") #chrome-webpage-inspect-copy-selector
    titles = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a")
    ratingN = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right")
    stars = Soup.select("body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")

for image, price, title ,rating ,star in zip(images,prices,titles,ratingN,stars):
        title_content = title.get_text(),
        rating_content = rating.get_text()
        price_content = price.get_text()
        image_content = image.get("src")
        stars_count = len(star.find_all("span", "glyphicon glyphicon-star"))

        data={
            'title':title_content,
            'rating':rating_content,
            'price':price_content,
            'image':image_content,
            'star':stars_count
        }

        print(data)