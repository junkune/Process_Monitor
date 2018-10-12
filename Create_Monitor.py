# -*- coding: utf-8 -*-
import pymysql
import csv
from pip._vendor.distlib._backport.tarfile import grp
import graph

conn = pymysql.connect(
    host = 'projectys.cui7ojvpzagk.us-east-2.rds.amazonaws.com',
    port = 3306,
    user = 'root',
    passwd = 'mypassword',
    db = 'pr_monitor',
    charset='utf8'
    )
    
cursor = conn.cursor()
    
        
#그래프 그리기#
def download_graph():
    conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '20121219Jun.K',
    db = 'pr_monitor',
    charset='utf8'
    )
    
    query = "SELECT * FROM monitor;"
    cursor.execute(query)
    result = cursor.fetchall()

    file = open('test.csv', 'w', encoding='utf-8', newline='')
    csv_wr = csv.writer(file)

    for row in result:
        csv_wr.writerow(row)

    file.close()