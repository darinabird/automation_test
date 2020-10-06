from selenium import webdriver
import time
import math

from selenium.common.exceptions import NoSuchElementException

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


# функция рассчета формулы на сайте
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # кликнуть кнопку
    first_button = browser.find_element_by_css_selector("button.btn")
    first_button.click()

    # принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # решить капчу
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    print(f"First addend is {x}")
    x = calc(x)

    # вставить ответ
    input1 = browser.find_element_by_tag_name("input#answer.form-control")
    input1.send_keys(x)

    # подтвердить
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

except NoSuchElementException:
    print("^_^ Change selector ^_^")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
