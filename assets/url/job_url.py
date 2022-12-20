class LinkedinJobUrlGenerate:

    def storeJobResults(self, lineToWrite: str):
        try:
            self.writeJobResults(lineToWrite)
        except Exception as e:
            print("Error in getting JobResults: " + str(e))

    def writeJobResults(self, text: str):
        fileName = "job_links.txt"
        try:
            with open("data/" + fileName, encoding="utf-8") as file:
                lines = []
                for line in file:
                    lines.append(line)
            with open("data/" + fileName, 'w', encoding="utf-8") as f:
                for line in lines:
                    f.write(line)
                f.write(text + "\n")

        except:
            with open("data/" + fileName, 'w', encoding="utf-8") as f:
                f.write(text + "\n")