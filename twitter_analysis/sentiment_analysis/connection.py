import tweepy
from .credentials import consumer_key,consumer_secret,access_token,access_token_secret

def get_twitter_Connection():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth)
    return twitter_api