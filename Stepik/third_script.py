from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://www.degreesymbol.net/"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.LINK_TEXT, "Degree Symbol in Math")
    link.click()

finally:
    browser.exit()
