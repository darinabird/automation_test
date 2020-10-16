import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
        time.sleep(5)
        answer = math.log(int(time.time()))
        blank = browser.find_element_by_css_selector('textarea[placeholder="Type your answer here..."]')
        blank.sendkeys(answer)

        button = WebDriverWait(browser, 5).until(ec.element_to_be_clickable((By.ID, "submit-button"))
                                                 )
        button.click()

        message = browser.find_element_by_id("verify_message")
        assert "Correct!" in message.text
