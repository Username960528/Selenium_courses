from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    browser.find_element(By.ID, "robotsRule").click()

    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    alert = browser.switch_to.alert
finally:
    time.sleep(5)
    browser.quit()


