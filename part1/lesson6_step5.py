import time

from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_link_text("224592")
    click_on_button = button.click()

    input1 = browser.find_element_by_tag_name(".form-group:nth-child(1) input.form-control")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name(".form-group:nth-child(2) input.form-control")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_tag_name(".form-group:nth-child(3) input.form-control")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_tag_name(".form-group:nth-child(4) input.form-control")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
