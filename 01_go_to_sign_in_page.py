from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import browser

browser.get('https://ijudge.it.kmitl.ac.th')

try:
    elem = WebDriverWait(browser, 30).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "mui-16csuza"))
    ).click()

    print(elem)
finally:
    browser.quit()