from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID,"book").click()
    x_element = browser.find_element(By.ID, "input_value")
    browser.execute_script("arguments[0].scrollIntoView();", x_element)
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(5)
    browser.quit()