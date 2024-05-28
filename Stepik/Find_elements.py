from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker

# Создаем экземпляр Faker для генерации данных
fake = Faker()
# stepick.org/lesson/237240/step/9?unit=209628 - задание
try:
    # Инициализируем веб-драйвер
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")

    # Находим все текстовые поля на странице
    elements = browser.find_elements(By.CSS_SELECTOR, "input[type='text']")

    for element in elements:
        field_name = element.get_attribute("name").lower()
        # Генерируем данные в зависимости от названия поля
        if "name" in field_name:
            element.send_keys(fake.name())
        elif "e-mail" in field_name:
            element.send_keys(fake.email())
        elif "address" in field_name:
            element.send_keys(fake.address())
        elif "phone" in field_name:
            element.send_keys(fake.phone_number())
        elif "date" in field_name:
            element.send_keys(fake.date())
        elif "time" in field_name:
            element.send_keys(fake.time())
        elif "url" in field_name:
            element.send_keys(fake.url())
        elif "company" in field_name:
            element.send_keys(fake.company())
        elif "job" in field_name:
            element.send_keys(fake.job())
        elif "postcode" in field_name:
            element.send_keys(fake.postcode())
        elif "city" in field_name:
            element.send_keys(fake.city())
        elif "country" in field_name:
            element.send_keys(fake.country())
        else:
            # Для всех остальных полей вставляем случайное слово
            element.send_keys(fake.word())

    # Находим и нажимаем кнопку отправки формы
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
     # button.click()

finally:
    # Даем время на копирование кода (если требуется)
    time.sleep(30)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла