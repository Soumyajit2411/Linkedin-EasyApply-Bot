import time, downloads.config as config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LinkedinLogin:

    def Login(self, driver):
        try:
            driver.find_element(By.XPATH,
                                "//*[@id='username']").send_keys(config.email)
            time.sleep(5)
            driver.find_element(By.XPATH, "//*[@id='password']").send_keys(
                config.password)
            time.sleep(5)
            driver.find_element(By.XPATH,
                                "//button[@aria-label='Sign in']").click()
            time.sleep(5)
        except NoSuchElementException:
            print("Path Not Found!")
        except:
            print("Couldnt log in Linkedin.")
            driver.close()