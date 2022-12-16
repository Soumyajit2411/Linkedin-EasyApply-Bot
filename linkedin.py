import time, math, random, os
import assets.job_details as job_details, assets.utils as utils, assets.url.keyword_url as keyword_url, assets.write_results as write_results, constants, config
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


class Linkedin:

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get("https://www.linkedin.com/login")
        except Exception:
            pass
        try:
            self.driver.find_element("xpath", "//*[@id='username']").send_keys(
                config.email)
            time.sleep(5)
            self.driver.find_element("xpath", "//*[@id='password']").send_keys(
                config.password)
            time.sleep(5)
            self.driver.find_element(
                "xpath", '//*[@id="organic-div"]/form/div[3]/button').click()
            time.sleep(10)
            WebDriverWait(self.driver, 10)
        except NoSuchElementException:
            print("Path Not Found!")
        except:
            print("Couldnt log in Linkedin.")
            exit

    def linkJobApply(self):
        countApplied = 0
        countJobs = 0
        keyword_url.LinkedinUrlGenerate().generateUrls()
        urlData = write_results.LinkedinWriteResults().getUrlDataFile()
        for url in urlData:
            self.driver.get(url)
            totalJobs = self.driver.find_element(By.XPATH, '//small').text
            totalPages = int(utils.jobsToPages(totalJobs))
            urlWords = utils.urlToKeywords(url)
            lineToWrite = "\n Category: " + urlWords[
                0] + ", Location: " + urlWords[1] + ", Applying " + str(
                    totalJobs) + " jobs."
            write_results.LinkedinWriteResults().displayWriteResults(
                lineToWrite)

            for page in range(totalPages):
                currentPageJobs = constants.jobsPerPage * page
                url = url + "&start=" + str(currentPageJobs)
                self.driver.get(url)
                time.sleep(1)
                offersPerPage = self.driver.find_elements(
                    By.XPATH, '//li[@data-occludable-job-id]')
                offerIds = []
                for offer in offersPerPage:
                    offerId = offer.get_attribute("data-occludable-job-id")
                    offerIds.append(int(offerId.split(":")[-1]))
                for jobID in offerIds:
                    offerPage = 'https://www.linkedin.com/jobs/view/' + str(
                        jobID)
                    self.driver.get(offerPage)
                time.sleep(1)
                countJobs += 1
                jobProperties = job_details.LinkedinJobDetails.getJobProperties(
                    countJobs)


Linkedin().linkJobApply()