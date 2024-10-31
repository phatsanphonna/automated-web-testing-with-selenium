from selenium import webdriver

WEBDRIVER_PATH = 'msedgedriver.exe'
service = webdriver.EdgeService(WEBDRIVER_PATH)
browser = webdriver.Edge(service=service)