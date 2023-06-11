from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


CHROME_DRIVER_PATH = r"C:\Users\Fidelis\PycharmProjects\100-days-of-coding-in-python\100-Days\Day_48\chrome_driver.exe"

driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)
driver.get("https://tinder.com/")

time.sleep(5)
login_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
login_button.click()

time.sleep(5)
fb_login = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
driver.quit()