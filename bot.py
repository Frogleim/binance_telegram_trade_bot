import logging
import telegram
from telegram import ReplyKeyboardMarkup, Bot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, \
    Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import time
from config import LOGIN, TRADERS, TOKEN, GROUP_ID, ADMIN_ID
import pandas as pd
from core import read_json

class Bots:
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self.users_data = {}
        self.updater = Updater(TOKEN)
        self.users_lst = []

    def start(self, update, context):
        """Send a message when the command /start is issued."""
        user_id = update.message.from_user.id
        username = update.message.chat.first_name
        chat_id = update.effective_chat.id
        print(chat_id)
        # if user_id not in self.users_data:
        #     self.users_data[user_id] = UserData(user_id=user_id, user_name=username)
        #     self.users_lst.append(self.users_data[user_id])
        #     user_info_file = pd.DataFrame(self.users_lst)
        #     user_info_file.to_excel('users_info.xlsx')
        # https: // t.me / binance_betting_test_bot
        #     print(self.users_data)
        # else:
        #     print('UserID already')
        keyboard = [
            [
                InlineKeyboardButton("LOGIN", callback_data="Այսօր"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(chat_id=ADMIN_ID,  text=f'Great! No please answer the first '
                                                                        f'question:\n\n '
                                                                        , parse_mode='HTML')
        return TRADERS

    def send_traders_data(self, update, context):
        traders_data = read_json.read()
        for traders in traders_data:
            print(f"Trader: {traders['nickName']}")
            print(f"Weekly PNL: +{round(float(traders['pnl']) * 100, 4)}")
            print(f"Weekly ROI: +{round(float(traders['roi']) * 100, 4)}")
            context.bot.send_message(chat_id=GROUP_ID, text=f"Trader: {traders['nickName']}\n"
                                                            f"Weekly PNL: +{round(float(traders['pnl']) * 100, 4)}\n"
                                                            f"Weekly ROI: +{round(float(traders['roi']) * 100, 4)}"
                                     , parse_mode='HTML')
        return ConversationHandler.END


    def cancel(self, update, _):
        user = update.message.from_user
        update.message.reply_text(
            'You subscription was canceled'
        )
        return ConversationHandler.END

    def error(self, update, context):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, context.error)

    def run(self):
        """Start the bot."""
        dp = self.updater.dispatcher
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],

            states={
                TRADERS: [MessageHandler(Filters.text, self.send_traders_data)],
            },
            fallbacks=[CommandHandler('cancel', self.cancel)]
        )
        dp.add_handler(conv_handler)
        dp.add_error_handler(self.error)

        self.updater.start_polling()
        self.updater.idle()


if __name__ == "__main__":
    my_bot = Bots()
    my_bot.run()