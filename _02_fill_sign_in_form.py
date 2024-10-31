from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from browser import browser
from time import sleep
from os import environ

def check_popup(text: str) -> bool:
    popup = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "go3958317564"))
    )

    return text.lower() in popup.text.lower()


def fill_sign_in_form():
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mui-16csuza"))
    ).click()


    # Find fields
    username_field = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.NAME, "username"))
    )
    password_field = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.NAME, "password"))
    )
    login_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mui-pteoa1"))
    )

    # Fill in the form with wrong credentials
    username_field.send_keys("your_username")
    password_field.send_keys("your_password")
    login_button.click()

    # Check if the popup is shown for in correct
    assert check_popup("Invalid username or password.")

    # Clear the fields
    username_field.send_keys(Keys.CONTROL + "a")
    username_field.send_keys(Keys.DELETE)

    password_field.send_keys(Keys.CONTROL + "a")
    password_field.send_keys(Keys.DELETE)

    # Fill in the form with correct credentials
    username_field.send_keys(environ["IJUDGE_USERNAME"])
    password_field.send_keys(environ["IJUDGE_PASSWORD"])
    login_button.click()

    # Wait for page to redirect
    sleep(1)

    # Check if page is redirected to home page
    assert "https://ijudge.it.kmitl.ac.th/" == browser.current_url


def playbook02():
    fill_sign_in_form()


if __name__ == '__main__':
    playbook02()
