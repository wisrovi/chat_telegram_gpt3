from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters) 
# pip install python-telegram-bot
from gpt3 import ask, append_interaction_to_chat_log

from config import TOKEN_TELEGRAM

session = dict() # lugar donde se guarda el historico de todos los chat

import os
BASE_DIR = os.getcwd() + "/"

def readSession(path):
    try:
        with open(BASE_DIR+path) as f:
            contents = f.read()
        return contents
    except:
        return None

def writeSession(path, contents):
    with open(BASE_DIR+path, "w") as f:
        f.write(contents)


def start(update, context):
    context.bot.send_message(update.message.chat_id, "Bienvenido!!")


def mensaje_nocomando(update, context):
    global session
    cid=update.message.chat_id
    data_input = update.message.text
    chat_log = session.get(cid)

    PATH_CHAT = "chats/"+str(cid)+".chat"
    if chat_log is None:
        chat_log = readSession(PATH_CHAT)

    answer = ask(data_input, chat_log)    
    session[cid] = append_interaction_to_chat_log(data_input, answer,chat_log)                         

    writeSession(PATH_CHAT, session[cid])

    #print(PATH_CHAT, session[cid])

    

    update.message.reply_text(answer) # Respondemos al comando con el mensaje
    
       

def main():
    updater=Updater(TOKEN_TELEGRAM, use_context=True)
    dp=updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler("start", start))    
    dp.add_handler(MessageHandler(Filters.text, mensaje_nocomando))

    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    updater.idle()
    
if __name__ == '__main__':
    print("Sistema iniciado")
    main()
