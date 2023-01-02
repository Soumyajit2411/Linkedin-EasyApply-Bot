import time, config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LinkedinButtons:

    def easyApplyButton(self, driver):
        try:
            button = driver.find_element(
                By.XPATH, '//button[contains(@class, "jobs-apply-button")]')
            time.sleep(1)
            EasyApplyButton = button
        except:
            EasyApplyButton = False

        return EasyApplyButton

    def chooseButtonConfig(self, driver):
        try:
            driver.find_element(
                By.XPATH, "//button[@aria-label='Choose Resume']").click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def nextButtonConfig(self, driver):
        try:
            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Continue to next step']").click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def reviewButtonConfig(self, driver):
        try:
            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Review your application']").click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def followCompaniesConfig(self, driver):
        try:
            if str(config.followCompanies) in "False":
                driver.find_element(
                    By.XPATH,
                    "//label[@for='follow-company-checkbox']").click()
                time.sleep(1)
        except NoSuchElementException:
            pass

    def submitButtonConfig(self, driver):
        try:
            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Submit application']").click()
            time.sleep(5)
        except NoSuchElementException:
            pass