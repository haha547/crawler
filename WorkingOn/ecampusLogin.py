import requests
from bs4 import BeautifulSoup
import re
login_URLs = "http://ecampus.nqu.edu.tw/eCampus3P/Learn/LoginPage2/product_login.aspx"
courses_URLs=[]#每個人的課程url

login_DataFrom = {'__EVENTTARGET': '',
    '__EVENTARGUMENT': '', 
    '__VIEWSTATE': ' /wEPDwUKMjAzODk5NzA3Mg8WAh4EX2N0bAUMYnRuTG9naW5IZWxwFgICAw9kFiYCAQ8WAh4KYmFja2dyb3VuZAUWaW1hZ2VzL3poLVRXL2xvZ2luLmdpZhYMAgEPFgIeBXN0eWxlBRpwb3NpdGlvbjpyZWxhdGl2ZTtsZWZ0OjBweBYCAgEPDxYCHghJbWFnZVVybAUTaW1hZ2VzL3poLVRXL2lkLmdpZmRkAgMPFgIfAgUacG9zaXRpb246cmVsYXRpdmU7bGVmdDowcHhkAgUPFgIfAgUacG9zaXRpb246cmVsYXRpdmU7bGVmdDowcHgWAmYPZBYCAgEPDxYCHwMFGWltYWdlcy96aC1UVy9wYXNzd29yZC5naWZkZAIHDxYCHwIFGnBvc2l0aW9uOnJlbGF0aXZlO2xlZnQ6MHB4ZAIJD2QWCAIBDw8WBh4IQ3NzQ2xhc3MFC21lbnVfdGV4dDAyHgRUZXh0BQ5b5b+Y6KiY5a+G56K8XR4EXyFTQgICZGQCAw8PFgYfBAUQbWVudV90ZXh0MDJfb190dx8FBQ5b55m75YWl6Kqq5piOXR8GAgJkZAIFDw8WBh8EBQttZW51X3RleHQwMh8FBQ5b6Kiq5a6i5Y+D6KeAXR8GAgJkZAIHDw8WCB8EBQttZW51X3RleHQwMh8FBQ5b5Y+D6KeA6Kqy56iLXR8GAgIeB1Zpc2libGVoZGQCCw8PFgIfAwUcaW1hZ2VzL3poLVRXL2xvZ2luIEVudGVyLmpwZxYEHgtvbm1vdXNlb3ZlcgU4amF2YXNjcmlwdDp0aGlzLnNyYz0naW1hZ2VzL3poLVRXL2xvZ2luIEVudGVyX292ZHcuanBnJzseCm9ubW91c2VvdXQFM2phdmFzY3JpcHQ6dGhpcy5zcmM9J2ltYWdlcy96aC1UVy9sb2dpbiBFbnRlci5qcGcnO2QCAw8PFgIfAwUTaW1hZ2VzL3poLVRXL0dCLmdpZmRkAgQPDxYCHwMFE2ltYWdlcy96aC1UVy9Fbi5naWZkZAIGDw8WAh8DBRZpbWFnZXMvemgtVFcvdGl0ZWwuanBnZGQCCA8PFgYfBAULbWVudV90ZXh0MDIfBQUOW+ebuOmXnOmAo+e1kF0fBgICZGQCCg8PFgYfBAULbWVudV90ZXh0MDIfBQUOW+W5s+WPsOS7i+e0uV0fBgICZGQCDA8PFgYfBAULbWVudV90ZXh0MDIfBQUOW+W4uOimi+WVj+mhjF0fBgICZGQCDg8PFgYfBAULbWVudV90ZXh0MDIfBQUOW+mAo+e1oeaIkeWAkV0fBgICZGQCEA8PFggfBAULbWVudV90ZXh0MDIfBQUOW+eUs+iri+W4s+iZn10fBgICHwdoZGQCFA8PFgIfAwUdaW1hZ2VzL3poLVRXL21haW4gcGljdHVyZS5qcGdkZAIWDxYCHwEFH2ltYWdlcy96aC1UVy9sb2dpbiB0ZXh0IHBhbi5qcGdkAhgPDxYCHwMFFWltYWdlcy96aC1UVy9uZXdzLmpwZ2RkAhwPDxYCHwMFGmltYWdlcy96aC1UVy9mcmFtZV90b3AuZ2lmZGQCHg8WAh8BBR9pbWFnZXMvemgtVFcvbG9naW4gdGV4dCBwYW4uanBnZAIgDxYEHgZoZWlnaHQFBTI0MHB4HgNzcmMFFy4uL2xvZ2luX0hlbHBJbmRleC5hc3B4ZAIiDxYCHwEFGGltYWdlcy96aC1UVy9mcmFtZV9SLmdpZmQCJA8PFgIfAwUaaW1hZ2VzL3poLVRXL2ZyYW1lX2Rvdy5naWZkZAIoDxYEHwUFHGVDYW1wdXMgSUlJIHYxLjYuMDkxOTguMDEwNDAfB2dkAi4PDxYCHwMFH2ltYWdlcy96aC1UVy9sb2dvIG9mIDNwcm9iZS5naWZkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAwUIYnRuTG9naW4FCmJ0bkNoaW5lc2UFCmJ0bkVuZ2xpc2hqzHG9hdaHqyty7OyKa8boh3mpUA==',
    '__VIEWSTATEGENERATOR': '8B4B7C2A',
    'txtLoginId': '110411506',
    'txtLoginPwd': 'b2626234',
    'btnLogin.x' : '42',
    'btnLogin.y' : '25',}

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
s= requests.session()
p = s.post(login_URLs, headers=headers, data=login_DataFrom)

soup = BeautifulSoup(p.text, "lxml")
f = open('./WorkingOn/course.txt', 'w')
for i in soup.find_all("input",{'url': re.compile('stu_course_default.aspx?')}):
    f.write("http://ecampus.nqu.edu.tw/eCampus3P/Learn/"+i["url"])
    f.write("\n")#寫入課程url

