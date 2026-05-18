from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# ==========================
# Driver setup
# ==========================

driver = webdriver.Chrome()

driver.get(
    "https://money.rediff.com/gainers/bse/daily/groupa"
)

driver.maximize_window()


# ==========================
# self
# ==========================

text_msg = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/self::a"
).text

print(text_msg)

# Output:
# India Tourism De


# ==========================
# parent
# ==========================

text_msg = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/parent::td"
).text

print(text_msg)

# Output:
# India Tourism De


# ==========================
# child (Approach 1)
# print text
# ==========================

text_msg = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr/child::td"
).text

print(text_msg)


# ==========================
# child (Approach 2)
# count children
# ==========================

childs = driver.find_elements(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr/child::td"
)

print(len(childs))


# ==========================
# ancestor
# ==========================

text_msg = driver.find_element(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr"
).text

print(text_msg)

# Output:
# India Tourism De A 358.35 375.30 +4.73


# ==========================
# descendant
# ==========================

descendants = driver.find_elements(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr/descendant::*"
)

print(
    "Number of descendant nodes:",
    len(descendants)
)

# Output:
# 7


# ==========================
# following
# ==========================

followings = driver.find_elements(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr/following::*"
)

print(
    "Number of following nodes:",
    len(followings)
)

# Output:
# 719


# ==========================
# following-sibling
# ==========================

followingsiblings = driver.find_elements(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr/following-sibling::*"
)

print(
    "Number of following sibling nodes:",
    len(followingsiblings)
)

# Output:
# 72


# ==========================
# preceding
# ==========================

precedings = driver.find_elements(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding::*"
)

print(len(precedings))

# Output:
# 251


# ==========================
# preceding-sibling
# ==========================

precedingsiblings = driver.find_elements(
    By.XPATH,
    "//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding-sibling::tr"
)

print(len(precedingsiblings))


driver.close()