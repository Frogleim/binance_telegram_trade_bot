import logging
from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler, \
    CallbackQueryHandler
from binance.client import Client
import os
import json
from core.read_json import read_traders

API_TOKEN = '6163015498:AAEb03qyxgZK_eFhaLO9egAUGVfZxjMnkWg'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define conversation states
START, FIRST, SECOND, MAIN_MENU, BUTTON, CHECK_BUTTON = range(6)


def start(update: Update, context: CallbackContext):
    """Start the conversation and ask the user for input."""
    keyboard = [
        [
            InlineKeyboardButton("Settings", callback_data=f"Settings"),
        ],
        [
            InlineKeyboardButton("Traders", callback_data="Traders")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = "Choose option:"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, reply_markup=reply_markup)

    return FIRST


# def return_to_main_menu(update, context):
#     print("returning...")
#     """Return user to main menu."""
#     query = update.callback_query
#     query.answer()
#     reply_markup = get_main_menu_keyboard()
#     context.bot.send_message(chat_id=update.effective_chat.id,
#                              text="Returning to main menu...",
#                              reply_markup=reply_markup)
#     return MAIN_MENU

def first(update: Update, context: CallbackContext):
    """Ask the user for their age."""
    query = update.callback_query
    keyboard = [
        [
            InlineKeyboardButton("Main Menu", callback_data=f"main_menu"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    user_id = update.effective_user.id

    if query.data == "Settings":
        if os.path.isfile(os.path.join('./data', f'{user_id}.json')):
            context.bot.send_message(chat_id=update.effective_chat.id, text="You already signed in!",
                                     reply_markup=reply_markup)
            return MAIN_MENU
        else:
            message = "Enter your Binance.com API Key and Secret Key"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            return SECOND

    elif query.data == "Traders":
        traders = read_traders()
        keyboard = []
        for trader in traders:
            button_text = "✅" + trader["nickName"] if trader["nickName"] in followed_trader_data else trader["nickName"]
            callback_data = f"1 {trader['nickName']}" if trader[
                                                             "nickName"] not in followed_trader_data else f"2 {trader['nickName']}"
            keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])
        reply_markup = InlineKeyboardMarkup(keyboard)
        keyboard_1 = [
            [
                InlineKeyboardButton("Mane Menu", callback_data="menu"),
            ],
            ]
        reply_markup_1 = InlineKeyboardMarkup(keyboard_1)

        context.bot.send_message(chat_id=update.effective_chat.id, text="Select the traders you want to follow:",
                                 reply_markup=reply_markup)

        context.bot.send_message(chat_id=update.effective_chat.id, text="Save and Return",
                                 reply_markup=reply_markup_1)
        return BUTTON


followed_trader_data = []


def button_callback(update, context):
    query = update.callback_query
    print(query.data)
    query.answer()
    users_data = {}
    user_id = update.effective_user.id
    global followed_trader_data

    if '1' in query.data:
        followed_trader = query.data.split()[1]
        if followed_trader not in followed_trader_data:
            followed_trader_data.append(followed_trader)
            button_text = "✅" + followed_trader
        else:
            followed_trader_data.remove(followed_trader)
            button_text = followed_trader

        users_data[user_id] = {"followed_traders": followed_trader_data}
        print(followed_trader_data)

        traders = read_traders()
        keyboard = []
        for trader in traders:
            if trader["nickName"] == followed_trader:
                button_text = '✅' + followed_trader if followed_trader in followed_trader_data else followed_trader
            else:
                button_text = "✅" + trader["nickName"] if trader["nickName"] in followed_trader_data else trader[
                    "nickName"]
            callback_data = f"1 {trader['nickName']}" if trader[
                                                             "nickName"] not in followed_trader_data else f"2 {trader['nickName']}"
            keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_reply_markup(reply_markup=reply_markup)

        # Check if the followed trader is in the followed_trader_data list
        if followed_trader in followed_trader_data:
            # Find the button corresponding to the followed trader
            for row in reply_markup.inline_keyboard:
                for button in row:
                    if button.callback_data == f"1 {followed_trader}":
                        # Update the button text to add the cross emoji
                        button.text = "❌" + followed_trader
                        break
    elif '2' in query.data:
        unfollowed_trader = query.data.split()[1]
        if unfollowed_trader in followed_trader_data:
            followed_trader_data.remove(unfollowed_trader)
            print(followed_trader_data)

            traders = read_traders()
            keyboard = []
            for trader in traders:
                if trader["nickName"] == unfollowed_trader:
                    button_text = unfollowed_trader
                else:
                    button_text = "✅" + trader["nickName"] if trader["nickName"] in followed_trader_data else trader[
                        "nickName"]
                callback_data = f"1 {trader['nickName']}" if trader[
                                                                 "nickName"] not in followed_trader_data else f"2 {trader['nickName']}"
                keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])

            reply_markup = InlineKeyboardMarkup(keyboard)
            query.edit_message_reply_markup(reply_markup=reply_markup)

            # Find the button corresponding to the unfollowed trader
            for row in reply_markup.inline_keyboard:
                for button in row:
                    if button.callback_data == f"2 {unfollowed_trader}":
                        # Update the button text to remove the cross emoji
                        button.text = unfollowed_trader
                        break

    elif query.data == "menu":
        keyboard = []
        callback_data = "main_menu"
        button_text = "Save Data"
        keyboard.append([InlineKeyboardButton(button_text, callback_data=callback_data)])

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_reply_markup(reply_markup=reply_markup)
        return MAIN_MENU

    users_data[user_id] = {"followed_traders": followed_trader_data}
    with open(f'./data/following/{user_id}_followed_traders.json', 'w') as f:
        json.dump(users_data, f)


def main_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Settings", callback_data=f"Settings"),
        ],
        [
            InlineKeyboardButton("Traders", callback_data="Traders")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Main menu", reply_markup=reply_markup)
    return FIRST


def connect_to_binance(update: Update, context: CallbackContext):
    """Echo the user's age and end the conversation."""
    users_data = {}
    api_key = update.message.text.split()[0]
    api_secret_key = update.message.text.split()[1]
    keyboard = [
        [
            InlineKeyboardButton("Main Menu", callback_data=f"main_menu"),
        ],

    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id, text="You connected successfully",
                             reply_markup=reply_markup)

    user_id = update.effective_user.id
    print(user_id)
    users_data[user_id] = {
        "api_key": api_key,
        "api_secret": api_secret_key
    }
    with open(f'./data/{user_id}.json', 'w') as f:
        json.dump(users_data, f)
    print(users_data)
    return MAIN_MENU


def make_order(api_key, api_secret):
    api_key = api_key
    api_secret = api_secret

    client = Client(api_key, api_secret)
    traders_username = None
    # Define order parameters
    file = open("./users_follows.json", encoding="utf8")
    data = json.load(file)
    for username in data:
        traders_username = username["followed trader"]
        print(traders_username)
    all_trades = open("./core/Trades.json", encoding="utf8")
    all_data = json.load(all_trades)
    for all_trade in all_data:
        if traders_username == all_trade["username"]:
            print(all_trade)
            symbol = all_trade["Symbol"].split()[0]
            if all_trade["Direction"] == "Long":
                side = Client.SIDE_BUY
            else:
                side = Client.SIDE_SELL
            type = Client.ORDER_TYPE_MARKET
            quantity = 1
            leverage = all_trade["Leverage"]
            leverage_without_x = leverage.replace("x", "")
            leverage = int(leverage_without_x)

            # Place order
            order = client.futures_create_order(symbol=symbol, side=side, type=type, quantity=quantity,
                                                leverage=leverage)
            print(order)


def cancel(update: Update, context: CallbackContext) -> int:
    """End the conversation."""
    update.message.reply_text(
        'Okay, bye! Let me know if you need anything else.'
    )
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(API_TOKEN, use_context=True)

    # Set up the conversation handler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(first)],
            SECOND: [MessageHandler(Filters.text & ~Filters.command, connect_to_binance)],
            MAIN_MENU: [CallbackQueryHandler(main_menu)],
            BUTTON: [CallbackQueryHandler(button_callback)],

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    # Add the conversation handler to the dispatcher
    updater.dispatcher.add_handler(conv_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()
