import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.fixtures import driver
from locators import  BASE_URL,MAIN_LOGIN_BTN, PROFILE_LINK, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON

TEST_EMAIL    = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"

def test_account_page_url(driver):
    driver.get(f"{BASE_URL}/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_LOGIN_BTN)).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_LINK)).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
    assert driver.current_url.endswith("/account/profile")