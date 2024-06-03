from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000))).button.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", robots_rule_radio)
    robots_rule_radio.click()
    # browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    time.sleep(10)
    browser.quit()
