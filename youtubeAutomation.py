
from multiprocessing.connection import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get('https://youtube.com')
wait = WebDriverWait(driver, 20)
searchbox = wait.until(
        EC.visibility_of_element_located((By.XPATH,"//input[@id='search']")))
#searchbox.click()
searchbox.send_keys("Best music")
searchButton=wait.until(
        EC.element_to_be_clickable((By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button/yt-icon")))
searchButton.click()
