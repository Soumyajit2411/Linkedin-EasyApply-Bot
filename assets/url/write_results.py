class LinkedinWriteResults:

    def displayWriteResults(self, lineToWrite: str):
        try:
            print(lineToWrite)
            self.writeResults(lineToWrite)
        except Exception as e:
            print("Error in DisplayWriteResults: " + str(e))

    def writeResults(self, text: str):
        fileName = "applied_job_data.txt"
        try:
            with open("downloads/" + fileName, encoding="utf-8") as file:
                lines = []
                for line in file:
                    if "----" not in line:
                        lines.append(line)

            with open("downloads/" + fileName, 'w', encoding="utf-8") as f:
                f.write("---- Applied Jobs Data ----" + "\n")
                f.write(
                    "---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result ----"
                    + "\n")
                for line in lines:
                    f.write(line)
                f.write(text + "\n")

        except:
            with open("downloads/" + fileName, 'w', encoding="utf-8") as f:
                f.write("---- Applied Jobs Data ----" + "\n")
                f.write(
                    "---- Number | Job Title | Company | Location | Work Place | Posted Date | Applications | Result ----"
                    + "\n")
                f.write(text + "\n")

    def getUrlDataFile(self):
        urlData = ""
        try:
            file = open('downloads/urlData.txt', 'r')
            urlData = file.readlines()
        except FileNotFoundError:
            pass
        return urlData
