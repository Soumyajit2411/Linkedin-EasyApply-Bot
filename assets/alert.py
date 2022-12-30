import time, config
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LinkedinAlert:

    def jobs_alert(self, driver, currentPageJobs, url):
        url = url + "&start=" + str(currentPageJobs)
        driver.get(url)
        time.sleep(1)
        offersPerPage = driver.find_elements(By.XPATH,
                                             '//li[@data-occludable-job-id]')
        self.alert(driver)
        return offersPerPage

    def alert(self, driver):
        try:
            if str(config.alert) in "True":
                driver.find_element(By.XPATH,
                                    "//span[contains(.,'Set alert')]").click()
                time.sleep(0.5)
            else:
                driver.find_element(By.XPATH,
                                    "//span[contains(.,'Alert on')]").click()
                time.sleep(0.5)
        except NoSuchElementException:
            pass
