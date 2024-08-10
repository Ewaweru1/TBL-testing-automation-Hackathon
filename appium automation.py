from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def test():

    driver = webdriver.Remote("url",)

    try:

        username_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "username")
        username_field.send_keys("testuser")

        password_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "password")
        password_field.send_keys("password")

        login_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "login")
        login_button.click()

        settings_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "settings")
        settings_button.click()

        profile_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "profile")
        profile_field.clear()
        profile_field.send_keys("Updated Profile Information")

        save_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "save")
        save_button.click()

    finally:
        
        driver.quit()

test()
