# 下载一个网页
import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.bilibili.com/'
#
# # 模拟浏览器发送http请求
#
reponse = requests.get(url)
reponse.encoding ='utf-8'
dl = ''
html = reponse.text
scoup = BeautifulSoup(html,'lxml')
dl = scoup.find_all('a')
title = []
for t in dl:
    title.append(t.string)
str1 = ','.join(str(i) for i in title)
str2 = str1.replace('None,' ,'')
str3 = str2.replace('\n','')
str4 = str3.replace(' ','')
str5 = list(set(str4.split(',')))
for i in str5:
    print(i)
print(str5)
print(html)
dl = re.findall(r'<title>(.*?)</title>', html)[0]
print(dl)
# 获取href
chapter = re.findall(r'href="(.*?)">(.*?)<', dl)
if reponse == 200:
    html = reponse.text
    dl = re.findall(r'<dl class="list">.*?</dl>', html,re.S)[0]
#     # 获取href
    chapter = re.findall(r'href="(.*?)">(.*?)<', dl)
else:
    print('错误编码：' + str(reponse))


