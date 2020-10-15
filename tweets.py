## This program retrieves the latest tweeks based on search keywords
from TwitterSearch import *


def get_tweets(keywords):
    """
    Return the lastest tweets for the keyword search
    """
    tweets = []

    try:
        order = TwitterSearchOrder()
        
        #Setting conditions
        order.set_keywords(keywords) #keywords in a list for search
        order.set_language('en') #english tweets only
        order.set_include_entities(False)

        search = TwitterSearch(
            consumer_key = os.getenv('CONSUMER_KEY'),
            consumer_secret = os.getenv('CONSUMER_SECRET'),
            access_token = os.getenv('ACCESS_TOKEN'),
            access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
        )

        #iterating through posts
        for tweet in search.search_tweets_iterable(order):
            tweets.append(f"{tweet['user']['screen_name']} just tweeted: {tweet['text']}")

        return tweets

    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)
        return tweets