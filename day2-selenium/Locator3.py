from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()

#tag & id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")


# tag and class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")


# tag & attribute
#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc@gmail.com")


# tag , class & attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("xyz")

#THE ABOVE CODE IS OLD AND NOT WORKING AS FACEBOOK HAS CHANGED THE HTML OF THE LOGIN PAGE NOW. NOW TAGS & ATTRIBUTE COMBINATION WOORKS THE MOST STABLE
#BELOW IS THE CODE WITH UPDATED LOCATORS BUT THEN ALSO TAG&ID AND TAG&CLASS REMAIN UNSTABLE AS IDS/CLASSES MAY NOT BE UNIQUE
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/login/")
driver.maximize_window()


# TAG & CLASS
driver.find_element(
    By.CSS_SELECTOR,
    "input.inputtext"
).send_keys("abc@gmail.com")


# TAG & ATTRIBUTE
driver.find_element(
    By.CSS_SELECTOR,
    "input[name='pass']"
).send_keys("123")


# TAG & CLASS & ATTRIBUTE
driver.find_element(
    By.CSS_SELECTOR,
    "input.inputtext[name='pass']"
).clear()

driver.find_element(
    By.CSS_SELECTOR,
    "input.inputtext[name='pass']"
).send_keys("xyz")


input("Enter...")
driver.quit()

"""

"""
# Identify element
# action


# <input id='sddsd' name='sadasd'> Name: </input>

# <a href="link"> register </a>

# register is a linktext


# id
# name
# linktext
# partiallinktext

# classname
# tagname


# CSS Selectors
# ----------------

# 1) tag id
# syntax:
# tagname#valueOfId
# example:
# input#email


# 2) tag class
# syntax:
# tagname.valueOfClass
# example:
# input.inputtext._55r1._6luy


# 3) tag attribute
# syntax:
# tagname[attribute=value]
# example:
# input[data-testid=royal_email]


# 4) tag class attribute
# syntax:
# tagname.valueOfClass[attribute=value]
# example:
# input.inputtext[data-testid=royal_pass]

"""