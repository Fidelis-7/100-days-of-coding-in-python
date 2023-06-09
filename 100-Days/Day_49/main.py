from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

CHROME_DRIVER_PATH = r"C:\Users\Fidelis\PycharmProjects\100-days-of-coding-in-python\100-Days\Day_48\chrome_driver.exe"

driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
driver.get("https://www.linkedin.com/login")
# driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3609036199&keywords=python%20developer%20&location=Accra&refresh=true")

# username field
username_field = driver.find_element(By.CSS_SELECTOR, "#username")
username_field.send_keys("fidelismartin90@gmail.com")

# password_field
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.send_keys("fidelisjunior")
password_field.send_keys(Keys.ENTER)

# signin_btn field
signin_btn = driver.find_element(By.CLASS_NAME, "login__form_action_container")
signin_btn.click()

# continue_with_google = driver.find_element(By.CSS_SELECTOR, ".nsm7Bb-HzV7m-LgbsSe-BPrWId")
# continue_with_google.click()


# wait for 20 seconds
time.sleep(120)



driver.quit()