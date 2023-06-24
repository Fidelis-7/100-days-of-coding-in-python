from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

SIMILAR_ACCOUNT = "thechefchi"
INSTA_USERNAME = "fidelis1277"
INSTA_PASSWORD = "Felix2003!"
CHROME_DRIVER_PATH = r"C:\Users\Fidelis\PycharmProjects\100-days-of-coding-in-python\100-Days\Day_48\chrome_driver.exe"

# CLASS CREATED
class InstaFollower:
    def __init__(self, driver_path):
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service)

    # Open login page
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(INSTA_USERNAME)

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(INSTA_PASSWORD)
        password_field.send_keys(Keys.ENTER)

        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")

        time.sleep(5)

        # Switch to the popup window
        if len(self.driver.window_handles) >= 1:
            self.driver.switch_to.window(self.driver.window_handles[0])

            # Perform actions on the popup window
            follow_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Follow')]")
            for button in follow_buttons:
                try:
                    button.click()
                    time.sleep(1)
                except Exception as e:
                    print(f"Failed to click follow button: {e}")

            # Close the popup window
            self.driver.close()

            # Switch back to the main window
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            print("No popup window found.")

    def follow(self):
        pass

# Instantiate the class and execute the script
instafollower = InstaFollower(CHROME_DRIVER_PATH)
instafollower.login()
instafollower.find_followers()
instafollower.follow()
