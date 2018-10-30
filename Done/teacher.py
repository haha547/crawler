
import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


url = ["http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1655-曹喜信",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1666-窦尔翔",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1614-李伟平",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1652-林金龙",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1656-柳翔",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1661-罗正忠",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1669-吴中海",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1639-杨雅辉",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1664-张兴",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1634-沈晴霓",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1716-张华",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1651-赵占波",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1637-文伟平",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1663-严  伟",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1641-郁 莲",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1650-黄嵩",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1613-蒋严冰",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1610-荆琦",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1608-林慧苹",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1648-马振华",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1615-莫同",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1662-时广轶",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1636-孙圣力",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1665-王振宇",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1640-俞敬松",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1642-周立新",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1647-李素科",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1643-朱郑州",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/2512-赵岩",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/2267-刘宏志",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1609-段莉华",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1645-邢恩泉",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1657-曹健",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1612-方跃坚",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1611-褚伟杰",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1659-刘京",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1660-刘珍峰",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1646-宋丹",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1638-夏敏",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1947-张宏岩",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1654-张齐勋",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/3636-倪宣明",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/3636-倪宣明",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/2512-赵岩",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/2267-刘宏志",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1947-张宏岩",
"http://www.ss.pku.edu.cn/index.php/teacherteam/teacherlist/1716-张华",]


#teacher-name
#inline


teacherlist = []



for i in range (0,len(url)):
    resp = requests.get(url[i])
    soup = BeautifulSoup(resp.text , "lxml")
    inline = soup.find('ul',{'class':'inline'})
    nextlayor = inline.find_all('li')

    var1 = soup.title.string
    #f = open('teacher.txt', 'a')
    
    print (var1[0:3])
    print ("****************************************")
    print (nextlayor)
    print ("----------------------------------------")

    #f.write(soup.title.string + '\n' + str(nextlayor)+ '\n'+ '\n')