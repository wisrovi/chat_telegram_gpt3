# -*- coding: utf-8 -*-

# !pip install python-telegram-bot

from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters)
from config import TOKEN_TELEGRAM as config
from gpt3 import getAnswer as gpt3
from files import writeSession as session

def start(update, context):
    context.bot.send_message(update.message.chat_id, "Bienvenido")

def mensaje_nocomando(update, context):
    cid = update.message.chat_id # obtengo el id_usuario
    question_user = update.message.text # obtengo el mensaje del usuario
    
    old_log = session.getLog(cid) # miro si hay un log previo cargado en cache, sino creo el cache para este usuario        
    answer, new_log = gpt3.getAnswer(question_user, old_log) # le pido a la IA una respuesta al comentario del usuario
    session.writeSession(cid, new_log) # guardo el cache para este usuario
    
    update.message.reply_text(answer) # respondo al usuario



if __name__=="__main__":
    print("Chatbot iniciado.")

    updater = Updater(config.TOKEN_TELEGRAM, use_context=True)
    dp=updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))    # respuesta al comando /start
    dp.add_handler(MessageHandler(Filters.text, mensaje_nocomando)) # respuesta a los comentarios del usuario
    
    updater.start_polling()    
    updater.idle()















