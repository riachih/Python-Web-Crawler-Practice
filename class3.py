import requests
from bs4 import BeautifulSoup
import time

url_saves = 'http://www.tripadvisor.com/Saves#37685322'
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['https://cn.tripadvisor.com/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]

headers = {
    'User-Agent':'',
    'Cookie':''
}

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    time.sleep(4)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles    = soup.select('div.property_title > a[target="_blank"]')
    imgs      = soup.select('img[width="160"]')
    cates     = soup.select('div.p13n_reasoning_v2')
    if data == None:
        for title,img,cate in zip(titles,imgs,cates):
            data = {
                'title'  :title.get_text(),
                'img'    :img.get('src'),
                'cate'   :list(cate.stripped_strings),
                }
        print(data)

def get_favs(url, data=None):
    wb_data = requests.get(url, headers=headers)
    print(wb_data)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select("div.title.titleLLR > div")
    imgs = soup.find_all("div", "missing lazyMiss")
    metas = soup.select('div.attraction_types > span')

    if data == None:
        for title, img, meta in zip(titles, imgs, metas):
            data = {
                'title': title.get_text().strip(),
                'img': img.get('data-thumburl'),
                'meta': meta.get_text()
            }
            print(data)

for single_url in urls:
    get_attractions(single_url)

# '''
# #cheat:
#
# url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text,'lxml')
#
# #titles = soup.select("#taplc_attraction_coverpage_0 > div > div > div > div.shelf_item_container > div > div > div > div.item.name > a")
# titles = soup.select('div.property_title > a[target="_blank"]') #'_blank' to exclude some other titles
# #imgs = soup.select('img["width=160"]') #a way to collect imgs
# imgs = soup.select() #using the img src to search in the page source code, find it-> however, the id might change every day(this could be also used to make sure some labels are exclusive)
# tags = soup.select('#FILTERED_LIST > div > div.element_wrap > div > div.p13n_reasoning_v2') #stop a level before
# print(tags)
#
# #pretend i log in: web page-> inspect -> network -> header -> cookie
#
# '''

# headers ={
#     'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36',
#     'Cookie' : 'TAUnique=%1%enc%3Air1hYv8XXx5H54FbIOkUsII7Hp2eL%2BlTeEQsOpR%2ByykBS27FZ6YVQQ%3D%3D; fbm_162729813767876=base_domain=.tripadvisor.com; ServerPool=X; TASSK=enc%3AAHObL2yKgcPnM9UuSBe5rrMbcTE3hbM9NBIHtV%2FCNah1lwqV24vNISkiwowSY3ljNV%2Fixi3HTytGJn5FRmFZN7ZU5q5X5e0k2GNTN%2F0shMDa3JGu1R1oK4MlttRsug4biA%3D%3D; PMC=V2*MS.21*MD.20170222*LD.20170222; PAC=AOv7rMsLAelPsPDXSki3eSdaBb2o2QsGnzMD_L02OzMLQJO4nx5hG4zehK5pDsonKysvsdpKETiHNfKHgU5rDzWJnPqwsYlLnH6KRlWFkWOJKPTgvxM35qHtib5D5bzEmIQUj-uff6AtSLR0bAEjPtI-5nsaS7DcRHZYy3qIb9JeX2VPlDZcnN0nMdpnq5E9tOq4RIMhJ9K1ydejaxajOaw%3D; TART=%1%enc%3AR%2BeBWyDpFLBP8tLTqQUy%2FoP1kkDycPbcqERQwgykR6%2FDqBmXc%2BptvfwdZpg1OxQgmEKXuc1TgSo%3D; SFPr=%1%xid6qaob0FAbK73W5tgnWw9x5zOd4WDXAkE7XRDOlwcUDjuO6YqSR6M7KAy0DCxDDCVYCOcwmcGuQvo3UY7okFCxnyuJDv4NmmgfSKNhqUuKE805WQFAXnqG1CayKbscPTU7E5LbwkTz21kPva18hwT5k6VE6rISWKlkhIkKwLuR%2FT%2BQzNpFgvXYbw4IGT0nQj7%2BAlsLW4tQ0rnEzGdx2RjIZv0Ak16J%2B8pHAfm9ZK%2Ff%2B%2FNYQu%2F6SAC%2FYuLjjlfEB%2Fno1k9xYPz3Lux17%2Fy5KTxZDZ0VHpPkyrn6AkDL1Oc%3D; TAAuth3=3%3A394a1af64515b0f21cdb7aa0a1ce65c5%3AAPL6B66nlstuDfrUvUQvVyww0AMS8xSpV4tfqiES75sXmWYPI8lUBq2AseFHKGUS%2F0kMxkwVb9UUUt5VSfjht1x3Xu0zNtJ6jFsR%2FvzPm%2Bw85BoLZbxCldR2VZLufLCgNMpW4NhGmOqf4ofq7JhG5fsNJ65Cw0klJAIExi1ieWHyuehb4yGtV9Us1Rm0gq9XRfp5UCGEqx04Z89xxsVIkppyRjA8yvt9OsLD9c7uQk0t; interstitialCounter=2; CommercePopunder=SuppressAll*1487745636976; TATravelInfo=V2*AC.LAX*A.2*MG.-1*HP.2*FL.3*RVL.147966_41l32655_41l60763_53l105127_53l107056_53l547175_53*RS.1; CM=%1%HanaPersist%2C%2C-1%7Cpu_vr2%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7Cpu_vr1%2C%2C-1%7CFtrPers%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Ccatchsess%2C4%2C-1%7Cbrandsess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C6%2C-1%7CHomeAPers%2C%2C-1%7C+r_lf_1%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7C+r_lf_2%2C%2C-1%7Ccatchpers%2C3%2C1488349910%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Cvr_npu2%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C104-771-null%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7Cvr_npu1%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cbrandpers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CWarPopunder_Session%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CWarPopunder_Persist%2C%2C-1%7CTakeOver%2C%2C-1%7Cr_ta_2%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7Cr_ta_1%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cbookstickpers%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g32655-d547175-Reviews-The_Grove-Los_Angeles_California.html; roybatty=TNI1625!AIXm0WZEowob6SMVr10FqFA%2FWFq8jsAkAnkQPYhi%2FQ0p%2BDnIh5GKcb5cGGPsazj9zNJD%2Bkx%2B8lFMYcS4BKYWcGYjRNMVg6mG3Y1y8a39C8IZwRfvO9jV%2FkqCcpe4u3K7vDX6M0YA1jO2qpsEQd0%2F69yZGW6U65fyZYLHaajiSgEX%2C1; fbsr_162729813767876=Zogg1ZYfdahvnuwZl-XiTOpl8-lgvEt1xjDYOFWuP5Y.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUJKY0Rwb0FVenJZVG1IY2ZVcDVmMmdMa1JsaWpqOGxNTzhPa2QxUGpCcmkzbzhmTXpFRTZzQTZvWnc0MWdPaXY1QnY1R3NkbnFMNC1UejVhNHFrNGFwV09sTlRSZ0tKRWlpVzlpUGZMRXRUaXVyTExvMmNUN1BnNGk4bVpZa2pWZHg0VVlQZndUYWszYkVpNnlMSF9Db2dUdUV0eFNpbU05SW5OUE9qYms5YjVVbjhHeGtOekMzT3U5SzFQN0RES3NVa19CV0wxNVNucjdkVTViYlBFVW5wdmJybFlNMzRhMFh0NFF0NDRpaXRXcUtZM2VhTVN2MnFmLXViQVVxU1ZDZFphby0tSU1qdnlVQ1Vvb3ViRXdtTlVrc0JaZEo4ei1zeERORHUyUjhkX2NVUUFxU1FlUFdZdnVaZXpGTGxWclVwUVV3NVZpMnVNUE5YLXByTlc2b0NId3ZOV1dSeTBYMklxdGNJVG5fNENzOGZBdmdlamVhc2ZFaWlXTEtoalEiLCJpc3N1ZWRfYXQiOjE0ODc3NDU4NTcsInVzZXJfaWQiOiIzMDg4NjAzMjkyNjI4MzUifQ; TASession=V2ID.D8B585F7926AD2B0F01F0A10F71C3707*SQ.39*LS.MetaPlacementAjax*GR.83*TCPAR.51*TBR.22*EXEX.49*ABTR.41*PPRP.81*PHTB.90*FS.68*CPU.53*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.42E89C1F3E283B09773C9BF7E1C84292*LF.zhCN*FA.1*DF.0*FBH.2*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.547175*FBC.1; TAUD=LA-1487743254531-1*LG-2606184-2.1.F.*LD-2606185-.....'
# }
#
#
#
# url_saves = 'http://www.tripadvisor.com/Saves#37685322'
# wb_data = requests.get(url_saves,headers=headers)
# soup = BeautifulSoup(wb_data.text,'lxml')
#
# titles = soup.select("div.title.titleLLR > div")
# imgs = soup.find_all("div", "missing lazyMiss")
# metas = soup.select('div.attraction_types > span')
#
# for title,img,meta in zip(titles,imgs,metas):
#     data = {
#         'title'  :title.get_text().strip(),
#         'img'    :img.get('data-thumburl'),
#         'meta'   :meta.get_text()
#     }
#     print(data)


