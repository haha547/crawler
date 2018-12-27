from bs4 import BeautifulSoup
import requests
import re
teacheris = [
"?ID=5450",
"?ID=1076",
"?ID=5448",
"?ID=1068",
"?ID=1069",
"?ID=5446",
"?ID=1077",
"?ID=5452",
"?ID=5456",
"?ID=1098",
"?ID=5445",
"?ID=1099",
"?ID=1100",
"?ID=5451",
"?ID=5453",
"?ID=5443",
"?ID=5457",
"?ID=5460",
"?ID=5441",
"?ID=334",
"?ID=5458",
"?ID=1102",
"?ID=1103",
"?ID=5440",
"?ID=6305",
"?ID=5461",
"?ID=1104",
"?ID=6425",
"?ID=1105",
"?ID=5462",
"?ID=1106",
"?ID=5459",
"?ID=1108",
"?ID=1107",
"?ID=5454",
"?ID=5444",
"?ID=5447",
"?ID=5449",
"?ID=5455"
]
f = open('teacher.txt', 'a')
for i in teacheris:
    url = "http://eecs.pku.edu.cn/teaching/inservice/search/Detail/"+i
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    print(soup.title.string[0:3])
    f.write(soup.title.string[0:3] )
    for j in soup.findAll("div", {"class": "zzjsnyM2_1Rnr"}):
        print(j.get_text())
        f.write(j.get_text())

