from browser import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def go_to_course_page():
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mui-hluzqh"))
    ).click()

    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "mui-6xu4c"))
    ).click()


def check_description():
    description_box = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "previewmd-preview"))
    )

    description = description_box.find_element(By.TAG_NAME, "p")

    assert "Hi Mom, It works." == description.text



def playbook03():
    go_to_course_page()
    check_description()


if __name__ == "__main__":
    playbook03()
