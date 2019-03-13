import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}

f = open('test.html', 'w+')
s= requests.session()
login_DataFrom = {
    'uid' : '110411506',
    'pwd' : 'b2626234',}
s.post("http://select3.nqu.edu.tw/kmkuas/perchk.jsp", headers=headers, data=login_DataFrom)

login_DataFrom1= {
    "arg01": "107",
    "arg02": "2",
    "arg03": "110411506",
    "arg04": "",
    "arg05": "",
    "arg06": "",
    "fncid": "AG203",
}

s.post("http://select2.nqu.edu.tw/kmkuas/ag_pro/ag203.jsp?", headers=headers, data=login_DataFrom1)

login_DataFrom2={"yms_yms": "107#2",
"dgr_id": "%",
"unt_id": "%",
"ls_clslong": "%",
"cls_id": "%",
"sub_name:" "",
"teacher": "",
"week": "%",
"period": "%",
"pgm_id": "%",
"yms_year": "107",
"yms_sms": "2",
"reading": "reading",}

r= s.post("http://select3.nqu.edu.tw/kmkuas/ag_pro/ag203.jsp?", headers=headers,data=login_DataFrom2)
soup= BeautifulSoup(r.text, "lxml")
print(soup.prettify())
f = open('test.html', 'w+')
f.write(soup.prettify())