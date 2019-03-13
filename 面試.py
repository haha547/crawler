import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time

emaillist=["howard19970613@gmail.com","benny123tw@gmail.com"]

def main(email):
    url = "http://www.ss.pku.edu.cn/index.php/admission/admnotice"
    r= requests.get(url)
    soup= BeautifulSoup(r.text,"lxml")
    a_tag= soup.find(id= "info-list-ul").a.get('href')
    print(a_tag)
    test= "/index.php/admission/admnotice/3774-软件与微电子学院2019年硕士研究生招生复试分数线"
    if test != a_tag:
        gmail_user = 'hsutestpython@gmail.com'
        gmail_password = 'b2626234' 

        msg = MIMEText('北大軟微招生有新通知。     suppor by Howard_Hsu')
        msg['Subject'] = '北大通知小幫手'
        msg['From'] = gmail_user
        msg['To'] = email

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.send_message(msg)
        server.quit()

        print('Email sent!')
    else:
        time.sleep(3600)
        main()

for i in emaillist:
    main(i)