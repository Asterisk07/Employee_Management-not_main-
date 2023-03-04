import sqlite3
import sys
conn = sqlite3.connect('empl.db')
cur=conn.cursor()

try:
    # use lstrip on all variables after extracting them from table since they will have whitespace at leftdef 

    q="create table data{} (name char(20),password char(10) ,email char(40),mobile char(10));"
    conn.execute(q)
    
except sqlite3.OperationalError :
    print(sys.exc_info()[1])
    pass

conn.close()
