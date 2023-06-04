from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r"C:\Users\Fidelis\PycharmProjects\100-days-of-coding-in-python\100-Days\Day_48\chrome_driver.exe"

driver = webdriver.Chrome(executable_path= CHROME_DRIVER_PATH)

driver.get("https://www.python.org/")

price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)
# driver.close()
driver.quit()