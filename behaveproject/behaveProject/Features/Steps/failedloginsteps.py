import time

from selenium.webdriver.common.by import By

def perform_actions(driver):
    print(f"Logging in with {driver.capabilities['browserName']} browser")
    try:
        driver.get("https://www.saucedemo.com/")
        print("URL opened")
        username_field = driver.find_element(By.ID, "user-name")
        print("Username field found")
        username_field.send_keys("locked_out_user")
        print("Username entered")
        password_field = driver.find_element(By.ID, "password")
        print("Password field found")
        password_field.send_keys("secret_sauce")
        print("Password entered")
        time.sleep(2)
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        time.sleep(2)
        print("Sorry this user has been banned")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    driver.save_screenshot("screenshot.png")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
perform_actions(driver)
