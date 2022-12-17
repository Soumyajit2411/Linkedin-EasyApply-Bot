import time
from selenium.webdriver.common.by import By


class LinkedinButtons:

    def easyApplyButton(self, driver):
        try:
            time.sleep(3)
            button = driver.find_element(
                By.XPATH, '//button[contains(@class, "jobs-apply-button")]')
            EasyApplyButton = button
        except:
            EasyApplyButton = False

        return EasyApplyButton