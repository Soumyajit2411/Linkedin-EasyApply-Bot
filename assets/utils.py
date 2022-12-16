import math, constants, config
from typing import List
from selenium.webdriver.firefox.options import Options


def browserOptions():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("-profile")
    return options


def urlToKeywords(url: str) -> List[str]:
    keywordUrl = url[url.index("keywords=") + 9:]
    keyword = keywordUrl[0:keywordUrl.index("&")]
    locationUrl = url[url.index("location=") + 9:]
    location = locationUrl[0:locationUrl.index("&")]
    return [keyword, location]


def jobsToPages(numOfJobs: str):
    number_of_pages = 1
    if (' ' in numOfJobs):
        spaceIndex = numOfJobs.index(' ')
        totalJobs = (numOfJobs[0:spaceIndex])
        totalJobs_int = int(totalJobs.replace(',', ''))
        number_of_pages = math.ceil(totalJobs_int / constants.jobsPerPage)
        if (number_of_pages > 40):
            number_of_pages = 40
    return number_of_pages
