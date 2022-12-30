from dotenv import dotenv_values

config = dotenv_values(".env")
browser = ["firefox"]
email = config['USERNAME']
password = config['PASSWORD']
chromeProfilePath = r""

location = ["India"]
keywords = [
    "backend", "react", "software", "javascript", "java", "python",
    "programming", "rpa"
]
experienceLevels = ["Entry level", "Internship"]
datePosted = ["Past month"]
jobType = ["Part-time", "Internship", "Temporary"]
remote = ["Remote", "Hybrid"]
salary = ["$40,000+"]
sort = ["Recent"]
blacklistCompanies = []
blackListTitles = []
blackListjobLocations = []
blackListLimitjobApplications = 10
followCompanies = False
alert = False
workAuthorization = "No"
defaultInput = "1"
defaultCheck = "1"
defaultRadio = "Yes"