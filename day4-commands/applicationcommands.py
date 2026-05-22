from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)          # OrangeHRM
print(driver.current_url)    # https://opensource-demo.orangehrmlive.com/
print(driver.page_source)    # Returns entire HTML source of page (very long output)

driver.quit()


"""
driver.close()   # closes current tab
driver.quit()    # closes whole browser
"""
