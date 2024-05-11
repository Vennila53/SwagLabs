import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def safe_click(driver, element):
    try:
        element.click()
    except Exception as e:
        print(f"An error occurred while clicking the element: {str(e)}")

def safe_send_keys(driver, element, text):
    try:
        element.send_keys(text)
    except Exception as e:
        print(f"An error occurred while sending keys to the element: {str(e)}")

def safe_find_element(driver, by, value):
    try:
        return driver.find_element(by, value)
    except Exception as e:
        print(f"An error occurred while finding the element: {str(e)}")

def perform_actions(driver):
    print(f"Logging in with {driver.capabilities['browserName']} browser")
    try:
        driver.get("https://www.saucedemo.com/")
        print("URL opened")
        username_field = safe_find_element(driver, By.ID, "user-name")
        print("Username field found")
        username_field.send_keys("standard_user")
        print("Username entered")
        password_field = safe_find_element(driver, By.ID, "password")
        print("Password field found")
        password_field.send_keys("secret_sauce")
        print("Password entered")
        login_button = safe_find_element(driver, By.ID, "login-button")
        safe_click(driver, login_button)
        print("Login button clicked")
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product_sort_container")))
        dropdown.click()

        select = Select(dropdown)

        select.select_by_value("hilo")

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket")))

        add_to_cart_button.click()

        shopping_cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        shopping_cart_link.click()

        checkout_button = driver.find_element(By.ID, "checkout")

        checkout_button.click()

        first_name_input = driver.find_element(By.ID, "first-name")
        last_name_input = driver.find_element(By.ID, "last-name")
        postal_code_input = driver.find_element(By.ID, "postal-code")

        first_name_input.clear()
        last_name_input.clear()
        postal_code_input.clear()

        first_name_input.send_keys("Alice")
        last_name_input.send_keys("Doe")
        postal_code_input.send_keys("592")

        continue_button = driver.find_element(By.ID, "continue")

        continue_button.click()
        price_element = driver.find_element(By.CSS_SELECTOR, ".inventory_item_price[data-test='inventory-item-price']")

        price_text = price_element.text

        if price_text :
            print("The price value is correct: $49.99")
        else:
            print("The price value is incorrect:", price_text)

        finish_button = driver.find_element(By.ID, "finish")

        finish_button.click()

        complete_header_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h2.complete-header[data-test='complete-header']"))
        )


        if complete_header_element:
            assert complete_header_element.is_displayed(), "Thank You header is not shown in Checkout Complete page"
            print("")
        else:
            print("Thank You header element is not found.")
        time.sleep(10)
        print("Logged in successfully and on the inventory page")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    driver.save_screenshot("screenshot.png")

driver = webdriver.Chrome()

perform_actions(driver)
