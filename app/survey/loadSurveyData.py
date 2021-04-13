# Return parsed YAML of surveydata
# throws YAMLError

import yaml
def loadSurveyData():
    with open("app/survey/surveydata.yaml", 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            raise exc