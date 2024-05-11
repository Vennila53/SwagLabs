import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define a function to perform the actions
def perform_actions(driver):
    print(f"Logging in with {driver.capabilities['browserName']} browser")
    try:
        driver.get("https://www.saucedemo.com/")
        print("URL opened")
        time.sleep(2)
        username_field = driver.find_element(By.ID, "user-name")
        print("Username field found")
        username_field.send_keys("standard_user")
        print("Username entered")
        password_field = driver.find_element(By.ID, "password")
        print("Password field found")
        password_field.send_keys("secret_sauce")
        print("Password entered")
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        print("Login button clicked")
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Swag Labs']")))
        print("Login successful")
        app_logo = driver.find_element(By.XPATH, "//div[@class='app_logo']")
        assert app_logo.is_displayed(), "App logo is not displayed"
        print("App logo found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    driver.save_screenshot("screenshot.png")

chrome_service = ChromeService(ChromeDriverManager().install())
chrome_driver = webdriver.Chrome(service=chrome_service)

perform_actions(chrome_driver)

chrome_driver.quit()
