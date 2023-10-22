from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service_obj = Service("C:/Users/aasis/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test")
driver.maximize_window()
time.sleep(20)
