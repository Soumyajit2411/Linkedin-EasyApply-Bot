from dotenv import dotenv_values

config = dotenv_values(".env")
browser = ["chrome"]
email = config['USERNAME']
password = config['PASSWORD']
chromeProfilePath = r""

location = []
keywords = ["frontend", "java", "python", "ruby"]
experienceLevels = ["Entry level", "Internship"]
datePosted = ["Past month"]
jobType = ["Part-time", "Internship", "Temporary"]
remote = ["Remote"]
salary = []
sort = ["Recent"]
blacklistCompanies = []
blackListTitles = []
blackListjobLocations = []
blackListLimitjobApplications = 200
followCompanies = True
alert = False
workAuthorization = "Yes"
defaultInput = "1"
defaultCheck = "Yes"
defaultRadio = "Yes"