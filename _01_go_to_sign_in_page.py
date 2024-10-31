from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import browser
from time import sleep

browser.get('https://ijudge.it.kmitl.ac.th')


WebDriverWait(browser, 30).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "mui-16csuza"))
).click()

sleep(10)

browser.quit()
