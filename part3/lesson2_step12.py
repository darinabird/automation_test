import unittest
from unittest import TestCase
from selenium import webdriver
import time

# класс, который наследуется от класса TestCase
from selenium.common.exceptions import NoSuchElementException


class TestEplace(TestCase):

    def test_eplace1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name(".first_block .form-control.third")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_tag_name(".second_block .form-control.first")
        input4.send_keys("Russia")
        input5 = browser.find_element_by_tag_name(".second_block .form-control.second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_eplace2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_tag_name(".first_block .form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_tag_name(".first_block .form-control.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_tag_name(".first_block .form-control.third")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_tag_name(".second_block .form-control.first")
        input4.send_keys("Russia")
        input5 = browser.find_element_by_tag_name(".second_block .form-control.second")
        input5.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Should be absolute value of a number")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == '__main__':
    unittest.main()
