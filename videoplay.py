
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
driver.get('https://youtube.com')
time.sleep(10)
driver.find_element_by_xpath("//*[@id='button']").click()

driver.quit()