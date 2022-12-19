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
            questions.LinkedinQuestions().chooseConfig(driver)
            questions.LinkedinQuestions().additionalConfig(driver, applyPages)
            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Review your application']").click()
            time.sleep(5)
            questions.LinkedinQuestions().followCompaniesConfig(driver)

            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Submit application']").click()
            time.sleep(5)

            result = "Just Applied to this job: " + str(offerPage)
        except:
            result = "Pages, couldn't apply to this job! Extra info needed. Link: " + str(
                offerPage)
        return result