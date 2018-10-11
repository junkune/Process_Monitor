# -*- coding: utf-8 -*-
import time
import pymysql

def data_insert(cpu_percent,memory):
    
    cpu = cpu_percent
    memory_percent = memory
    time_result = time.strftime('%m-%d %H:%M')
    
    conn = pymysql.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '20121219Jun.K',
        db = 'pr_monitor',
        charset='utf8'
        )
    
    cursor = conn.cursor()
    
    query = "INSERT INTO monitor (cpu, memory, time) VALUES (%s, %s, %s)"
    cursor.execute(query, (cpu, memory_percent, time_result))
    
    conn.commit()
    
    conn.close()