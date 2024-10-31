from browser import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_popup(text: str) -> bool:
    popup = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "go3958317564"))
    )

    return text.lower() in popup.text.lower()


def send_submission():
    upload_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mui-hluzqh"))
    )
    upload_button.click()

    assert check_popup("Code submitted successfully.")


def playbook06():
    send_submission()
