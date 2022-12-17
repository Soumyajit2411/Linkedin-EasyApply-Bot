import config
from selenium.webdriver.common.by import By


class LinkedinJobDetails:

    def getJobProperties(self, driver, count: str):
        textToWrite = ""
        jobTitle = ""
        jobCompany = ""
        jobLocation = ""
        jobWOrkPlace = ""
        jobPostedDate = ""
        jobApplication = ""

        try:
            jobTitle = driver.find_element(
                By.XPATH, "//h1[contains(@class, 'job-title')]").get_attribute(
                    "innerHTML").strip()
            res = [
                blItem for blItem in config.blackListTitles
                if (blItem.lower() in jobTitle.lower())
            ]
            if (len(res) > 0):
                jobTitle += "(blaclisted title)"
        except Exception as e:
            print("Warning in getting jobTitle: " + str(e)[0:50])
            jobTitle = ""

        try:
            jobCompany = driver.find_element(
                By.XPATH,
                "//a[contains(@class, 'ember-view t-black t-normal')]"
            ).get_attribute("innerHTML").strip()
            res = [
                blItem for blItem in config.blacklistCompanies
                if (blItem.lower() in jobTitle.lower())
            ]
            if (len(res) > 0):
                jobCompany += "(blaclisted company)"
        except Exception as e:
            print("Warning in getting jobCompany: ")
            jobCompany = ""

        try:
            jobLocation = driver.find_element(
                By.XPATH, "//span[contains(@class, 'bullet')]").get_attribute(
                    "innerHTML").strip()
            res = [
                blItem for blItem in config.blackListjobLocations
                if (blItem.lower() in jobLocation.lower())
            ]
            if (len(res) > 0):
                jobCompany += "(blaclisted location)"
        except Exception as e:
            print("Warning in getting jobLocation: ")
            jobLocation = ""
        try:
            jobWOrkPlace = driver.find_element(
                By.XPATH,
                "//span[contains(@class, 'workplace-type')]").get_attribute(
                    "innerHTML").strip()
        except Exception as e:
            print("Warning in getting jobWorkPlace: ")
            jobWOrkPlace = ""
        try:
            jobPostedDate = driver.find_element(
                By.XPATH,
                "//span[contains(@class, 'posted-date')]").get_attribute(
                    "innerHTML").strip()
        except Exception as e:
            print("Warning in getting jobPostedDate: ")
            jobPostedDate = ""
        try:
            jobApplications = driver.find_element(
                By.XPATH,
                "//span[contains(@class, 'applicant-count')]").get_attribute(
                    "innerHTML").strip()
            res = 0
            jobApplication = noofApplicant(jobApplications)
            if (int(jobApplication) < int(
                    config.blackListLimitjobApplications)):
                res += 1
            if (int(res) > 0):
                jobApplication += "(blaclisted applicant limit reached)"
        except Exception as e:
            print("Warning in getting jobApplications: ")
            jobApplication = ""

        textToWrite = str(count) + " | " + str(jobTitle) + " | " + str(
            jobCompany) + " | " + str(jobLocation) + " | " + str(
                jobWOrkPlace) + " | " + str(jobPostedDate) + " | " + str(
                    jobApplication)
        return textToWrite


def noofApplicant(numOfApplicants: str):
    if (' ' in numOfApplicants):
        spaceIndex = numOfApplicants.index(' ')
        applicants = (numOfApplicants[0:spaceIndex])
        jobApplication = int(applicants.replace(',', ''))
        return jobApplication