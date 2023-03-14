import subprocess
from core.main import read, GetData
import logging
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, \
    CallbackQueryHandler
from binance.client import Client
import os
import json
from config import ADMIN_TOKEN

trade_type = "DELIVERY"
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

START, FIRST, SECOND = range(3)


def start(update: Update, context: CallbackContext) -> int:
    """Start the conversation and ask the user for input."""
    keyboard = [
        [
            InlineKeyboardButton("Yes", callback_data=f"Yes"),
        ],
        [
            InlineKeyboardButton("No", callback_data="No")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Hi there! Do you want to change the current top ranking?',
        reply_markup=reply_markup
    )
    return FIRST


def first(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "Yes":
        keyboard = [
            [
                InlineKeyboardButton("USD$-M", callback_data=f"PERPETUAL"),
            ],
            [
                InlineKeyboardButton("COIN-M", callback_data="DELIVERY")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.callback_query.message.edit_text("Please choose options", reply_markup=reply_markup)

        return SECOND
    else:
        update.callback_query.message.edit_text("Let me know, when you will need something!")

        return ConversationHandler.END


def second(update: Update, context: CallbackContext):
    """Echo the user's age and end the conversation."""
    query = update.callback_query
    res = read(query.data)
    print(res)
    my_data = GetData(res)
    my_data.run_all()
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    """End the conversation."""
    update.message.reply_text(
        'Okay, bye! Let me know if you need anything else.'
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(ADMIN_TOKEN, use_context=True)

    # Set up the conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(first)],
            SECOND: [CallbackQueryHandler(second)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    # Add the conversation handler to the dispatcher
    updater.dispatcher.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()
