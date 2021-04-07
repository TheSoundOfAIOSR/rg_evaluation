# Modified by Balaji - 9/3/2021
# DB operations added
# Creation script is commented out here. But was run separately once


# Access AWS with Python 3
# DB Parameters moved to dbConfig.json :: Balaji 24/3/2021

from datetime import datetime

from app.config import Config
from app.survey.surveydata import SurveyData
import pymysql


class DBInterface:

    # global database variables. Access these in code segments either
    # as self.db, self.cursor, etc,  OR as  DBInterface.db, DBInterface.cursor, etc.
    DATABASE_NAME = "SofAISurvey"
    config = Config.load_config()

    def connect(self):
        self.db = pymysql.connect(
            host=self.config["hostname"],
            user=self.config["username"],
            password=self.config["password"],
        )
        self.cursor = self.db.cursor()

    def createMainTable(self):
        """Creates the main table for the database.

        The table will store entries like this:
        Responder       Q1         Q2     Q3
        Person1          5          2     “I love it”
        Person2          4          1     “it’s great”
        """

        self.cursor.execute(f"USE {self.DATABASE_NAME}")
        self.cursor.execute(
            "CREATE TABLE survey (responder INT NOT NULL AUTO_INCREMENT PRIMARY KEY)"
        )
        self.cursor.execute("SHOW COLUMNS FROM survey")
        print(self.cursor.fetchall())
        # db.commit()

    def writeToCsv(self, csv_file, form) -> None:
        """
        Appends the given survey result to the given csv file.

        csv_file
            string, path to the csv file.form
        dictionary,
            intended to be survey results coming out of flask.request.form.
        """
        responses = []
        for question_number in range(1, SurveyData.count + 1):
            if "q" + str(question_number) in form:
                responses.append(form["q" + str(question_number)])
            else:
                # if someone doesn't respond to a question, this will make sure it
                # gets recorded as a NaN
                responses.append("")

        current_date = datetime.now().strftime("%Y-%m-%d-%H-%M")
        responses.append(current_date)

        # write all responses to the textfile separated by commas
        with open(csv_file, "a") as fp:
            fp.write(",".join(responses))
            fp.write("\n")

    def writeToDB(self, RespUser, RespType, RespInt, RespText, RespDate):

        # get the sql version of the database
        self.cursor.execute("select version()")
        sql_version = self.cursor.fetchone()

        print("SQL Version: {}".format(sql_version))

        # gets the tables. This was empty until a table was created.
        self.cursor.execute("""use {}""".format(self.DATABASE_NAME))
        self.cursor.execute("""show tables""")
        all_tables = self.cursor.fetchall()
        print(
            "Tables within the {} database: {}".format(self.DATABASE_NAME, all_tables)
        )

        # db.commit()

        # add a question with the label "1" to the table named survey1
        table_name = "survey2"
        columns = "(Responder, ResponseType, ResponseInt, ResponseText, ResponseDate)"
        values = tuple(map(str, (RespUser, RespType, RespInt, RespText, RespDate)))
        insert_query = f"INSERT INTO {table_name} {columns} VALUES  {values}"
        print("INSERT QUERY", insert_query)
        self.cursor.execute(insert_query)
        # self.db.commit()

        # Clean up the table
        # cursor.execute("DELETE FROM survey2")
        # db.commit()

        select_all_query = "SELECT * FROM survey2"
        self.cursor.execute(select_all_query)
        data = self.cursor.fetchall()
        print("Output on 25th March:", data)


"""
if you don't commit after running SQL queries,
the database on the AWS server doesn't update.
only uncomment next line if you want to push changes
"""
# db.commit()
