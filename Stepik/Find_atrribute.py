from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
finally:
    time.sleep(5)
    browser.quit()