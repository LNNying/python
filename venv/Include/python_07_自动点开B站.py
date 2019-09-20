from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


# 自动打开B站视频
driver = webdriver.Chrome()

driver.get('https://www.bilibili.com')
# 登录
driver.find_element_by_class_name('i-face').click()
# 重定向
# driver.switch_to_window(driver.window_handles[0])
# 获取登录input和按钮
name = driver.find_element_by_id('login-username')
password = driver.find_element_by_id('login-passwd')
# 设置信息
time.sleep(1)
name.send_keys('15153557020')
time.sleep(1)
password.send_keys('ningning.')
# 登录
login = driver.find_element_by_class_name('btn-login')
login.click()
time.sleep(4)
# 问题获取不到input 原因在于 点击按钮直接执行下一局语句
# 搜索跳转
handle = driver.current_window_handle
driver.switch_to_window(handle)
time.sleep(4)
inputValue = driver.find_element_by_class_name('search-keyword')
inputValue.send_keys('python')
time.sleep(4)
buttonClick = driver.find_element_by_class_name('search-submit')
buttonClick.click()
# try:
#     buttonClick = driver.find_element_by_class_name('search-submit')
#     time.sleep(2)
#     buttonClick.click()
# except Exception as ex:
#     print('点击出错')
# 跳转后的页面需要重新定向
driver.switch_to_window(driver.window_handles[1])
aClick = driver.find_elements_by_class_name('img-anchor')[0]
time.sleep(2)
aClick.click()
driver.switch_to_window(driver.window_handles[2])
videoClick = driver.find_elements_by_class_name('bilibili-player-area')[0]
time.sleep(2)
videoClick.click()
#
time.sleep(10)
driver.quit()