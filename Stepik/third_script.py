from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://www.degreesymbol.net/"
link2 = "https://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
    link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
    link.click()


    browser.get(link2)
    link2 = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link2.click()


    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='first_name']")
    first_name.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




finally:
    time.sleep(5)
    browser.quit()
