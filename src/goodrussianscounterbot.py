import os
import time

from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

from dotenv import load_dotenv
import scraper
from messages import message_number_of_dead_orcs, message_rest_of_the_casualties
from data_sources import COME_BACK_ALIVE_URL

load_dotenv()


updater = Updater(
    os.getenv('API_TOKEN'),
    use_context=True
)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Привіт! Цей бот буде з радістю нагадувати тобі статистику по <i>хорошім руськім</i>.", parse_mode="html")
    time.sleep(2)
    update.message.reply_text("Для того, щоб дізнатися свіженькі цифри, тицьни /get_stats")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available commands :-
    /start - start the bot
    /get_stats - get statistics
    """)


def get_stats(update: Update, context: CallbackContext):
    casualties_data = scraper.update()
    update.message.reply_text(message_number_of_dead_orcs(casualties_data))
    time.sleep(1.5)

    update.message.reply_text(message_rest_of_the_casualties(casualties_data))
    time.sleep(3)

    update.message.reply_text(f'Хочешь більше? Донать на <a href="{COME_BACK_ALIVE_URL}">ЗСУ</a>!', parse_mode='html')

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(f"Дуже перепрошую, але я не розумію, шо ви говорите. Мені надіслали {update.message.text}, а треба брати звідси: /help")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('get_stats', get_stats))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))


updater.start_polling()
