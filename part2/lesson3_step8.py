import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не снизится до 100
needed_price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

submit = browser.find_element_by_id("book")
submit.click()


# функция рассчета формулы на сайте
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # решить капчу
    x = browser.find_element_by_css_selector("span#input_value.nowrap").text
    print(f"First addend is {x}")
    x = calc(x)

    # вставить ответ
    input1 = browser.find_element_by_tag_name("input#answer.form-control")
    input1.send_keys(x)

    # подтвердить
    submit = browser.find_element_by_css_selector("button#solve")
    submit.click()

except NoSuchElementException:
    print("^_^ Change selector ^_^")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
