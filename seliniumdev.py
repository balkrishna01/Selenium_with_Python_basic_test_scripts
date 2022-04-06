from selenium import webdriver


driver = webdriver.Firefox()

driver.get("http://selenium.dev")

driver.quit()