import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}

f = open('test.html', 'w+')
s= requests.session()
login_DataFrom = {
    'uid' : '110411506',
    'pwd' : 'b2626234',}
s.post("http://select3.nqu.edu.tw/kmkuas/perchk.jsp",headers=headers,data=login_DataFrom)

s.post("http://select3.nqu.edu.tw/kmkuas/fnc.jsp",headers=headers,data="0A001")
login_DataFrom1= {
    "arg01": "107", #學年
    "arg02": "2",   #學期
    "arg03": "110411506",#學號
    "arg04": "",
    "arg05": "",
    "arg06": "",
    "fncid": "0A001",}
#              /\
#             /  \ 
#            /    \
#           /      \
#             | |
#             | |
#            大門登入

s.post("http://select3.nqu.edu.tw/kmkuas/choice/check.jsp?fnckind=A",headers=headers,data=login_DataFrom1)
del login_DataFrom, login_DataFrom1
s.get("http://select3.nqu.edu.tw/kmkuas/choice/0A001.jsp", headers=headers)
login_DataFrom={
    "etxt_gen": "%",
    "etxt_degree": "15",
    "unittmp": "31|0100|學分班#17|UE02|電子學系#17|UE76|食品學系#17|UE85|資工學系#27|UE85|資工學系#17|UE86|土木學系#17|UH57|建築學系#17|UH59|國際學系#27|UH59|國際學系#17|UH60|應英學系#17|UK10|都景學系#17|UL10|邊境學系#17|UM75|企管學系#27|UM75|企管學系#17|UM84|觀光學系#27|UM84|觀光學系#17|UM87|運休學系#27|UM87|運休學系#17|US10|工管學系#17|UU10|護理學系#17|UU20|社工學系#27|UU20|社工學系#17|UU30|長照學系#17|UH61|華語文學系#15|UH10|閩南所#15|UE02|電子學系#15|UE76|食品學系#15|UE86|土木學系#15|UH57|建築學系#15|UH59|國際學系#15|UH60|應英學系#15|UL10|邊境學系#15|UM75|企管學系#15|UM84|觀光學系#15|UM87|運休學系#25|MC01|管理學院事業經營#25|SS01|理工學院工程科技#15|UH11|閩南所學位學程#15|US20|智慧計算應用碩士#15|US21|資訊科技應用碩士#",
    "etxt_norunit": "UH10",#上面很智障的編號
    "etxt_clsyear": "4" ,#年級？
}
r= s.post("http://select3.nqu.edu.tw/kmkuas/choice/0A002.jsp", headers=headers,data=login_DataFrom)
#              /\
#             /  \ 
#            /    \
#           /      \
#             | |
#             | |
#         打開通識選課

soup= BeautifulSoup(r.text,"lxml")
f.write(soup.prettify())
