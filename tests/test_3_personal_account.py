import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, MAIN_LOGIN_BTN, PROFILE_LINK, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON
from utils.fixtures import driver
from utils.helpers import login

TEST_EMAIL = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"

class TestAccountPage:
    def test_account_page_url(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_LOGIN_BTN)).click()
        login(driver, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_LINK)).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
        assert driver.current_url.endswith("/account/profile")