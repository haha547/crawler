import requests
from bs4 import BeautifulSoup
import os
import time
url = "https://www.dcard.tw/f/sex?latest=true"
#headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36','cookie' : 'webp=1; PHPSESSID=5vnssplt7or8u1nh1pt4v707b5; T591_TOKEN=5vnssplt7or8u1nh1pt4v707b5; c10f3143a018a0513ebe1e8d27b5391c=1; _ga=GA1.3.1355740309.1540142859; _gid=GA1.3.816343156.1540142859; _ga=GA1.4.1355740309.1540142859; _gid=GA1.4.816343156.1540142859; new_rent_list_kind_test=0; is_new_index=1; is_new_index_redirect=1; index_keyword_search_analysis=%7B%22role%22%3A%220%22%2C%22type%22%3A%221%22%2C%22keyword%22%3A%22%22%2C%22selectKeyword%22%3A%22%22%2C%22menu%22%3A%22%22%2C%22hasHistory%22%3A0%2C%22hasPrompt%22%3A0%2C%22history%22%3A0%7D; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82; 591_new_session=eyJpdiI6ImR2eUIxNldQeG4rRGh1eVlxUmtnTmc9PSIsInZhbHVlIjoib09cL3MwNEFEMTZudExqT3grdzJLTHRPYTlwN2FsMk5tVEs0OCt5MDVSS01VZFFQV2V4VmZWaUFCRG9MQldSWDBLN2FyYjJuUm1wVVc4NGM5MERicCtnPT0iLCJtYWMiOiJmODZkNTc1NmM5ZTZjZjA2NTg3ZDFjYTQ4MWQ1ZTAwNmU2NDNmYzk4N2U3NmUyMDg4ZGMyNjUwOGY5N2ZjM2VlIn0%3D'}
resp = requests.get(url)
soup = BeautifulSoup(resp.text,"lxml")
#final = soup.find( id="content")
print(soup.prettify())
#print(final.find(class_ = "price").i.string)#price
#print(final.find_all(class_ = "lightBox"))#坪數與類型地區
#print(final.prettify())
#clearfix