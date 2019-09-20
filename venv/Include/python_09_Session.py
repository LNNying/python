import requests
import random
import json
import time
import re
from requests.adapters import HTTPAdapter
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
#
# session = requests.session()
# session.mount('https://', HTTPAdapter(max_retries=2))
#
# session.post('https://bilibili.com/cookies/set/setcookies/这是一个cookie')
#
# response = session.post('https://www.bilibili.com/cookies')
#
# print(response.text)
#
# print(session.cookies)
#
# url ='https://api.github.com/events'
# datas = {"data": '数据'}
# r = requests.post(url, data=json.dumps(datas))
#
# print(r.json())
#
# print(r.status_code)
#
# print(r.raise_for_status())
#
# print(r.headers)
#
# print(r.text)

# cookie = requests.utils.dict_from_cookiejar(response.cookies)

# print(response.url.find('Login'))
# print(cookie)
# print(response.text)


# driver = webdriver.Chrome()
# driver.get('https://baidu.com')
# driver.execute_script('alert("这是一个js文件")')
# time.sleep(1)
# alert = driver.switch_to_alert()
# alert.accept()

str = "location.href = '/data_files/ebiz/bill_of_lading/pdf/20190822//QIWB3723555_20190822163412_9925.pdf';"
dome = re.findall(r"/data_files.*?'",str)
print(dome)