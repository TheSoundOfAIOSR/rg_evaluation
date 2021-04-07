# rg_evaluation
Research Group - Evaluation

[![Python application](https://github.com/TheSoundOfAIOSR/rg_evaluation/actions/workflows/python-app.yml/badge.svg)](https://github.com/TheSoundOfAIOSR/rg_evaluation/actions/workflows/python-app.yml)

## Flask App for the survey:

> `run.py` handles the Python survey app (written in Flask) 

## Streamlit App

> `streamlit run dashboard.py` runs the streamlit app

## PyMySQL rundown

The two main objects you want to work with in PyMySQL are 1) the database connection object (which is `db` in the script) and 2) the `cursor` object. A typical workflow looks like this:

    # set up the database connection 
    db = pymysql.connect(...database info...)

    # pull out the cursor from the connection (only need to do this once like this)
    cursor = db.cursor()

    # write a sql query as a python string
    query = """SELECT * FROM table"""

    # tell the cursor to execute the query
    cursor.execute(query)

    # grab the results of the query and store it in
    # a python object that I called "data"
    data = cursor.fetchall()

    # do what you want with data, like print it.
    print(data)


Optionally, if you want to make changes to the database, the workflow is similar, but you need to commit the changes:

    # sql query to do some stuff
    query = """ INSERT INTO table VALUES (blah blah blah)"""

    # execute the query (this alters the local model of the database)
    cursor.execute(query)

    # send the changes to the cloud on AWS
    db.commit()
