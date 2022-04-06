
from selenium import webdriver


driver=webdriver.Firefox()
driver.get('https://youtube.com')

driver.find_element_by_id("container").send_keys("Music")
driver.find_element_by_id("search-icon-legacy").click()