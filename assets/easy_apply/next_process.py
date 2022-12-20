import time, math, config
from selenium.webdriver.common.by import By
import assets.easy_apply.questions as questions
import assets.easy_apply.easy_apply_buttons as easy_apply_buttons


class LinkedinNextButtons:

    def findPercentage(self, driver):
        easy_apply_buttons.LinkedinButtons().nextButtonConfig(driver)
        comPercentage = driver.find_element(By.XPATH,
                                            "//span[@role='note']").text
        percenNumber = int(comPercentage[0:comPercentage.index("%")])
        return percenNumber

    def applyProcess(self, driver, offerPage):
        percentage = self.findPercentage(driver)
        applyPages = math.floor(100 / percentage)
        result = ""
        try:
            easy_apply_buttons.LinkedinButtons().chooseButtonConfig(driver)
            questions.LinkedinQuestions().additionalConfig(driver, applyPages)
            easy_apply_buttons.LinkedinButtons().followCompaniesConfig(driver)
            easy_apply_buttons.LinkedinButtons().reviewButtonConfig(driver)
            easy_apply_buttons.LinkedinButtons().submitButtonConfig(driver)
            result = "Just Applied to this job: " + str(offerPage)
        except:
            result = "Pages, couldn't apply to this job! Extra info needed. Link: " + str(
                offerPage)
        return result