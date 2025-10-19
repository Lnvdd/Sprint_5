import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, MAIN_LOGIN_BTN, PROFILE_LINK, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, LOGOUT_BUTTON
from utils.fixtures import driver
from utils.helpers import login_and_go_to_profile

TEST_EMAIL = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"

class TestLogout:
    def test_logout_from_profile(self, driver):
        login_and_go_to_profile(driver, BASE_URL, MAIN_LOGIN_BTN, PROFILE_LINK, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        driver.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login")