import requests
from bs4 import BeautifulSoup
url = "http://www.cs.ntou.edu.tw/cswp/index.php?name=people1"

r = requests.get (url)
r.encoding = "utf-8"
soup = BeautifulSoup(r.text,"lxml")
for i in  soup.find("tbody").find_all("tr"):
    print (i.find())