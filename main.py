"""
Modified by Balaji - 9/3/2021
DB operations added
"""

from flask import Flask, render_template, request
from surveydata import SurveyData
from sofaidb import DBInterface
from datetime import datetime
import os

app = Flask(__name__)
survey_data = SurveyData()
filename = 'data.txt'  # This can be removed later


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
    RspType = -1
    rating = request.form['q1']

    if rating:  # equivalent of is None
        out = open(filename, 'a')
        out.write(rating + '\n')
        out.close()

        RspType = 1  # set it for radio button if at least one radio button is present in the questionnaire
        # Write ResponseInt <-- rating

    response = request.form['q5']
    if response:
        if RspType == -1:
            # set it for text input. As of now, this field and Responder filed are one and the same.
            RspType = 2
            # Write ResponseText <-- response
            # Write Responder <-- response
            # Write ResponseType <-- RspType

    CurrDate = datetime.now()
    # Write ResponseDate <-- CurrDate
    CurrDate = CurrDate.strftime("%Y-%m-%d")
    DBInterface.writeToDB(RespUser='dummyUser', RespType=1, RespInt=int(
        rating), RespText=response, RespDate=CurrDate)

    return render_template('thankyou.html', data=survey_data, ans=request.form)


@app.route('/results')
def show_results():
    """
    Show results of survey
    :return:
    """
    responses = {}
    for f in survey_data.data['fields']:
        responses[f] = 0

    f = open(filename, 'r')
    for line in f:
        response = line.rstrip("\n")
        responses[response] += 1

    return render_template('results.html', data=survey_data.data, votes=responses)


if __name__ == "__main__":
    app.run(debug=True)
