# Access AWS with Python 3

# db: sofai-mysql
# username: admin 
# password: soundofai
# port: 3306
# hostname: sofai-mysql.cbyywm0dtzft.us-east-2.rds.amazonaws.com

import pymysql

db = pymysql.connect(host= 'sofai-mysql.cbyywm0dtzft.us-east-2.rds.amazonaws.com', 
        user='admin', password='soundofai')

cursor = db.cursor()

print(cursor)

cursor.execute("select version()")
data = cursor.fetchone()

print(data)

# Initially Create Table
# sql = '''create database SofAISurvey'''
# cursor.execute(sql)

cursor.execute('''use SofAISurvey''')
cursor.execute('''show tables''')
cursor.fetchall()

