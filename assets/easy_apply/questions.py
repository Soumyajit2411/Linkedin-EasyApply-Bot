import time, config
from selenium.webdriver.common.by import By
import additional_questions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import assets.easy_apply.easy_apply_buttons as easy_apply_buttons


class LinkedinQuestions:

    def additionalConfig(self, driver, applyPages):
        for pages in range(applyPages - 2):
            easy_apply_buttons.LinkedinButtons().nextButtonConfig(driver)
            try:
                driver.find_element(
                    By.XPATH, "//h3[contains(.,'Additional Questions')]")
                self.radioButtonConfig(driver)
                self.inputFieldConfig(driver)
                self.checkboxConfig(driver)
            except NoSuchElementException:
                pass
            try:
                driver.find_element(By.XPATH,
                                    "//h3[contains(.,'Domande aggiuntive')]")
                self.radioButtonConfig(driver)
                self.inputFieldConfig(driver)
                self.checkboxConfig(driver)
            except NoSuchElementException:
                pass
            try:
                driver.find_element(By.XPATH,
                                    "//h3[contains(.,'Work authorization')]")
                self.workAuthorizationConfig(driver)
            except NoSuchElementException:
                pass

    def checkboxConfig(self, driver):

        try:
            questions = driver.find_elements(
                By.XPATH, "//label[@data-test-text-entity-list-form-title='']")
            checkboxData = additional_questions.LinkedinAdditionalQuestions(
            ).checkboxConfigData()
            i = 1
            for question in questions:
                questionno = question.get_attribute("innerHTML")
                q = str(config.defaultCheck)
                for x in checkboxData.keys():
                    if x.lower() in str(questionno).lower():
                        q = checkboxData[x]
                souki = "(//select[@data-test-text-entity-list-form-select=''])[" + str(
                    i) + "]"
                d = Select(driver.find_element(By.XPATH, souki))
                try:
                    d.select_by_visible_text(str(q))
                except:
                    pass
                d.select_by_index(1)
                time.sleep(0.5)
                i += 1
        except NoSuchElementException:
            pass
        except:
            pass

    def inputFieldConfig(self, driver):

        try:
            questions = driver.find_elements(
                By.XPATH, "//label[@class='artdeco-text-input--label']")
            inputFieldsData = additional_questions.LinkedinAdditionalQuestions(
            ).inputFieldConfigData()
            i = 1
            for question in questions:
                questionno = question.get_attribute("innerHTML")
                souki = "(//input[@class=' artdeco-text-input--input'])[" + str(
                    i) + "]"
                ko = driver.find_element(By.XPATH,
                                         souki).get_attribute("value")
                if len(ko) == 0:
                    q = str(config.defaultInput)
                    for x in inputFieldsData.keys():
                        if x.lower() in str(questionno).lower():
                            if type(inputFieldsData[x]) is dict:
                                for k in inputFieldsData[x].keys():
                                    if k.lower() in str(questionno).lower():
                                        q = inputFieldsData[x][k]
                            else:
                                q = inputFieldsData[x]
                    driver.find_element(By.XPATH, souki).send_keys(q)
                    time.sleep(0.5)
                i += 1
        except NoSuchElementException:
            pass
        except:
            pass

    def radioButtonConfig(self, driver):

        try:
            questions = driver.find_elements(
                By.XPATH,
                "//legend[@data-test-form-builder-radio-button-form-component__title='true']"
            )
            radioButtonData = additional_questions.LinkedinAdditionalQuestions(
            ).radioConfigData()
            i = 1
            for question in questions:
                questionno = question.get_attribute("innerHTML")
                q = str(config.defaultRadio)
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
                time.sleep(0.5)
                i += 1
        except NoSuchElementException:
            pass
        except:
            pass

    def workAuthorizationConfig(self, driver):
        try:
            if str(config.workAuthorization) == "Yes":
                souki = "//label[@data-test-text-selectable-option__label='Yes']"
            else:
                souki = "//label[@data-test-text-selectable-option__label='No']"
            driver.find_element(By.XPATH, souki).click()
            time.sleep(0.5)
        except NoSuchElementException:
            pass
        except:
            pass
