# -*- coding: utf-8 -*-
import Monitor
import graph
from time import sleep
import threading

# Main Program
def Main_Start():
    timer = threading.Timer(60,Monitor.process_check)
    timer.start()
    
if __name__ == "__main__":
    Main_Start()