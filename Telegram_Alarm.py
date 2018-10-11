# -*- coding: utf-8 -*-
# 추후 구현 가능 예정임
import telepot

def telegram_Alarm(cpu_percent, memory_result, Result):    
    bot = telepot.Bot('691038392:AAGsm2O_i86-0exuQ_lzYcwXpZx72_gi9-g')
    chat_id = '559561088'
    print(bot.getMe())