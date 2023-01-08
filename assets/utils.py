import math, constants
from typing import List


def urlToKeywords(url: str) -> List[str]:
    keywordUrl = url[url.index("keywords=") + 9:]
    if "&" in keywordUrl:
        keyword = keywordUrl[0:keywordUrl.index("&")]
    else:
        keyword = keywordUrl[0:keywordUrl.index("\n")]
    if "location" in url:
        locationUrl = url[url.index("location=") + 9:]
        if "&" in locationUrl:
            location = locationUrl[0:locationUrl.index("&")]
        else:
            location = locationUrl[0:locationUrl.index("\n")]
    else:
        location = "Default"
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


def configs(request):
    keywords = stringToKeywords(request.get('keywords'))
    location = stringToKeywords(request.get('location'))
    blacklistCompanies = stringToKeywords(request.get('blacklistCompanies'))
    blackListTitles = stringToKeywords(request.get('blackListTitles'))
    blackListjobLocations = stringToKeywords(
        request.get('blackListjobLocations'))
    return "browser = '" + request.get(
        'Browser') + "'\n" + "email = '" + request.get(
            'Email') + "'\n" + "password = '" + request.get(
                'Password') + "'\n" + "keywords = " + str(
                    keywords
                ) + "\n" + "blacklistCompanies = " + str(
                    blacklistCompanies
                ) + "\n" + "blackListTitles = " + str(
                    blackListTitles
                ) + "\n" + "blackListjobLocations = " + str(
                    blackListjobLocations
                ) + "\n" + "blackListLimitjobApplications = '" + request.get(
                    'blackListLimitjobApplications'
                ) + "'\n" + "followCompanies = '" + request.get(
                    'followCompanies') + "'\n" + "alert = '" + request.get(
                        'alert'
                    ) + "'\n" + "workAuthorization = '" + request.get(
                        'workAuthorization'
                    ) + "'\n" + "defaultInput = '" + request.get(
                        'defaultInput'
                    ) + "'\n" + "defaultCheck = '" + request.get(
                        'defaultCheck'
                    ) + "'\n" + "defaultRadio = '" + request.get(
                        'defaultRadio') + "'\n" + "location = " + str(
                            location) + "\n" + "experienceLevels = " + str(
                                request.getlist('experienceLevels')
                            ) + "\n" + "datePosted = " + str(
                                request.getlist(
                                    'datePosted')) + "\n" + "jobType = " + str(
                                        request.getlist('jobType')
                                    ) + "\n" + "remote = " + str(
                                        request.getlist('remote')
                                    ) + "\n" + "salary = " + str(
                                        request.getlist('salary')
                                    ) + "\n" + "sort = " + str(
                                        request.getlist('sort')) + "\n"


def stringToKeywords(url: str) -> List[str]:
    if len(url) == 0:
        return []
    x = url.split(",")
    return x