# -*- coding: utf-8 -*-
import time
import pymysql
import DB_Connection

def data_insert(cpu_percent,memory):
    
    conn = DB_Connection.Connection_DB()
    cursor = conn.cursor()
    
    cpu = cpu_percent
    memory_percent = memory
    time_result = time.strftime('%m-%d %H:%M')

    query = "INSERT INTO monitor (cpu, memory, time) VALUES (%s, %s, %s)"
    cursor.execute(query, (cpu, memory_percent, time_result))
    
    conn.commit()
    
    conn.close()