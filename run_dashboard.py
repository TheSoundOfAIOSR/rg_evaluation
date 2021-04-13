import streamlit as st
import pandas as pd
import numpy as np
import json
from app.survey.surveydata import SurveyData
import pymysql

survey_data = SurveyData()

##### Deprecated: DBInterface Use" ####

#with open("dbConfig.json") as json_data_file:
#    DBParameters = json.load(json_data_file)
#    dict1 = DBParameters['sofai_evalDB']
#    hostName = dict1['hostname']
#    userName = dict1['username']
#    PWD = dict1['password']

#db = pymysql.connect(host=hostName, user=userName, password=PWD)
#cursor = db.cursor()
#cursor.execute('''show tables''')
#data = cursor.fetchall()

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.title("Sound of AI Survey Feedback Visualization")

df = pd.read_csv("./data.csv")

#@st.cache
#def load_data(nrows):
#    data = pd.read_csv(DATA_URL, nrows=nrows)
#    def lowercase(x): return str(x).lower()
#    data.rename(lowercase, axis='columns', inplace=True)
#    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#    return data
#data = load_data(10000)
print(df["Q0001"])

#st.bar_chart(df["q1"])
#st.bar_chart(df["q2"])
#st.bar_chart(df["q3"])
#st.bar_chart(df["q7"])
#st.bar_chart(df["q9"])
#st.bar_chart(df["q10"])

#row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.beta_columns(
#    (.1, 1, .1, 1, .1))

#with row3_1:
#    st.subheader(survey_data.question1['question'])
#    hist_values = np.histogram(
#        data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
#    st.bar_chart(hist_values)
#
#with row3_2:
#    st.subheader(survey_data.question2['question'])
#    hist_values = np.histogram(
#        data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
#    st.bar_chart(hist_values)

#row3_space1, row4_1, row4_space2, row4_2, row3_space3 = st.beta_columns(
#    (.1, 1, .1, 1, .1))

#with row4_1:
#    st.subheader(survey_data.question3['question'])
#    hist_values = np.histogram(
#        data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
#    st.bar_chart(hist_values)

#with row4_2:
#    st.subheader(survey_data.question4['question'])
#    hist_values = np.histogram(
#        data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
#    st.bar_chart(hist_values)

st.text("")
st.markdown("[Insert Survey String Responses]")