import constants, config,os

class LinkedinUrlGenerate:

    def generateUrls(self):
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
        try:
            with open('downloads/urlData.txt', 'w', encoding="utf-8") as file:
                linkedinJobLinks = self.generateUrlLinks()
                for url in linkedinJobLinks:
                    file.write(url + "\n")
        except:
            print("No Url Found!")

    def generateUrlLinks(self):
        path = []
        if not config.location:
            for keyword in config.keywords:
                url = constants.linkJobUrl + "?f_AL=true&keywords=" +keyword
                if config.jobType != []:
                    url+=self.jobType()
                if config.remote != []:
                    url+=self.remote()
                if config.experienceLevels != []:
                    url+=self.jobExp()
                if config.datePosted != []:
                    url+=self.datePosted()
                if config.salary != []:
                    url+=self.salary()
                if config.sort != []:
                    url+=self.sortBy()
                path.append(url)
        else:
            for location in config.location:
                for keyword in config.keywords:
                    url = constants.linkJobUrl + "?f_AL=true&keywords=" +keyword
                    if config.jobType != []:
                        url+=self.jobType()
                    if config.remote != []:
                        url+=self.remote()
                    if config.location != 0:
                        url+=self.checkJobLocation(location)
                    if config.experienceLevels != []:
                        url+=self.jobExp()
                    if config.datePosted != []:
                        url+=self.datePosted()
                    if config.salary != []:
                        url+=self.salary()
                    if config.sort != []:
                        url+=self.sortBy()
                    path.append(url)
        return path

    def checkJobLocation(self,job):
        jobLoc = "&location=" +job
        match job.casefold():
            case "asia":
                jobLoc += "&geoId=102393603"
            case "europe":
                jobLoc += "&geoId=100506914"
            case "northamerica":
                jobLoc += "&geoId=102221843&"
            case "southamerica":
                jobLoc +=  "&geoId=104514572"
            case "australia":
                jobLoc +=  "&geoId=101452733"
            case "africa":
                jobLoc += "&geoId=103537801"

        return jobLoc

    def jobExp(self):
        jobtExpArray = config.experienceLevels
        firstJobExp = jobtExpArray[0]
        jobExp = ""
        match firstJobExp:
            case "Internship":
                jobExp = "&f_E=1"
            case "Entry level":
                jobExp = "&f_E=2"
            case "Associate":
                jobExp = "&f_E=3"
            case "Mid-Senior level":
                jobExp = "&f_E=4"
            case "Director":
                jobExp = "&f_E=5"
            case "Executive":
                jobExp = "&f_E=6"
        for index in range (1,len(jobtExpArray)):
            match jobtExpArray[index]:
                case "Internship":
                    jobExp += "%2C1"
                case "Entry level":
                    jobExp +="%2C2"
                case "Associate":
                    jobExp +="%2C3"
                case "Mid-Senior level":
                    jobExp += "%2C4"
                case "Director":
                    jobExp += "%2C5"
                case "Executive":
                    jobExp  +="%2C6"

        return jobExp

    def datePosted(self):
        datePosted = ""
        match config.datePosted[0]:
            case "Any Time":
                datePosted = ""
            case "Past Month":
                datePosted = "&f_TPR=r2592000&"
            case "Past Week":
                datePosted = "&f_TPR=r604800&"
            case "Past 24 hours":
                datePosted = "&f_TPR=r86400&"
        return datePosted

    def jobType(self):
        jobTypeArray = config.jobType
        firstjobType = jobTypeArray[0]
        jobType = ""
        match firstjobType:
            case "Full-time":
                jobType = "&f_JT=F"
            case "Part-time":
                jobType = "&f_JT=P"
            case "Contract":
                jobType = "&f_JT=C"
            case "Temporary":
                jobType = "&f_JT=T"
            case "Volunteer":
                jobType = "&f_JT=V"
            case "Intership":
                jobType = "&f_JT=I"
            case "Other":
                jobType = "&f_JT=O"
        for index in range (1,len(jobTypeArray)):
            match jobTypeArray[index]:
                case "Full-time":
                    jobType += "%2CF"
                case "Part-time":
                    jobType +="%2CP"
                case "Contract":
                    jobType +="%2CC"
                case "Temporary":
                    jobType += "%2CT"
                case "Volunteer":
                    jobType += "%2CV"
                case "Intership":
                    jobType  +="%2CI"
                case "Other":
                    jobType  +="%2CO"
        jobType += "&"
        return jobType

    def remote(self):
        remoteArray = config.remote
        firstJobRemote = remoteArray[0]
        jobRemote = ""
        match firstJobRemote:
            case "On-site":
                jobRemote = "f_WT=1"
            case "Remote":
                jobRemote = "f_WT=2"
            case "Hybrid":
                jobRemote = "f_WT=3"
        for index in range (1,len(remoteArray)):
            match remoteArray[index]:
                case "On-site":
                    jobRemote += "%2C1"
                case "Remote":
                    jobRemote += "%2C2"
                case "Hybrid":
                    jobRemote += "%2C3"

        return jobRemote

    def salary(self):
        salary = ""
        match config.salary[0]:
            case "$40,000+":
                salary = "f_SB2=1&"
            case "$60,000+":
                salary = "f_SB2=2&"
            case "$80,000+":
                salary = "f_SB2=3&"
            case "$100,000+":
                salary = "f_SB2=4&"
            case "$120,000+":
                salary = "f_SB2=5&"
            case "$140,000+":
                salary = "f_SB2=6&"
            case "$160,000+":
                salary = "f_SB2=7&"    
            case "$180,000+":
                salary = "f_SB2=8&"    
            case "$200,000+":
                salary = "f_SB2=9&"                  
        return salary

    def sortBy(self):
        sortBy = ""
        match config.sort[0]:
            case "Recent":
                sortBy = "sortBy=DD"
            case "Relevent":
                sortBy = "sortBy=R"                
        return sortBy