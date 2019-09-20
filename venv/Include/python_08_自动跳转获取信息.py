from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


url = 'https://www.bilibili.com/'

driver = webdriver.Chrome()

driver.get(url)

inputValue = driver.find_element_by_class_name('search-keyword')
#
inputValue.send_keys('python')
#
try:
    buttonClick = driver.find_element_by_css_selector('.search-submit')
    buttonClick.click();
except Exception as ex:
    print('点击出错')

driver.switch_to_window(driver.window_handles[1])
aHrefList = []

# btnList = len(driver.find_elements_by_class_name('pagination-btn'))
btnList = [0,1,2,3,4,5,6,7,8]
for item in driver.find_elements_by_class_name('img-anchor'):
    aHrefList.append(item)
# 获取当前页
# for num in btnList:
#         for item in driver.find_elements_by_class_name('img-anchor'):
#             aHrefList.append(item)
#         time.sleep(5)
#         if num < 7:
#             page = int(num + 1)
#             driver.find_elements_by_class_name('pagination-btn')[page].click()
#         else:
#             break

hrefList = []

for i in aHrefList:
    hrefList.append(i.get_attribute('href'))

with open('href', 'w+') as file:
    for idx in hrefList:
        file.write(idx + '\n')
