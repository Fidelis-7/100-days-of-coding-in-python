from selenium import webdriver
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = r"C:\Users\Fidelis\PycharmProjects\100-days-of-coding-in-python\100-Days\Day_48\chrome_driver.exe"


driver = webdriver.Chrome(executable_path= CHROME_DRIVER_PATH)

driver.get("https://www.python.org/")

# upcoming_events_dates = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time')
# upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
# print(upcoming_events_dates.text, upcoming_events.text)
upcoming_events= {}
time_of_events = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# for time in time_of_events:
#     print(time.text)

names_of_events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for names in names_of_events:
#     print(names.text)

# for time,names in zip(time_of_events, names_of_events):
#     upcoming_events[time.text] = names.text

for events in range(len(time_of_events)):
    upcoming_events[events] = {"time": time_of_events[events].text, "name": names_of_events[events].text}

print(upcoming_events)


driver.close()


# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]