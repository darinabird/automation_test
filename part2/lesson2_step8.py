from selenium import webdriver
import time
import os

from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    # заполнить текстовые поля
    name = browser.find_element_by_css_selector("input[name=firstname]")
    name.send_keys("Darina")

    last_name = browser.find_element_by_css_selector("input[name=lastname]")
    last_name.send_keys("Bird")

    mail = browser.find_element_by_css_selector("input[name=email]")
    mail.send_keys("darinabird46722@gmail.com")

    # загрузить файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    element_upload = browser.find_element_by_css_selector("input#file")
    element_upload.send_keys(file_path)

    # отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

except NoSuchElementException:
    print("\n>_< Change selector >_<")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
