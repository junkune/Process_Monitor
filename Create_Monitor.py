# -*- coding: utf-8 -*-
import pymysql
import csv
import DB_Connection

#db_conneection#
def download_graph():
    conn = DB_Connection.Connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM monitor;"
    cursor.execute(query)
    result = cursor.fetchall()

    file = open('test.csv', 'w', encoding='utf-8', newline='')
    csv_wr = csv.writer(file)

    for row in result:
        csv_wr.writerow(row)

    file.close()