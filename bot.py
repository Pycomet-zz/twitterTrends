## This is the telegram bot script to forward the tweets to a group

import telebot
from tweets import *

bot = telebot.TeleBot(
    token = os.getenv('TOKEN'),
    threaded = True
)

@bot.message_handler(commands=['start'])
def get_started(msg):
    "Echo Handler"
    keywords = ['#EndSars', '#EndSWAT']

    tweets = get_tweets(keywords)

    for each in tweets:
        bot.reply_to(
            msg,
            f"""
    {each}

    By Twitter Trends
            """
        )


bot.polling()