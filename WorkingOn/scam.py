import requests
import re
from bs4 import BeautifulSoup

url = 'https://rent.591.com.tw/?kind=&region=1&shType=clinch'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','cookie' : 'webp=1; PHPSESSID=5vnssplt7or8u1nh1pt4v707b5; T591_TOKEN=5vnssplt7or8u1nh1pt4v707b5; _ga=GA1.3.1355740309.1540142859; _ga=GA1.4.1355740309.1540142859; new_rent_list_kind_test=0; is_new_index=1; is_new_index_redirect=1; index_keyword_search_analysis=%7B%22role%22%3A%220%22%2C%22type%22%3A%221%22%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82; c10f3143a018a0513ebe1e8d27b5391c=1; _gid=GA1.3.397449087.1540791689; _gid=GA1.4.397449087.1540791689; 591_new_session=eyJpdiI6InZ2ditrUGpmejdxUXJkNElWWTRCK1E9PSIsInZhbHVlIjoibFpvQ1ZcL0tDNHRtNk1zRkRuUFJUa3JlbVkxNXVJN29MWktNZ2d3b053NndkRFY5WXNCUmhnRmZSZEJBcW5WcEJZM3BRNFZUV2NUQTBxTjVFMXdVK2JnPT0iLCJtYWMiOiIyMjIyOGU4YzI4MjBiYzIxZTU0ZjU2OTgyZDdkZGI3NWZjZjgwNGY1NjAzYWQ0NThmZGUwNTUzNmNlYzg2NGI1In0%3D'}

#因為他們會用基本的擋爬蟲 所以需要user-agent cookies 是因為他們的查詢是使用cookies記錄使用者的訊息
#不知道為什麼browser 的 resource code 跟抓出來的不一樣所以做sibling有點奇怪ＧＧ
#這很慢因為他是每一筆都送一個requests.get但是他可以之後用find()抓到裡面的詳細資訊 解決上面說的sibling問題

for i in range (0,51): 
    time =str(i)
    resp = requests.get(url, headers = headers , params={
        'is_new_list': '1',
        'type': '', 
        'kind': '',
        'searchtype': '1',
        'region': '1',
        'shType': 'clinch',
        'firstRow' : time,
    })
    soup = BeautifulSoup(resp.text,"lxml")
    data = soup.find(id="content")  #找每一個的html

    type1 = data.find(class_ = "lightBox").find(text=re.compile("獨立套房"))
    type2 = data.find(class_ = "lightBox").find(text=re.compile("整層住家"))
    type3 = data.find(class_ = "lightBox").find(text=re.compile("辦公"))
    type4 = data.find(class_ = "lightBox").find(text=re.compile("分租套房"))
    type5 = data.find(class_ = "lightBox").find(text=re.compile("雅房"))
    type6 = data.find(class_ = "lightBox").find(text=re.compile("車位"))

    #用很笨的方法因為我還是不太了解 python QQ
    #再加上我沒時間拉就湊合著用

    localO = data.find(text=re.compile("區"))   #output local
    sizeO = data.find(class_ = "lightBox").find(text=re.compile("坪"))  #output size
    priceO = data.find(class_ = "price")   #output price

    if type1 != None:
        print(type1)
    elif type2 != None:
        print(type2)
    elif type3 != None:
        print(type3)  
    elif type4 != None:
        print(type4)
    elif type5 != None:
        print(type5)
    else:
        print(type6)  
    
    print(localO)
    print(sizeO)
    print(priceO.i.string)
    print("------------------------")