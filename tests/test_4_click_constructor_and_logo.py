import pytest
from selenium.webdriver.support.ui import WebDriverWait
from locators import BASE_URL, MAIN_LOGIN_BTN, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, PROFILE_LINK, CONSTRUCTOR_TAB, LOGO_LINK
from utils.fixtures import driver
from utils.helpers import login_and_go_to_profile

TEST_EMAIL = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"

class TestClickConstructorAndLogo:
    def test_click_constructor_from_profile(self, driver):
        login_and_go_to_profile(driver, BASE_URL, MAIN_LOGIN_BTN, PROFILE_LINK, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        driver.find_element(*CONSTRUCTOR_TAB).click()
        WebDriverWait(driver, 10).until(lambda d: d.current_url == f"{BASE_URL}/")
        assert driver.current_url == f"{BASE_URL}/"

    def test_click_logo_from_profile(self, driver):
        login_and_go_to_profile(driver, BASE_URL, MAIN_LOGIN_BTN, PROFILE_LINK, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        driver.find_element(*LOGO_LINK).click()
        WebDriverWait(driver, 10).until(lambda d: d.current_url == f"{BASE_URL}/")
        assert driver.current_url == f"{BASE_URL}/"