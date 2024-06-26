from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "input[name='first_name']")
    first_name.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    # browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
