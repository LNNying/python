import requests
import re
from bs4 import BeautifulSoup



url = "https://www.bilibili.com/"

reponse = requests.get(url)

html = reponse.text

reponse.encoding = 'utf-8'

soup = BeautifulSoup(html, 'lxml')

dl = soup.find_all('a')

href = []
hrefs = []
body = []

# 循环得到url
for i in dl:
    try:
        if i.attrs['href']:
            href.append(i.attrs['href'])
        else:
            href.append('')
    except Exception as ex:
        print('')
# 数组字符串化
strList = ','.join(str(i) for i in href)
# 去除空格
href1 = strList.replace(' ','')
# 去除 //
href2 = href1.replace('//','')
# 字符串数组化
realHref = list(set(href2.split(',')))

httpBody = [] # 包含https
otherBody = [] # 不包含https
# 分别得到包含https 和 不包含https
for idx in realHref:
    http = re.findall('https', idx)
    try:
        if http[0] == 'https':
            httpBody.append(idx)
    except Exception as ex:
        otherBody.append(idx)

# 对于不同情况拼接url
for inf in otherBody:
    urls = inf
    li = re.findall(r'www|/v', inf)
    try:
        if li[0] == 'www':
            body.append('https://' + str(urls))
        elif li[0] == '/v':
            body.append('https://www.bilibili.com' + str(urls))
        else:
            body.append('https://www.bilibili.com/' + str(urls))
    except Exception as ex:
        body.append('https://www.bilibili.com/' + str(urls))

# # 写到文件中
with open('url', 'a+') as file:
    for ind in body:
        if ind != '':
            file.write(ind + '\n')
    for indx in httpBody:
        file.write(indx + '\n')