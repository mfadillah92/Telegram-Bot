import os
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')

bot = Bot(token=bot_token)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Selamat datang di bot Telegram saya.")

def menu(update: Update, context: CallbackContext):
    text_menu = "/puisi /pantun"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_menu)

def puisi(update: Update, context: CallbackContext):
    text_puisi = "Aku lalai di hari pagi, Beta lelah di masa muda, Kini hidup meracuni hati, Miskin ilmu miskin harta. 😔"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_puisi)

def pantun(update: Update, context: CallbackContext):
    text_pantun = "Lipatlah kertas origami, Kertas dibentuk selebar kaki. Dengan kita silaturahmi, Panjang umur murah rezeki."
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_pantun)

def echo(update: Update, context: CallbackContext):
    message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    print(f"pesan dari user: {message}")

updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('menu', menu))
dispatcher.add_handler(CommandHandler('puisi', puisi))
dispatcher.add_handler(CommandHandler('pantun', pantun))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()

updater.idle()