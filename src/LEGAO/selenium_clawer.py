"""
try claw the image which searched by image
request: selenium, webdirver
"""
from selenium import webdriver

driver = webdriver.Chrome()
baseurl = 'https://www.google.com.hk/imghp?hl=zh-CN'
driver.get(baseurl)
driver.find_element_by_id('KW').send_keys('anime')
driver.find_element_by_id('su').click()


# hidden_submenu = driver.find_element_by_css_selector(".nav #submenu1")

# actions = ActionChains(driver)
# actions.move_to_element(menu)
# actions.click(hidden_submenu)
# actions.perform()