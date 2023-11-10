import telebot
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
token = os.getenv('AUTH_TOKEN_TELEGRAM')
chat_id = os.getenv('CHAT_ID_TELEGRAM')

bot = telebot.TeleBot(token) # creating a instance

# Função para processar mensagens recebidas
def enviar_mensagem():
    # Obter a hora, minuto e segundo atuais
    agora = datetime.datetime.now()
    hora_atual = agora.hour
    minuto_atual = agora.minute
    segundo_atual = agora.second

    # Mensagem a ser registrada no log
    log_message = f'Mensagem enviada às {hora_atual:02d}:{minuto_atual:02d}:{segundo_atual:02d}'
    print(log_message)

    # Responder à mensagem
    mensagem = 'Olá, meus investimentos.'
    bot.send_message(chat_id, mensagem)

enviar_mensagem()