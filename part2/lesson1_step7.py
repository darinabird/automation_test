from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищу элементы на странице
    x_el = browser.find_element_by_id("treasure")
    x_el = x_el.get_attribute("valuex")
    x_el = x_el.text
    x = calc(x_el)

    # ввод ответа в текстовое поле
    input1 = browser.find_elements_by_css_selector("input#answer")
    input1.send_keys(x)

    # отмечаю чекбокс
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
