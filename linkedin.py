import time, constants, downloads.config as config
import assets.job_details as job_details
import assets.url.job_url as job_url
import assets.login as login
import assets.easy_apply.next_process as next_process
import assets.easy_apply.easy_apply_buttons as easy_apply_buttons
import assets.utils as utils
import assets.url.keyword_url as keyword_url
import assets.url.write_results as write_results
import assets.alert as alert
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.firefox import GeckoDriverManager


class Linkedin:

    def __init__(self):
        try:
            if "chrome" in config.browser:
                self.driver = webdriver.Chrome(ChromeDriverManager().install())
            else:
                self.driver = webdriver.Firefox(
                    executable_path=GeckoDriverManager().install())
            self.driver.get(constants.home)
        except Exception as e:
            print(e)
            pass
        login.LinkedinLogin().Login(self.driver)

    def linkJobApply(self):
        countApplied = 0
        countJobs = 0
        keyword_url.LinkedinUrlGenerate().generateUrls()
        urlData = write_results.LinkedinWriteResults().getUrlDataFile()
        for url in urlData:
            self.driver.get(url)
            delay = 20
            totalJobss = []
            try:
                totalJobss = WebDriverWait(self.driver, delay).until(
                    EC.presence_of_element_located((By.XPATH, '//small')))
            except TimeoutException:
                print("Loading took too much time!")
                self.driver.close()
            totalJobs = totalJobss.text
            totalPages = int(utils.jobsToPages(totalJobs))
            urlWords = utils.urlToKeywords(url)
            lineToWrite = "\n Category: " + urlWords[
                0] + ", Location: " + urlWords[1] + ", Applying " + str(
                    totalJobs) + " jobs."
            write_results.LinkedinWriteResults().displayWriteResults(
                lineToWrite)

            for page in range(totalPages):
                currentPageJobs = constants.jobsPerPage * page
                offersPerPage = alert.LinkedinAlert().jobs_alert(
                    self.driver, currentPageJobs, url)
                offerIds = []
                for offer in offersPerPage:
                    offerId = offer.get_attribute("data-occludable-job-id")
                    offerIds.append(int(offerId.split(":")[-1]))
                for jobID in offerIds:
                    offerPage = constants.view + str(jobID)
                    self.driver.get(offerPage)
                    job_url.LinkedinJobUrlGenerate().storeJobResults(offerPage)
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
                        button = easy_apply_buttons.LinkedinButtons(
                        ).easyApplyButton(self.driver)
                        if button is not False:
                            button.click()
                            time.sleep(0.5)
                            countApplied += 1
                            try:
                                easy_apply_buttons.LinkedinButtons(
                                ).chooseButtonConfig(self.driver)
                                easy_apply_buttons.LinkedinButtons(
                                ).submitButtonConfig(self.driver)
                                lineToWrite = jobProperties + " | " + "Just Applied to this job: " + str(
                                    offerPage)
                                write_results.LinkedinWriteResults(
                                ).displayWriteResults(lineToWrite)
                            except:
                                try:
                                    result = next_process.LinkedinNextButtons(
                                    ).applyProcess(self.driver, offerPage)
                                    lineToWrite = jobProperties + " | " + result
                                    write_results.LinkedinWriteResults(
                                    ).displayWriteResults(lineToWrite)
                                except:
                                    lineToWrite = jobProperties + " | " + "Cannot apply to this Job! " + str(
                                        offerPage)
                                    write_results.LinkedinWriteResults(
                                    ).displayWriteResults(lineToWrite)
                        else:
                            lineToWrite = jobProperties + " | " + "Already applied! Job: " + str(
                                offerPage)
                            write_results.LinkedinWriteResults(
                            ).displayWriteResults(lineToWrite)
        self.driver.close()
        return


start = time.time()
Linkedin().linkJobApply()
end = time.time()
print(str(round((time.time() - start) / 60)))
