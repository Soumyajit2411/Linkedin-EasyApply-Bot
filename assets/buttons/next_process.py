import time, math, config
from selenium.webdriver.common.by import By
import assets.buttons.questions as questions


class LinkedinNextButtons:

    def findPercentage(self, driver):
        driver.find_element(
            By.XPATH, "//button[@aria-label='Continue to next step']").click()
        time.sleep(5)
        comPercentage = driver.find_element(By.XPATH,
                                            "//span[@role='note']").text
        percenNumber = int(comPercentage[0:comPercentage.index("%")])
        return percenNumber

    def applyProcess(self, driver, offerPage):
        percentage = self.findPercentage(driver)
        applyPages = math.floor(100 / percentage)
        result = ""
        try:
            for pages in range(applyPages - 2):
                driver.find_element(
                    By.XPATH,
                    "//button[@aria-label='Continue to next step']").click()
                time.sleep(1)
            # questions.LinkedinQuestions().checkboxConfig(driver,applyPages)

            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Review your application']").click()
            time.sleep(1)

            if config.followCompanies is False:
                driver.find_element(
                    By.XPATH,
                    "//label[@for='follow-company-checkbox']").click()
                time.sleep(1)

            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Submit application']").click()
            time.sleep(1)

            result = "Just Applied to this job: " + str(offerPage)
        except:
            result = "Pages, couldn't apply to this job! Extra info needed. Link: " + str(
                offerPage)
        return result