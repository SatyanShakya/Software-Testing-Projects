import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://dev.visacentre.com.au/")
    
    nepal_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-value='nepal']"))
    )
    time.sleep(1)
    nepal_option.click()

    apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply']"))
    )
    apply_button.click()
    time.sleep(1)

    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Where Do You Want to Go?']"))
    )
    
    search_terms = ["India","Nepal","Pakistan"]
    for term in search_terms:

        search_input.clear()
        search_input.send_keys(term)
        search_input.send_keys(Keys.RETURN)
        time.sleep(1)
    
    print("----------------Test Performed Successfully--------------------")

finally:
    driver.quit()
