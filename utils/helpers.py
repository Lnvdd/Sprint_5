from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, email_loc, password_loc, button_loc, email, password):
    driver.find_element(*email_loc).send_keys(email)
    driver.find_element(*password_loc).send_keys(password)
    driver.find_element(*button_loc).click()

def login_and_go_to_profile(driver, base_url, main_login_btn, profile_link, login_email_input, login_password_input, login_button, email, password):
    driver.get(base_url)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(main_login_btn)).click()
    login(driver, login_email_input, login_password_input, login_button, email, password)
    WebDriverWait(driver, 10).until(EC.url_contains("/login"))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(profile_link)).click()
    WebDriverWait(driver, 10).until(EC.url_contains("/account/profile"))
