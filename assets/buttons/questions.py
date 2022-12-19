import time, config
from selenium.webdriver.common.by import By
import additional_questions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


class LinkedinQuestions:

    def chooseConfig(self, driver):
        try:
            driver.find_element(
                By.XPATH, "//button[@aria-label='Choose Resume']").click()
            time.sleep(1)
        except NoSuchElementException:
            pass

    def additionalConfig(self, driver, applyPages):
        for pages in range(applyPages - 2):
            driver.find_element(
                By.XPATH,
                "//button[@aria-label='Continue to next step']").click()
            time.sleep(1)
            try:
                driver.find_element(
                    By.XPATH, "//h3[contains(.,'Additional Questions')]")
                time.sleep(1)
                self.radioButtonConfig(driver)
                self.inputFieldConfig(driver)
                self.checkboxConfig(driver)
            except NoSuchElementException:
                pass
            try:
                driver.find_element(By.XPATH,
                                    "//h3[contains(.,'Work authorization')]")
                time.sleep(1)
                self.workAuthorizationConfig(driver)
            except NoSuchElementException:
                pass

    def checkboxConfig(self, driver):

        try:
            questions = driver.find_elements(
                By.XPATH, "//label[@data-test-text-entity-list-form-title='']")
            time.sleep(1)
            checkboxData = additional_questions.LinkedinAdditionalQuestions(
            ).checkboxConfigData()
            i = 1
            for question in questions:
                questionno = question.get_attribute("innerHTML")
                q = "Yes"
                for x in checkboxData.keys():
                    if x.lower() in str(questionno).lower():
                        q = checkboxData[x]
                souki = "(//select[@data-test-text-entity-list-form-select=''])[" + str(
                    i) + "]"
                d = Select(driver.find_element(By.XPATH, souki))
                d.select_by_visible_text(str(q))
                time.sleep(1)
                i += 1
        except NoSuchElementException:
            return
        except:
            pass
        return 0

    def inputFieldConfig(self, driver):

        try:
            questions = driver.find_elements(
                By.XPATH, "//label[@class='artdeco-text-input--label']")
            time.sleep(1)
            inputFieldsData = additional_questions.LinkedinAdditionalQuestions(
            ).inputFieldConfigData()
            i = 1
            for question in questions:
                questionno = question.get_attribute("innerHTML")
                souki = "(//input[@class=' artdeco-text-input--input'])[" + str(
                    i) + "]"
                ko = driver.find_element(By.XPATH, souki).is_displayed()
                if str(ko) in "True":
                    q = "1"
                    for x in inputFieldsData.keys():
                        if x.lower() in str(questionno).lower():
                            if type(inputFieldsData[x]) is dict:
                                for k in inputFieldsData[x].keys():
                                    if k.lower() in str(questionno).lower():
                                        q = inputFieldsData[x][k]
                            else:
                                q = inputFieldsData[x]
                    driver.find_element(By.XPATH, souki).send_keys(q)
                    time.sleep(1)
                i += 1
        except NoSuchElementException:
            return
        except:
            pass
        return 0

    def radioButtonConfig(self, driver):

        try:
            questions = driver.find_elements(
                By.XPATH,
                "//legend[@data-test-form-builder-radio-button-form-component__title='true']"
            )
            time.sleep(1)
            radioButtonData = additional_questions.LinkedinAdditionalQuestions(
            ).radioConfigData()
            i = 1
            for question in questions:
                questionno = question.get_attribute("innerHTML")
                q = "Yes"
                for x in radioButtonData.keys():
                    if x.lower() in str(questionno).lower():
                        q = radioButtonData[x]
                if q == "Yes":
                    souki = "(//label[@data-test-text-selectable-option__label='Yes'])[" + str(
                        i) + "]"
                else:
                    souki = "(//label[@data-test-text-selectable-option__label='No'])[" + str(
                        i) + "]"
                driver.find_element(By.XPATH, souki).click()
                time.sleep(1)
                i += 1
        except NoSuchElementException:
            return
        except:
            pass
        return 0

    def workAuthorizationConfig(self, driver):
        try:
            if str(config.workAuthorization) == "Yes":
                souki = "//label[@data-test-text-selectable-option__label='Yes']"
            else:
                souki = "//label[@data-test-text-selectable-option__label='No']"
            driver.find_element(By.XPATH, souki).click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        except:
            pass

    def followCompaniesConfig(self, driver):
        try:
            if str(config.followCompanies) in "False":
                driver.find_element(
                    By.XPATH,
                    "//label[@for='follow-company-checkbox']").click()
                time.sleep(5)
        except NoSuchElementException:
            pass
        except:
            pass
