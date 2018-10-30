from bs4 import BeautifulSoup
import requests
import json

url = "http://eecs.pku.edu.cn/teaching/inservice/"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

print(soup)