import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('num', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestAnswer:
    def test_diff_links(self, browser, num):
        link = f"https://stepik.org/lesson/{num}/step/1"
        browser.get(link)
        answer = math.log(int(time.time()))
        browser.implicitly_wait(5)

        blank = browser.find_element_by_xpath("//textarea[@placeholder='Type your answer here...']")
        blank.sendkeys(answer.text)

        button = browser.find_element_by_css_selector("submit-button")
        button.click()
        message = browser.find_element_by_id("verify_message")
        assert "Correct!" in message.text
