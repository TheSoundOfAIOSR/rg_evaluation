# Access AWS with Python 3

# db: sofai-mysql
# username: admin
# password: soundofai
# port: 3306
# hostname: sofai-mysql.cbyywm0dtzft.us-east-2.rds.amazonaws.com

import pymysql

db = pymysql.connect(host='sofai-mysql.cbyywm0dtzft.us-east-2.rds.amazonaws.com',
                     user='admin', password='soundofai')

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
print(data)

# create a table. Only uncomment this if you want to create the table again!!!
# cursor.execute('''CREATE TABLE survey1 (question INT)''')

# add a question with the label "1" to the table named survey1
# insert_query = """
#         INSERT INTO survey1
#         VALUES (17)
#         """
# cursor.execute(insert_query)

select_all_query = """
                SELECT * FROM survey1
                """
cursor.execute(select_all_query)
data = cursor.fetchall()
print(data)


# if you don't commit after running SQL queries, the database on the AWS server doesn't update.
# only uncomment next line if you want to push changes.
# db.commit()
