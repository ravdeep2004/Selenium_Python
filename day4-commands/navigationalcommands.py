from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.snapdeal.com")
driver.get("http://www.amazon.com")

driver.back()      # snapdeal
driver.forward()   # amazon

driver.refresh()

driver.quit()