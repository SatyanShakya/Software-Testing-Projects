import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

driver = webdriver.Chrome()

#----------------------------- Inputs -------------------------------------------------
fake = Faker()

email ="satyanshakya@gmail.com"
otp ="123456"
firstname =fake.first_name()
lastname =fake.last_name()
password = "Test@123"
confirmpassword = "Test@123"
send_otp_after = 2

try:
    driver.get("https://dev.visacentre.com.au/auth")
    
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

    #------------------- Email ---------------------------------------------------
    
    email_field = driver.find_element(By.XPATH, "//input[@placeholder='example@gmail.com']")

    email_field.send_keys(email)
    time.sleep(1)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)    
    

    #----------------------------------- Register otp ----------------------------------
    
    if driver.current_url == "https://dev.visacentre.com.au/auth/register-verify-otp":

        otp_number = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-input-otp='true']"))
        )

        otp_number.send_keys(otp)
        time.sleep(1)
        otp_number.send_keys(Keys.RETURN)  # Submit OTP
        time.sleep(2)

#------------------------ Register set password ------------------------------------------ 
    
    if driver.current_url == "https://dev.visacentre.com.au/auth/setup-password":

        first_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "firstName"))
        )
        last_name = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.NAME, "lastName"))
        )
        password_field = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        confirm_password = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.NAME, "confirmPassword"))
        )

        first_name.send_keys(firstname)
        time.sleep(1)
        last_name.send_keys(lastname)
        time.sleep(1)
        password_field.send_keys(password)
        time.sleep(1)
        confirm_password.send_keys(confirmpassword)
        time.sleep(1)

        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))
        )
        save_button.click()
        time.sleep(5)

#-------------------------- login password -----------------------------------------
    
    if driver.current_url == "https://dev.visacentre.com.au/auth/check-password":

        password_field = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='.................']"))
        )

        password_field.click
        password_field.send_keys(password)
        time.sleep(1)

        # for _ in range(100):
        #     password_field.send_keys(Keys.RETURN)
        #     time.sleep(2)

        password_field.send_keys(Keys.RETURN)
        time.sleep(2)

#------------------------------- login OTP ---------------------------------    

    if driver.current_url == "https://dev.visacentre.com.au/auth/login-verify-otp":
        
        login_otp = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-input-otp='true']"))
        )

        login_otp.send_keys(otp)
        time.sleep(send_otp_after)
        login_otp.send_keys(Keys.RETURN)
        time.sleep(5)

    print("----------------Test Performed Successfully--------------------")

finally:
    driver.quit()
