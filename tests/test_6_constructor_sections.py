import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import BASE_URL, CONSTRUCTOR_TAB, TAB_BUNS, TAB_SAUCES, TAB_FILLINGS, HEADER_BUNS, HEADER_SAUCES, HEADER_FILLINGS
from utils.fixtures import driver

@pytest.fixture(autouse=True)
def open_constructor(driver):
    driver.get(f"{BASE_URL}/")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CONSTRUCTOR_TAB)).click()

def test_fillings_section(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_FILLINGS)).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HEADER_FILLINGS))

def test_sauces_section(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_SAUCES)).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HEADER_SAUCES))

def test_buns_section(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_FILLINGS)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(TAB_BUNS)).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(HEADER_BUNS))