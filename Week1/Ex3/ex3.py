# need: title/ address/ daily price/ first pic src/ landload pic src (check)
# / land load gender/ land load name (check)
# if else on land load gender
# level 2: same info but 300 of them

from bs4 import BeautifulSoup
import requests


def get_link(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select("#page_list > ul > li > a")
    for link in links:
        href = link.get("href")  # !! notice
        get_data(href)


def get_gender(class_name):
    if class_name == ['member_boy_ico']:
        return 'M'
    elif class_name == ['member_girl_ico']:
        return 'F'


def get_data(href):
    url = href

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    titles = soup.select(' div.pho_info > h4 > em')

    addresss = soup.select('span.pr5')

    prices = soup.select("#pricePart > div.day_l > span")  # this works

    load_names = soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a")

    profiles = soup.select("#floatRightBox > div.js_box.clearfix > div.member_pic > a > img")

    imgs = soup.select("#curBigImage")  # notice the div inside the div

    genders = soup.select("#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > span")

    for title, address, price, name, profile, img, gender in zip(titles, addresss, prices, load_names, profiles, imgs,
                                                                 genders):
        title_content = title.get_text(),
        address_content = address.get_text(),
        profile_content = profile.get("src"),
        price_content = price.get_text(),
        image_content = img.get("src"),
        name_content = name.get_text(),
        gender_content = get_gender(gender.get("class"))
        data = {
            "title": title_content,
            "address": address_content,
            "price": profile_content,
            "image": price_content,
            "profile": profile_content,
            "name": name_content,
            "gender": gender_content,
        }
        print(data)


urls = ["http://bj.xiaozhu.com/search-duanzufang-p{}-0/".format(str(i)) for i in range(1, 10)]
for url in urls:
    print(url)
    get_link(url)
