import requests
import re
from bs4 import BeautifulSoup
import xlwt 

url = 'https://rent.591.com.tw/?kind=&region=1&shType=clinch'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','cookie' : 'webp=1; PHPSESSID=5vnssplt7or8u1nh1pt4v707b5; T591_TOKEN=5vnssplt7or8u1nh1pt4v707b5; _ga=GA1.3.1355740309.1540142859; _ga=GA1.4.1355740309.1540142859; new_rent_list_kind_test=0; is_new_index=1; is_new_index_redirect=1; index_keyword_search_analysis=%7B%22role%22%3A%220%22%2C%22type%22%3A%221%22%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82; c10f3143a018a0513ebe1e8d27b5391c=1; _gid=GA1.3.397449087.1540791689; _gid=GA1.4.397449087.1540791689; 591_new_session=eyJpdiI6InZ2ditrUGpmejdxUXJkNElWWTRCK1E9PSIsInZhbHVlIjoibFpvQ1ZcL0tDNHRtNk1zRkRuUFJUa3JlbVkxNXVJN29MWktNZ2d3b053NndkRFY5WXNCUmhnRmZSZEJBcW5WcEJZM3BRNFZUV2NUQTBxTjVFMXdVK2JnPT0iLCJtYWMiOiIyMjIyOGU4YzI4MjBiYzIxZTU0ZjU2OTgyZDdkZGI3NWZjZjgwNGY1NjAzYWQ0NThmZGUwNTUzNmNlYzg2NGI1In0%3D'}

#因為他們會用基本的擋爬蟲 所以需要user-agent cookies 是因為他們的查詢是使用cookies記錄使用者的訊息
#不知道為什麼browser 的 resource code 跟抓出來的不一樣所以做sibling有點奇怪ＧＧ
#這很慢因為他是每一筆都送一個requests.get但是他可以之後用find()抓到裡面的詳細資訊 解決上面說的sibling問題

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
ws.write(0, 0, "type")
ws.write(0, 1, "Zip code")
ws.write(0, 2, "size")
ws.write(0, 3, "price")


districtDic = {
"中正區" : "Zhongzheng_District" , "大同區" : "Datong_District" , "中山區" : "Zhongshan_District"
,"松山區" : "Songshan_District" , "大安區" : "Da’an_District" , "萬華區" : "Wanhua_District" , "信義區" : "Xinyi_District"
,"士林區" : "Shilin_District" , "北投區" : "Beitou_District" , "內湖區" : "Neihu_District" , "南港區" : "Nangang_District"
,"文山區" : "Wenshan_District"}

for i in range (0,3000): 
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
        ws.write(i+1, 0, "Independent_Suite")
    elif type2 != None:
        ws.write(i+1, 0, "Whole_Floor_Home")
    elif type3 != None:
        ws.write(i+1, 0, "Office")  
    elif type4 != None:
        ws.write(i+1, 0, "Sublet_Suite")
    elif type5 != None:
        ws.write(i+1, 0, "Elegant_Room")
    elif type6 != None:
        ws.write(i+1, 0, "Parking_Space")
    else:
        ws.write(i+1, 0, "Other")
    
    #print(localO)
    ws.write(i+1, 1, districtDic[localO[0:3]])
    #print(sizeO)
    if sizeO == None:  #有些坪數是0很靠北
        ws.write(i+1, 2, 1)
    else:
        ws.write(i+1, 2, sizeO[0 : len(sizeO.strip()) -1 ])
    #print(priceO.i.string)
    ws.write(i+1, 3, priceO.i.string[0:len(priceO.i.string)-4] + priceO.i.string[len(priceO.i.string)-3:])
    print(i)
    wb.save('Workbook1.xls')
    soup.decompose = True
    soup.clear()