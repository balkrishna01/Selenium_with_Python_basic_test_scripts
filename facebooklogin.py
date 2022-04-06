from lib2to3.pgen2 import driver
from selenium import webdriver
driver=webdriver.Chrome()

driver.get("https://www.facebook.com/")

#driver.implicitly_wait(20)
driver.maximize_window()
driver.find_element_by_name("email").send_keys("ABC@gmail.com")
driver.find_element_by_name("pass").send_keys("password12345")
driver.find_element_by_name("login").click()
#print(uname.is_enabled())
#print(uname.is_selected())
