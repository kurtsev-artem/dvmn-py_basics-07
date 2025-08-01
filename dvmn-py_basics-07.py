import ptbot
import os
import random
from dotenv import load_dotenv
from pytimeparse import parse
load_dotenv()

TG_TOKEN = os.getenv('TG_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')
bot = ptbot.Bot(TG_TOKEN)
timeout = 5


def answer_timeout(chat_id, question):
    bot.send_message(chat_id, "Время вышло")

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)    

def reply(chat_id, question):
    message_id =  bot.send_message(chat_id, "Запускаю таймер...")
    bot.create_countdown(timeout, notify, chat_id=chat_id,message_id = message_id)
    bot.create_timer(timeout, answer_timeout, chat_id=chat_id, question=question)

def notify(secs_left, chat_id, message_id):
    bot.update_message(chat_id,message_id ,"Осталось {} секунд!\n {}".format(secs_left,render_progressbar(timeout, timeout - secs_left))  )

bot = ptbot.Bot(TG_TOKEN)
bot.reply_on_message(reply)  
bot.run_bot()
