from pprint import pprint
from datetime import datetime

from flask import Flask, render_template, request

# from app.survey.surveydata import SurveyData
from app.survey.sofaidb import DBInterface
# from app.constants import NUM_QUESTIONS
from app.survey.loadSurveyData import loadSurveyData

app = Flask(__name__)
survey_data = loadSurveyData()
csv_file = 'data.csv'
text_file = 'data.txt'

@app.route('/')
def root():
    """
    Run app
    :return:
    """
    return render_template("survey.html", data=survey_data)

@app.route('/responsedata', methods=['POST'])
def surveyresponse():
    """
    Handle Survey Response
    :return:
    """
    # old code - only being kept to pass tests.
    # we should aim to get this generalized and into
    # DBInterface.writeToDB
    #RspType = -1

    #rating = request.form['q1']
    #if rating:
    #    out = open(text_file, 'a')
    #    out.write(rating + '\n')
    #    out.close()

    #RspType = 1  # set it for radio button if at least one radio button is present in the questionnaire
    # Write ResponseInt <-- rating

    #response = request.form['q5']
    #if response:
    #    if RspType == -1:
            # set it for text input. As of now, this field and Responder filed are one and the same.
    #        RspType = 2
            # Write ResponseText <-- response
            # Write Responder <-- response
            # Write ResponseType <-- RspType

    # Write to the database
    # TODO: Backend Fix!
    #DBInterface.writeToDB(RespUser='dummyUser', RespType=1, RespInt=int(
    #    rating), RespText=response, RespDate=datetime.now())
    #############
    #############
    # End old code

    # writes the files to the local csv file for backup
    DBInterface.writeToCsv(csv_file, request.form)

    return render_template('thankyou_simple.html')

@app.route('/results')
def show_results():
    """
    Show results of survey
    :return:
    """
    responses = {}
    for f in survey_data.data['fields']:
        responses[f] = 0

    f = open(csv_file, 'r')
    for line in f:
        response = line.rstrip("\n")
        responses[response] += 1

    return render_template('results.html', data=survey_data.data, votes=responses)
