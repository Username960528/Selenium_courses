import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    elements = browser.find_element(By.CLASS_NAME, "form-group")
    browser.find_element(By.NAME, "firstname").send_keys("Yuriy")
    browser.find_element(By.NAME, "lastname").send_keys("Mikityuk")
    browser.find_element(By.NAME, "email").send_keys("blabla@gmail.com")
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
finally:
    time.sleep(10)
    browser.quit()
