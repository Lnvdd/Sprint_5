import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, PASSWORD_ERROR_MSG
from utils.fixtures import driver
from utils.data_generator import generate_email, generate_password

def test_successful_registration(driver):
    driver.get(f"{BASE_URL}/register")
    driver.find_element(*NAME_INPUT).send_keys("Eduard Leonov")
    email = generate_email("eduard", "leonov", "33")
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    password = generate_password(6)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REGISTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

def test_registration_with_short_password(driver):
    driver.get(f"{BASE_URL}/register")
    driver.find_element(*NAME_INPUT).send_keys("Eduard Leonov")
    email = generate_email("eduard", "leonov", "33")
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys("123")
    driver.find_element(*REGISTER_BUTTON).click()
    assert driver.find_element(*PASSWORD_ERROR_MSG).is_displayed()