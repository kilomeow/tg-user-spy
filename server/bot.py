# создаем телеграм бота
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, commandhandler
from telegram import Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.utils.request import Request

import config

import json

req = Request(proxy_url=config.proxy) if config.proxy else Request()
bot = Bot(config.token, request=req)
upd = Updater(bot=bot, use_context=True)
dp = upd.dispatcher

# логирование
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

# приветственное сообщение
def hello(update, context):
    update.message.reply_text('hello')
    

def new_users(update, context):
    for user in update.message.new_chat_members:
        if user.id == config.bot_id:
            hello(update, context)
        else:
            update.message.reply_text(json.dumps(user.to_dict(), indent=2, ensure_ascii=False))


dp.add_handler(CommandHandler('start', hello))
dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_users))

def main():
    upd.start_polling()
    upd.idle()

if __name__ == '__main__':
    main()
