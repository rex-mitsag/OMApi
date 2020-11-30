import pyodbc
from pandas import read_sql_query as pd
import os

##Connection String
#str(os.getenv('SQLAZURECONNSTR_WWIF'))
#'Driver={ODBC Driver 17 for SQL Server};Server=tcp:qeplsqlcloud.database.windows.net,1433;Database=quickeats;Uid=qepladmin;Pwd=$Puneet@123;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
driver = 'Driver={ODBC Driver 17 for SQL Server};''Server=tcp:qeplsqlcloud.database.windows.net,1433;''Database=quickeats;''Uid=qepladmin@qeplsqlcloud;Pwd=$Puneet@123;''Encrypt=yes;'
#
#
##

def checkconn() :
    try :
        conn = pyodbc.connect(driver)
        return 'working'
    except :
        return 'error'

def updatedata(query) :
    conn = pyodbc.connect(driver)
    cursor = conn.cursor()
    try :
        cursor.execute(query)
        msg = '1'
    except :
        msg = '0'
    conn.commit()
    conn.close()
    return msg

def getlistdata(query) :
    conn = pyodbc.connect(driver)
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

def getdata(query) :
    conn = pyodbc.connect(driver)
    try :
        data = pd(query, conn)
    except :
        data = None
    conn.commit()
    conn.close()
    return data