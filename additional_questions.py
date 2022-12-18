import yaml


class LinkedinAdditionalQuestions:

    def checkboxConfig(self):
        try:
            with open('additional_questions\check.yaml') as check:
                data = yaml.load(check, Loader=yaml.FullLoader)
        except Exception as e:
            print("Error in Parsing yaml : " + str(e))
        return data

    def inputFieldConfig(self):
        try:
            with open('additional_questions\input.yaml') as input:
                data = yaml.load(input, Loader=yaml.FullLoader)
        except Exception as e:
            print("Error in Parsing yaml : " + str(e))
        return data


LinkedinAdditionalQuestions().checkboxConfig()
# LinkedinAdditionalQuestions().inputFieldConfig()