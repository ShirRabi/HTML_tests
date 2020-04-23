from export_elements import export_elements
import pyodbc

from parameters import SERVER
from parameters import db
from parameters import driver
from parameters import Original_url
from parameters import table
#connecting SQL server
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+SERVER+';DATABASE='+db)
cnxn.autocommit = True
cursor = cnxn.cursor()

#get wanted columns
unique,tag_times=export_elements()

#upload db
cursor.execute("DROP TABLE "+table)
cursor.execute("CREATE TABLE "+table+"(repititions int, element_name CHAR(255));")
for i in range(0,len(tag_times),1):
    times=str(tag_times[i])
    element=str(unique[i])
    cursor.execute("INSERT INTO ynet_broadcasts_elements(repititions,element_name) VALUES("+times+",'"+element+"');")
