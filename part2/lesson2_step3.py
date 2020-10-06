from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # ищу элементы на странице
    x = browser.find_element_by_css_selector(".nowrap#num1").text
    print(f"First addend is {x}")
    y = browser.find_element_by_css_selector(".nowrap#num2").text
    print(f"Second addend is {y}")
    sum = int(x) + int(y)
    print(sum)

    # выбираю нужный ответ из dropdown меню
    browser.find_element_by_xpath("select").click()
    browser.find_element_by_css_selector(f"[value='{sum}']").click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
