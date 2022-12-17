import time
import assets.job_details as job_details
import assets.buttons.next_process as next_process
import assets.utils as utils
import assets.url.keyword_url as keyword_url
import assets.write_results as write_results
import assets.buttons.easy_apply as easy_apply
import constants, config
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
            self.driver.find_element(
                By.XPATH, "//*[@id='username']").send_keys(config.email)
            time.sleep(5)
            self.driver.find_element(
                By.XPATH, "//*[@id='password']").send_keys(config.password)
            time.sleep(5)
            self.driver.find_element(
                By.XPATH, "//button[@aria-label='Sign in']").click()
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
                    time.sleep(5)
                    countJobs = str(int(countJobs) + 1)
                    jobProperties = job_details.LinkedinJobDetails.getJobProperties(
                        self, self.driver, countJobs)
                    if "blacklisted" in jobProperties:
                        lineToWrite = jobProperties + " | " + "Blacklisted Job, skipped!: " + str(
                            offerPage)
                        write_results.LinkedinWriteResults(
                        ).displayWriteResults(lineToWrite)
                    else:
                        button = easy_apply.LinkedinButtons().easyApplyButton(
                            self.driver)
                        if button is not False:
                            button.click()
                            time.sleep(1)
                            countApplied += 1
                            try:
                                self.driver.find_element(
                                    By.XPATH,
                                    "//button[@aria-label='Submit application']"
                                ).click()
                                time.sleep(5)
                                lineToWrite = jobProperties + " | " + "Just Applied to this job: " + str(
                                    offerPage)
                                write_results.LinkedinWriteResults(
                                ).displayWriteResults(lineToWrite)
                            except:
                                try:
                                    self.driver.find_element(
                                        By.XPATH,
                                        "//button[@aria-label='Continue to next step']"
                                    ).click()
                                    time.sleep(5)
                                    comPercentage = self.driver.find_element(
                                        By.XPATH, "//span[@role='note']").text
                                    percenNumber = int(
                                        comPercentage[0:comPercentage.index("%"
                                                                            )])
                                    result = next_process.LinkedinNextButtons(
                                    ).applyProcess(self.driver, percenNumber,
                                                   offerPage)
                                    lineToWrite = jobProperties + " | " + result
                                    write_results.LinkedinWriteResults(
                                    ).displayWriteResults(lineToWrite)
                                except:
                                    lineToWrite = jobProperties + " | " + "Cannot apply to this Job! " + str(
                                        offerPage)
                                    write_results.LinkedinWriteResults(
                                    ).displayWriteResults(lineToWrite)


start = time.time()
Linkedin().linkJobApply()
end = time.time()
print(str(round((time.time() - start) / 60)))
