from dotenv import dotenv_values

config = dotenv_values(".env")
browser = ["firefox"]
email = config['USERNAME']
password = config['PASSWORD']
chromeProfilePath = r""

location = ["India"]
keywords = ["web development", "java", "python", "react"]
experienceLevels = ["Entry level", "Internship"]
datePosted = ["Past month"]
jobType = ["Part-time", "Internship", "Temporary"]
remote = ["Remote"]
salary = ["$40,000+"]
sort = ["Recent"]
blacklistCompanies = []
blackListTitles = []
blackListjobLocations = []
blackListLimitjobApplications = 10
followCompanies = True
alert = False
workAuthorization = "Yes"
defaultInput = "1"
defaultCheck = "Yes"
defaultRadio = "Yes"