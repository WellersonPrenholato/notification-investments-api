import telebot
import os
from dotenv import load_dotenv
import pandas as pd
from Database.verify_database_csv import verify_database_google

load_dotenv()
token = os.getenv('AUTH_TOKEN_TELEGRAM')
chat_id = os.getenv('CHAT_ID_TELEGRAM')

bot = telebot.TeleBot(token)

def enviar_mensagem():
    # log_message = f'Mensagem enviada às {hora_formatada}'
    response = verify_database_google()
    print(response)

    bot.send_message(chat_id, response)

enviar_mensagem()