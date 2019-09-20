from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
# driver.get('https://www.bilibili.com/v/game/esports/?spm_id_from=333.334.primary_menu.35#/9222')
driver.get('https://www.bilibili.com')

# try:
#     WebDriverWait(driver, 2).until(EC.presence_of_all_elements_located(By.CLASS_NAME,'vd-list'))
#     for doctoerName in driver.find_element_by_css_selector('.vd-list li'):
#         print(doctoerName.find_element_by_css_selector('.r > a').text)
# finally:
#     driver.close()