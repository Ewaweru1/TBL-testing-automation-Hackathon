from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def search_test_automation():
    
    driver = webdriver.Chrome()

    try:
        
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Test Automation")
        search_box.send_keys(Keys.RETURN)

        wait = WebDriverWait(driver, 10)  
        wait.until(EC.presence_of_element_located((By.ID, "search")))

        assert "Test Automation" in driver.page_source

    finally:
        
        driver.quit()

search_test_automation()
