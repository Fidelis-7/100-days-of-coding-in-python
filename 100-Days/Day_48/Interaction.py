from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER = r"C:\Users\Fidelis\PycharmProjects\100-days-of-coding-in-python\100-Days\Day_48\chrome_driver.exe"

driver = webdriver.Chrome(executable_path = CHROME_DRIVER)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.CSS_SELECTOR, "#articlecount a")


search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)


# search_bar.click()



# number.click() 

driver.close() 