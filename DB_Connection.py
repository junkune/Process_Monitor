# -*- coding: utf-8 -*-
import pymysql

def Connection_DB():

    db_information = []
        
    DB_Connection_File = open('Connection.ini', 'r')

    for x in file:
        db_information.append(x.rstrip())
       
    conn = pymysql.connect(
    host = db_information[0],
    port = int(db_information[1]),
    user = db_information[2],
    passwd = db_information[3],
    db = db_information[4],
    charset= db_information[5]
    )

    return conn