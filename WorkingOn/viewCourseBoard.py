
url = "http://ecampus.nqu.edu.tw/eCampus3P/Learn/stu_materials_default.aspx?CurrCourseId=7f1d3fc5-c879-4032-952b-788465c84e1f&CurrRole=Student&CurrAccId=806bd183-9932-4e4c-bfdf-1c80157c9052"


data = {"CurrCourseId" : "7f1d3fc5-c879-4032-952b-788465c84e1f",
"CurrRole" : "Student",
"CurrAccId" : "806bd183-9932-4e4c-bfdf-1c80157c9052"}


p = requests.get(url, params=data)
soup = BeautifulSoup(p.text, "lxml")
print(soup.prettify())import requests
from bs4 import BeautifulSoup
import re