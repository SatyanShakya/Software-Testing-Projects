import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

driver = webdriver.Chrome()
driver.set_window_size(375,812)

#----------------------------- Inputs -------------------------------------------------
fake = Faker()

email ="satyantest@gmail.com"
otp ="123456"
newpassword = "Test@1234"
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

#----------------------------- Email ---------------------------------------------------
    
    email_field = driver.find_element(By.XPATH, "//input[@placeholder='example@gmail.com']")

    email_field.send_keys(email)
    time.sleep(1)
    email_field.send_keys(Keys.RETURN)
    time.sleep(1)    

#-------------------------- forgot password -----------------------------------------
    
    if driver.current_url == "https://dev.visacentre.com.au/auth/check-password":
        
        forgot_password_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Forgot Password']"))
        )
        forgot_password_link.click()    
        time.sleep(2)

 #----------------------------- Email ---------------------------------------------------
    
    if driver.current_url == "https://dev.visacentre.com.au/auth/forgot-password":
        
        email_field = driver.find_element(By.XPATH, "//input[@placeholder='example@gmail.com']")

        email_field.send_keys(email)
        time.sleep(1)
        email_field.send_keys(Keys.RETURN)
        time.sleep(2)    

#------------------------------- forgot password OTP ---------------------------------    

    if driver.current_url == "https://dev.visacentre.com.au/auth/forgot-password/verify":
        
        login_otp = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@data-input-otp='true']"))
        )

        login_otp.send_keys(otp)
        time.sleep(send_otp_after)
        login_otp.send_keys(Keys.RETURN)
        time.sleep(2)

    #------------------------ Register set password ------------------------------------------ 
    
    if driver.current_url == "https://dev.visacentre.com.au/auth/reset-password":

        password_field = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        confirm_password = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.NAME, "confirmPassword"))
        )

        password_field.send_keys(newpassword)
        time.sleep(1)
        confirm_password.send_keys(confirmpassword)
        time.sleep(1)

        save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Save']"))
        )
        save_button.click()
        time.sleep(5)


    print("----------------Test Performed Successfully--------------------")

finally:
    driver.quit()
