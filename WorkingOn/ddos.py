import requests
from bs4 import BeautifulSoup
url = 'https://benny123tw.github.io/bh-blog/'
for i in range(0,100):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,"lxml")
    print(i)
    soup.clear