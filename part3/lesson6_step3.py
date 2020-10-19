import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.keys import Keys


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
        browser.implicitly_wait(10)

        blank = browser.find_element_by_css_selector("textarea")
        blank.send_keys(f"{answer}")

        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()

        message = browser.find_element_by_css_selector(".smart-hints__hint")
        assert "Correct!" in message.text
