import requests
from bs4 import BeautifulSoup
import re
url = "http://www.thss.tsinghua.edu.cn/publish/soft/3655/index.html"
resp = requests.get(url)
soup = BeautifulSoup(resp.text,"lxml")
for i in soup.find_all(id = "s2_right_con"):
    print(i,"\n")