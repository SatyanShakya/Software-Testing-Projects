import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.set_window_size(375, 812)  # iPhone X size

# driver=webdriver.Firefox()
# driver=webdriver.Edge()
# driver=webdriver.Ie()

email ="John@gmail.com"
otp ="123456"
password = "Test@123"

try:

    driver.get("https://dev.visacentre.com.au/")

    country = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@data-value='nepal']"))
    )
    time.sleep(1)
    country.click()

    apply_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Apply']"))
    )
    apply_button.click()
    time.sleep(1)

    driver.get("https://dev.visacentre.com.au/visa/nepal-to-united-kingdom")

    apply = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//button[text()='Apply for Visa']"))
    )
    apply.click()
    time.sleep(1)

    apply_yes = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//button[text()='Yes']"))
    )
    apply_yes.click()
    time.sleep(1)

    apply_search = driver.find_element(By.XPATH,"//input[@placeholder='Search']")

    apply_search.send_keys("nepal")
    apply_search.send_keys(Keys.RETURN)
    time.sleep(1)

    apply_search_submit = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//button[@type='submit']"))
    )
    apply_search_submit.click()
    time.sleep(1)

    #------------------- Email ---------------------------------------------------
    
    email_field = driver.find_element(By.XPATH, "//input[@placeholder='example@gmail.com']")

    email_field.send_keys(email)
    time.sleep(1)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)    
    
#-------------------------- login password -----------------------------------------
    
    if driver.current_url == "https://dev.visacentre.com.au/auth/check-password":

        password_field = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='.................']"))
        )

        password_field.click
        password_field.send_keys(password)
        time.sleep(1)

        password_field.send_keys(Keys.RETURN)
        time.sleep(2)

#------------------------------- login OTP ---------------------------------    

    if driver.current_url == "https://dev.visacentre.com.au/auth/login-verify-otp":
        
        login_otp = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-input-otp='true']"))
        )

        login_otp.send_keys(otp)
        login_otp.send_keys(Keys.RETURN)
        time.sleep(5)



finally:
    driver.quit()