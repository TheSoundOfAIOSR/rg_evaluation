from flask import Flask, render_template, request
from surveydata import SurveyData
import os

app = Flask(__name__)
survey_data = SurveyData()
filename = 'data.txt'

@app.route('/')
def root():
    """
    Run app
    :return:
    """
    return render_template("survey.html", data = survey_data.data)

@app.route('/responsedata')
def surveyresponse():
    """
    Handle Survey Response
    :return:
    """
    response = request.args.get('field')

    out = open(filename, 'a')
    out.write(response + '\n')
    out.close()
    return render_template('thankyou.html', data=survey_data.data)

@app.route('/results')
def show_results():
    """
    Show results of survey
    :return:
    """
    responses = {}
    for f in survey_data.data['fields']:
        responses[f] = 0

    f  = open(filename, 'r')
    for line in f:
        response = line.rstrip("\n")
        responses[response] += 1

    return render_template('results.html', data=survey_data.data, votes=responses)

if __name__ == "__main__":
    app.run()


