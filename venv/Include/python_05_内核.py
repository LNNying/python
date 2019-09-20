from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
import time

# 获取chrome路径
driver = webdriver.Chrome()
# 获取百度首页
driver.get('https://www.baidu.com')
#-------------获取标签---------------
# input_first = driver.find_element_by_id('q')
# input_second = driver.find_element_by_css_selector('#q')
# input_third = driver.find_element_by_xpath('//*[@id="q"]')
# print(input_first.size)
# print(input_second.id)
# print(input_third.tag_name)
# ---------------------------

# ---------获取页面代码-------
# print(driver.page_source)
# -----------------------------

# ----------模拟点击-----------
# 获取输入框元素
# input = driver.find_element_by_id('kw')
# button = driver.find_element_by_id('su')
# input.send_keys('Python')
# button.click()
# ---------------------------

# -------------网页选项卡操作---------
# driver.execute_script('window.open()')
# print(driver.window_handles)
# driver.switch_to_window(driver.window_handles[1])
# driver.get('https://www.taobao.com')
# time.sleep(1)
# driver.switch_to_window(driver.window_handles[0])
# driver.get('https://python.org')
# -------------------------------------------
# time.sleep(5)
# driver.close() # 关闭当前窗口
driver.quit() # 关闭所有窗口