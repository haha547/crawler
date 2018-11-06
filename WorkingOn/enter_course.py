import requests
from bs4 import BeautifulSoup
import re







"""URL_COOKIES = s.cookies.get_dict()
print(URL_COOKIES)

for i in courses_URLs:
    r= s.get(i, cookies=URL_COOKIES, headers=headers)
    headers_jump = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',"Referer":i}
    s.get("http://ecampus.nqu.edu.tw/eCampus3P/Learn/enter_course_index.aspx", headers=headers_jump, cookies=URL_COOKIES)
    q= s.get(i, cookies=URL_COOKIES, headers=headers)
    print(r.text)
    print(q.text)"""