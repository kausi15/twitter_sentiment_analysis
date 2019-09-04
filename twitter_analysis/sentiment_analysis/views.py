from django.shortcuts import render
from django.http import HttpResponse
from .connection import get_twitter_Connection
import tweepy

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sentiment_analysis(request):
    import pdb
    pdb.set_trace()
    twitter_api = get_twitter_Connection()
    response = twitter_api.search("#byjus",lang="en",include_entities=False)
    tweets = list()
    for i in response:
        tweets.append(i.text)



    return HttpResponse(tweets)
