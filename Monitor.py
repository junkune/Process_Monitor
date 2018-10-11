# -*- coding: utf-8 -*-
import psutil
import DB_Insert
import Telegram_Alarm
import Create_Monitor

# PROCESS CHECK 함수
def process_check():
    # cpu결과
    cpu_percent = psutil.cpu_percent(interval=1)
    # memory 추출
    memory = psutil.virtual_memory()[2:3]
    # memory 결과
    memory_result = memory[0]
    # data_insert 입력
    DB_Insert.data_insert(str(cpu_percent), str(memory_result))
    
    Create_Monitor.download_graph()  
    
    
    if(cpu_percent > 50 or memory[0] > 70):
        # TOP 3 MEMORY_PERCENT
        memory_Percent = ([(p.pid, p.info) for p in sorted(psutil.process_iter(attrs=['name', 'memory_percent']), key=lambda p: p.info['memory_percent'])][-3:])
        # TOP 3 DISK_IO
        disk_IO = ([(p.pid, p.info) for p in sorted(psutil.process_iter(attrs=['name', 'io_counters']), key=lambda p: p.info['io_counters'])][-3:])
        # TOP 3 CPU
        CPU = ([(p.pid, p.info) for p in sorted(psutil.process_iter(attrs=['name', 'cpu_percent']), key=lambda p: p.info['cpu_percent'])][-3:])

        Result = "현재 CPU 사용량" + str(cpu_percent) + "현재 메모리 사용량" + str(memory[0]) + "\n[TOP3 Memory]\n" + str(memory_Percent) + "\n[TOP3 DISK_IO]\n" + str(disk_IO) + "\n[TOP3 CPU]\n" + str(CPU)
        
        Telegram_Alarm.telegram_Alarm(cpu_percent, memory_result, Result)
