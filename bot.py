import logging
import subprocess
import time
import json
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, \
    CallbackQueryHandler
from core.read_json import read_trades

API_TOKEN = '5811589868:AAElvx1nnMo5vaPWY-J2tYQ2YGL5TSv158A'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

START, FIRST, SECOND = range(3)
data = []


def start(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask the user for input."""
    top_traders = read_trades()
    for trades in top_traders:
        message = f"{trades['username']}\nSymbol: {trades['Symbol']}\nDirection: {trades['Direction']}" \
                  f"\nLeverage: {trades['Leverage']}\nEntry price: {trades['Entry price']}"

        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        time.sleep(1)


def cancel(update: Update, context: CallbackContext) -> int:
    """End the conversation."""
    update.message.reply_text(
        'Okay, bye! Let me know if you need anything else.'
    )


if __name__ == '__main__':
    updater = Updater(API_TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()
