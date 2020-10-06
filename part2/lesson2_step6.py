from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import math
import time


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)


# функция рассчета формулы на сайте
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    print(f"First addend is {x}")
except NoSuchElementException:
    print("^_^ Change selector ^_^")
try:
    x = calc(x)

    # ввод ответа в текстовое поле
    input1 = browser.find_element_by_tag_name("input#answer.form-control")
    input1.send_keys(x)

    # скролл страницы
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    # отмечаю чекбокс
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    # переключаю radiobutton
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
