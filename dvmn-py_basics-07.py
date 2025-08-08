import ptbot
import os
from dotenv import load_dotenv

TIMEOUT = 5


def answer_timeout(chat_id,bot):
    bot.send_message(chat_id, "Время вышло")
    

def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def reply(chat_id,question,bot):
    message_id =  bot.send_message(chat_id, "Запускаю таймер...")
    bot.create_countdown(TIMEOUT, notify, chat_id=chat_id,message_id=message_id,bot=bot)
    bot.create_timer(TIMEOUT, answer_timeout, chat_id=chat_id,bot=bot)
    

def notify(secs_left, chat_id, message_id,bot):
    bot.update_message(chat_id,message_id ,"Осталось {} секунд!\n {}".format(secs_left,render_progressbar(TIMEOUT, TIMEOUT - secs_left))  )
    

def main():
    load_dotenv()
    tg_token = os.getenv('TG_TOKEN')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(reply,bot=bot)  
    bot.run_bot()
    

if __name__ == '__main__':
    main()    
