# -*- coding: utf-8 -*-
import pymysql

# DB Connection
def Connection():

    db_information = []
    # Read DB information File
    DB_Connection_File = open('Connection.ini', 'r')
    
    for x in file:
    # DB crop the ("/n")
        db_information.append(x.rstrip())
    # put inforamtion varibles
    # check information (list > tuple)
    conn = pymysql.connect(
    host = db_information[0],
    port = int(db_information[1]),
    user = db_information[2],
    passwd = db_information[3],
    db = db_information[4],
    charset= db_information[5]
    )

    return conn