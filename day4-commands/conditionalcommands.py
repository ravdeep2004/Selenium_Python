from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()


# is_displayed()   is_enabled()

searchbox = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")

print("Display status:", searchbox.is_displayed())   # True
print("Enabled status:", searchbox.is_enabled())     # True


# is_selected() -> for radio buttons and checkboxes

rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")


print("Default radio buttons status.....")
print(rd_male.is_selected())      # False
print(rd_female.is_selected())    # False


rd_male.click()      # select male radio button

print("After selecting male radio button.....")
print(rd_male.is_selected())      # True
print(rd_female.is_selected())    # False


rd_female.click()

print("After selecting female radio button.....")
print(rd_male.is_selected())      # False
print(rd_female.is_selected())    # True


driver.quit()