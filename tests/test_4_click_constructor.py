import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import BASE_URL, MAIN_LOGIN_BTN, LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON, LOGO_LINK, PROFILE_LINK, CONSTRUCTOR_TAB
from utils.fixtures import driver

TEST_EMAIL    = "leonoveduard33@yandex.ru"
TEST_PASSWORD = "password123"

def login_to_account(driver):
    driver.get(f"{BASE_URL}/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_LOGIN_BTN)).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

def test_click_constructor_from_profile(driver):
    login_to_account(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_LINK)).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))

    driver.find_element(*CONSTRUCTOR_TAB).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(f"{BASE_URL}/"))
    assert driver.current_url == f"{BASE_URL}/"


def test_click_logo_from_profile(driver):
    login_to_account(driver)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PROFILE_LINK)).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))

    driver.find_element(*LOGO_LINK).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(f"{BASE_URL}/"))
    assert driver.current_url == f"{BASE_URL}/"