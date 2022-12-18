import time
from selenium.webdriver.common.by import By
import additional_questions
from selenium.common.exceptions import NoSuchElementException


class LinkedinQuestions:

    def checkboxConfig(self, driver, applyPages):
        for pages in range(applyPages - 2):
            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Continue to next step']").click()
            time.sleep(1)
            try:
                driver.find_element(
                    By.XPATH,
                    "//h3[contains(.,'Additional Questions')]").click()
                time.sleep(1)
                try:
                    questions = driver.find_elements(
                        By.XPATH,
                        "//label[@class='artdeco-text-input--label']")
                    time.sleep(1)
                    questionno = []
                    for question in questions:
                        questionno = question.get_attribute("value")
                    # driver.find_element(
                    #     By.XPATH,
                    #     "//input[@class=' artdeco-text-input--input']").click(
                    #     )
                    # time.sleep(1)
                except NoSuchElementException:
                    pass
            except NoSuchElementException:
                pass
