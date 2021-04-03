# Modified by Balaji - 9/3/2021
# DB operations added
# Creation script is commented out here. But was run separately once


# Access AWS with Python 3
# DB Parameters moved to dbConfig.json :: Balaji 24/3/2021

from app.config import load_config
import json
import pymysql


class DBInterface:

    config = load_config()

    def writeToDB(RespUser, RespType, RespInt, RespText, RespDate):
        db = pymysql.connect(
            host=DBInterface.config['hostname'],
            user=DBInterface.config['username'],
            password=DBInterface.config['password'])
        cursor = db.cursor()

        # this is just a python object; just prints the location of the object in your memory
        print(cursor)

        # get the sql version of the database
        cursor.execute("select version()")
        data = cursor.fetchone()
        print(data)

        # Initially create the database; only run once
        # sql = '''create database SofAISurvey'''
        # cursor.execute(sql)

        # gets the tables. This was empty until a table was created.
        cursor.execute('''use SofAISurvey''')
        cursor.execute('''show tables''')
        data = cursor.fetchall()
        # print(data)

        # create a table. Only uncomment this if you want to create the table again!!!
        # Primary key missing - add after discussions
        # cursor.execute('''CREATE TABLE survey2 (questionNo int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        # 					Responder varchar(40) NOT NULL,
        # 					ResponseType int,	#1 - for radio btn, 2 - for text, ...
        # 					ResponseInt int,
        # 					ResponseText varchar(40),
        # 					ResponseDate	DATE )''')

        # db.commit()

        # add a question with the label "1" to the table named survey1
        insert_query = "INSERT INTO survey2 (Responder, ResponseType, ResponseInt, ResponseText, ResponseDate) \
                                   VALUES  (%s,%s,%s,%s,%s)"  # , (RespUser, RespType, RespInt, RespText, RespDate)
        cursor.execute(insert_query, (RespUser, RespType,
                                      RespInt, RespText, RespDate))
        db.commit()

        # Clean up the table
        #cursor.execute("DELETE FROM survey2")
        # db.commit()

        select_all_query = "SELECT * FROM survey2"
        cursor.execute(select_all_query)
        data = cursor.fetchall()
        print('Output on 25th March:', data)


# if you don't commit after running SQL queries, the database on the AWS server doesn't update.
# only uncomment next line if you want to push changes.
# db.commit()
