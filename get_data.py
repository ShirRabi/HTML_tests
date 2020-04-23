
import export_elements
import pyodbc
import sys
from parameters import SERVER
from parameters import db
from parameters import driver
from parameters import Original_url
from parameters import table

def get_data():

    # output: list of  (repitition of the elements,HTML elements from table)
    try:
        #connecting SQL server
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+SERVER+';DATABASE='+db)
        cnxn.autocommit = True
        cursor = cnxn.cursor()

        #get data from db
        cursor.execute("SELECT * from "+ table)
        data=cursor.fetchall()
        assert data, "table is empty" #no saved elements in db
        return data

    #problems with connection
    except pyodbc.Error as e:
        print(e)
        sys.exit()

