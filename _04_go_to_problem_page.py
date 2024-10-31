from browser import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_problems_of_course_page():
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mui-1m5f78l"))
    ).click()


def go_to_problem_page():
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Hello Selenium')]"))
    ).click()


def playbook04():
    go_to_problems_of_course_page()
    go_to_problem_page()

