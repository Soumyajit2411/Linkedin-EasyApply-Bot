import config
from selenium.webdriver.common.by import By
import linkedin


class LinkedinJobDetails:

    def getJobProperties(self, count):
        self = linkedin.Linkedin()
        textToWrite = ""
        jobTitle = ""
        jobCompany = ""
        jobLocation = ""
        jobWOrkPlace = ""
        jobPostedDate = ""
        jobApplications = ""

        try:
            jobTitle = self.driver.find_element(
                By.XPATH, "//h1[contains(@class, 'job-title')]").get_attribute(
                    "innerHTML").strip()
            res = [
                blItem for blItem in config.blackListTitles
                if (blItem.lower() in jobTitle.lower())
            ]
            if (len(res) > 0):
                jobTitle += "(blaclisted title: " + ' '.join(res) + ")"
        except Exception as e:
            print("Warning in getting jobTitle: " + str(e)[0:50])
            jobTitle = ""

        try:
            jobCompany = self.driver.find_element(
                By.XPATH,
                "//a[contains(@class, 'ember-view t-black t-normal')]"
            ).get_attribute("innerHTML").strip()
            res = [
                blItem for blItem in config.blacklistCompanies
                if (blItem.lower() in jobTitle.lower())
            ]
            if (len(res) > 0):
                jobCompany += "(blaclisted company: " + ' '.join(res) + ")"
        except Exception as e:
            print("Warning in getting jobCompany: ")
            jobCompany = ""

        try:
            jobLocation = self.driver.find_element(
                By.XPATH, "//span[contains(@class, 'bullet')]").get_attribute(
                    "innerHTML").strip()
        except Exception as e:
            print("Warning in getting jobLocation: ")
            jobLocation = ""
        try:
            jobWOrkPlace = self.driver.find_element(
                By.XPATH,
                "//span[contains(@class, 'workplace-type')]").get_attribute(
                    "innerHTML").strip()
        except Exception as e:
            print("Warning in getting jobWorkPlace: ")
            jobWOrkPlace = ""
        try:
            jobPostedDate = self.driver.find_element(
                By.XPATH,
                "//span[contains(@class, 'posted-date')]").get_attribute(
                    "innerHTML").strip()
        except Exception as e:
            print("Warning in getting jobPostedDate: ")
            jobPostedDate = ""
        try:
            jobApplications = self.driver.find_element(
                By.XPATH,
                "//span[contains(@class, 'applicant-count')]").get_attribute(
                    "innerHTML").strip()
        except Exception as e:
            print("Warning in getting jobApplications: ")
            jobApplications = ""

        textToWrite = str(
            count
        ) + " | " + jobTitle + " | " + jobCompany + " | " + jobLocation + " | " + jobWOrkPlace + " | " + jobPostedDate + " | " + jobApplications
        return textToWrite