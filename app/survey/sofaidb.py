# Modified by Balaji - 9/3/2021
# DB operations added
# Creation script is commented out here. But was run separately once


# Access AWS with Python 3
# DB Parameters moved to dbConfig.json :: Balaji 24/3/2021

from datetime import datetime

from app.config import load_config
from app.constants import NUM_QUESTIONS
# from app.survey.surveydata import SurveyData
from app.survey.loadSurveyData import loadSurveyData
import pymysql


class DBInterface:

    # global database variables. Access these in code segments either
    # as cls.db, cls.cursor, etc,  OR as  DBInterface.db, DBInterface.cursor, etc.
    DATABASE_NAME = "SofAISurvey"
    config = load_config()
    # db = pymysql.connect(
    #     host=config['hostname'],
    #     user=config['username'],
    #     password=config['password'])
    # cursor = db.cursor()

    @classmethod
    def createMainTable(cls):
        """Creates the main table for the database.

        The table will store entries like this:
        Responder       Q1         Q2     Q3
        Person1          5          2     “I love it”
        Person2          4          1     “it’s great” 
        """

        cls.cursor.execute("USE {}".format(cls.DATABASE_NAME))
        cls.cursor.execute("""
                        CREATE TABLE survey (responder INT NOT NULL AUTO_INCREMENT PRIMARY KEY)
                        """)
        cls.cursor.execute("SHOW COLUMNS FROM survey")
        print(cls.cursor.fetchall())
        # db.commit()

    @classmethod
    def writeToCsv(cls, csv_file, form) -> None:
        """
        Appends the given survey result to the given csv file.

        ARGS:
            - csv_file - string, path to the csv file.
            - form - dictionary, intended to be survey results coming out of flask.request.form.
        """
        responses = []
        survey_data = loadSurveyData()

        current_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
        responses.append(current_date)

        for key, item in survey_data.items():
            for question in item:
                try: 
                    userResponse = form[question['attribute']['identifier']]
                except:
                    userResponse = ""
                finally:
                    responses.append(userResponse)

        # write all responses to the textfile separated by commas
        with open(csv_file, "a") as fp:
            fp.write(','.join(responses))
            fp.write('\n')

    @classmethod
    def writeToDB(cls, RespUser, RespType, RespInt, RespText, RespDate):

        # get the sql version of the database
        cls.cursor.execute("select version()")
        sql_version = cls.cursor.fetchone()

        print("SQL Version: {}".format(sql_version))

        # gets the tables. This was empty until a table was created.
        cls.cursor.execute("""use {}""".format(cls.DATABASE_NAME))
        cls.cursor.execute("""show tables""")
        all_tables = cls.cursor.fetchall()
        print("Tables within the {} database: {}".format(
            cls.DATABASE_NAME, all_tables))

        # db.commit()

        # add a question with the label "1" to the table named survey1
        insert_query = "INSERT INTO survey2 (Responder, ResponseType, ResponseInt, ResponseText, ResponseDate) \
                                   VALUES  (%s,%s,%s,%s,%s)"  # , (RespUser, RespType, RespInt, RespText, RespDate)
        cls.cursor.execute(insert_query, (RespUser, RespType,
                                          RespInt, RespText, RespDate))
        # cls.db.commit()

        # Clean up the table
        #cursor.execute("DELETE FROM survey2")
        # db.commit()

        select_all_query = "SELECT * FROM survey2"
        cls.cursor.execute(select_all_query)
        data = cls.cursor.fetchall()
        print('Output on 25th March:', data)


# if you don't commit after running SQL queries, the database on the AWS server doesn't update.
# only uncomment next line if you want to push changes.
# db.commit()
