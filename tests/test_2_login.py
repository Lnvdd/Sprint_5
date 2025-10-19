import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, MAIN_LOGIN_BTN, PROFILE_LINK, REGISTER_FORM_LOGIN_LINK, RECOVERY_FORM_LOGIN_LINK, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON
from utils.fixtures import driver
from utils.helpers import login

TEST_EMAIL = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"

class TestLogin:
    def test_login_via_main_link(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_LOGIN_BTN)).click()
        login(driver, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login")

    def test_login_via_personal_account(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_LINK)).click()
        login(driver, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login")

    def test_login_via_register_form(self, driver):
        driver.get(f"{BASE_URL}/register")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(REGISTER_FORM_LOGIN_LINK)).click()
        login(driver, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login")

    def test_login_via_recovery_form(self, driver):
        driver.get(f"{BASE_URL}/forgot-password")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RECOVERY_FORM_LOGIN_LINK)).click()
        login(driver, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, TEST_EMAIL, TEST_PASSWORD)
        WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        assert driver.current_url.endswith("/login")