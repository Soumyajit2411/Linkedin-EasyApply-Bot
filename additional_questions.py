import yaml


class LinkedinAdditionalQuestions:

    def checkboxConfigData(self):
        try:
            with open('additional_questions\check.yaml') as check:
                data = yaml.load(check, Loader=yaml.FullLoader)
        except Exception as e:
            print("Error in Parsing yaml : " + str(e))
        return data

    def inputFieldConfigData(self):
        try:
            with open('additional_questions\input.yaml') as input:
                data = yaml.load(input, Loader=yaml.FullLoader)
        except Exception as e:
            print("Error in Parsing yaml : " + str(e))
        return data

    def radioConfigData(self):
        try:
            with open('additional_questions\\radio.yaml') as input:
                data = yaml.load(input, Loader=yaml.FullLoader)
        except Exception as e:
            print("Error in Parsing yaml : " + str(e))
        return data


LinkedinAdditionalQuestions().radioConfigData()