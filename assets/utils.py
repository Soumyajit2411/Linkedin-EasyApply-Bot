import math, constants
from typing import List


def urlToKeywords(url: str) -> List[str]:
    keywordUrl = url[url.index("keywords=") + 9:]
    keyword = keywordUrl[0:keywordUrl.index("&")]
    if "location" in url:
        locationUrl = url[url.index("location=") + 9:]
        location = locationUrl[0:locationUrl.index("&")]
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
    return "browser = '" + request.get(
        'Browser') + "'\n" + "email = '" + request.get(
            'Email') + "'\n" + "password = '" + request.get(
                'Password') + "'\n" + "keywords = '" + request.get(
                    'keywords'
                ) + "'\n" + "blacklistCompanies = '" + request.get(
                    'blacklistCompanies'
                ) + "'\n" + "blackListTitles = '" + request.get(
                    'blackListTitles'
                ) + "'\n" + "blackListjobLocations = '" + request.get(
                    'blackListjobLocations'
                ) + "'\n" + "blackListLimitjobApplications = '" + request.get(
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
                            request.getlist('location')
                        ) + "\n" + "experienceLevels = " + str(
                            request.getlist('experienceLevels')
                        ) + "\n" + "datePosted = " + str(
                            request.getlist('datePosted')
                        ) + "\n" + "jobType = " + str(
                            request.getlist('jobType')
                        ) + "\n" + "remote = " + str(request.getlist(
                            'remote')) + "\n" + "salary = " + str(
                                request.getlist(
                                    'salary')) + "\n" + "sort = " + str(
                                        request.getlist('sort')) + "\n"
