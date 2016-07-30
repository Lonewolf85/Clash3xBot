#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import telegram
from telegram import (ReplyKeyboardMarkup,ReplyKeyboardHide)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,
                          ConversationHandler)
import logging
import clashAPICaller

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

HOME, CLANS, SEARCH_CLANS_NAME, SEARCH_CLANS_TAG, CLAN_INFO = range(5)

temp_tag = ""

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
	user = update.message.from_user
	logger.info("Bot Started : %s" % (user.first_name))
	bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	reply_keyboard = [['Clans', 'Bases'],['',''],['','']]
	bot.sendMessage(update.message.chat_id, text='Hi Chief '+user.first_name+' ! Welcome !',reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard = True, one_time_keyboard=True,))
	return HOME


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def clans_main(bot,update):
    user = update.message.from_user
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    reply_keyboard = [['Search Clans By Name', 'Search Clans By Tag']]
    bot.sendMessage(update.message.chat_id, text='Chief '+user.first_name+' ! Clans !',reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard = True, one_time_keyboard=False))
    return CLANS

def bases_main(bot,update):
    return HOME

#Search clans based on clan name
def search_clans_name(bot, update):
	bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	bot.sendMessage(update.message.chat_id, text='Chief! Give me a name to search!', reply_markup = ReplyKeyboardHide())
	return SEARCH_CLANS_NAME

def search_by_name(bot, update):
	bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	key = update.message.text
	clan_list = clashAPICaller.search_clans(key)
	bot.sendMessage(update.message.chat_id, text=clan_list)
	return

#Search clans based on clan tag
def search_clans_tag(bot, update):
	bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	bot.sendMessage(update.message.chat_id, text='Chief! Give me a tag to search!')
	return SEARCH_CLANS_TAG

def search_by_tag(bot, update):
	user = update.message.from_user
	reply_keyboard = [['Get Members List', 'Get Warlogs']]
	logger.info("Search by tag : %s" % (user.first_name))
	bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	key = update.message.text
	key = key.replace('#',"%23")
	global temp_tag
	temp_tag = key
	clan_list = clashAPICaller.search_clans_tag(key)
	bot.sendMessage(update.message.chat_id, text=clan_list,reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
	return CLAN_INFO


#Search clans based on clan tag
def get_clan_members(bot, update):
	user = update.message.from_user
	logger.info("Get clan members for %s: %s" % (temp_tag,user.first_name))
	bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	clan_list = clashAPICaller.get_clan_members(temp_tag)
	bot.sendMessage(update.message.chat_id, text=clan_list)
	return CLAN_INFO

#Search clans based on clan tag
def get_warlogs(bot, update):
	user = update.message.from_user
	logger.info("Get warlogs for %s: %s" % (temp_tag,user.first_name))
	clan_list = clashAPICaller.get_warlogs(temp_tag)
	bot.sendMessage(update.message.chat_id, text=clan_list)
	return CLAN_INFO


def unknown_message(bot, update):
    bot.sendMessage(update.message.chat_id, text="We are working on it! Use /start ."+telegram.Emoji.PILE_OF_POO)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def cancel(bot, update):
    user = update.message.from_user
    logger.info("User %s canceled the conversation." % user.first_name)
    bot.sendMessage(update.message.chat_id,
                    text='Bye! I hope we can talk again some day. CLASH ONN!')

    return ConversationHandler.END


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("225770137:AAEtlT534Xe4jOminmjeh2S3xP5dsJLfgug")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    #dp.add_handler(CommandHandler("start", start))
    #dp.add_handler(CommandHandler("help", help))
    #dp.add_handler(CommandHandler("searchClans", search_clans, pass_args=True))
    #dp.add_handler(CommandHandler("searchClansTag", search_clans_tag, pass_args=True))
    #dp.add_handler(CommandHandler("getMembers", get_clan_members, pass_args=True))
    #dp.add_handler(CommandHandler("getWarlogs", get_warlogs, pass_args=True))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            HOME: [RegexHandler('^(Clans)$', clans_main),RegexHandler('^(Bases)$', bases_main),CommandHandler('start', start)],

            CLANS: [RegexHandler('^(Search Clans By Name)$', search_clans_name),RegexHandler('^(Search Clans By Tag)$', search_clans_tag),CommandHandler('start', start)],

            SEARCH_CLANS_NAME: [MessageHandler([Filters.text], search_by_name),CommandHandler('start', start)],

            SEARCH_CLANS_TAG: [MessageHandler([Filters.text], search_by_tag),CommandHandler('start', start)],

            CLAN_INFO: [RegexHandler('^(Get Members List)$', get_clan_members),RegexHandler('^(Get Warlogs)$', get_warlogs),CommandHandler('start', start)],
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dp.add_handler(conv_handler)


    # on noncommand 
    dp.add_handler(MessageHandler([Filters.text], unknown_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
