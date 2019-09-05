from django.shortcuts import render
from django.http import HttpResponse
from .connection import get_twitter_Connection
from nltk.stem.porter import *
import json


stemmer = PorterStemmer()

'''
In this function we gather data regarding specific keyword using twitter api
and do sentiment analysis over it using NLTK library (Stanford Open Source NLP Library)
and render the result over a word cloud html using d3.js

:param
    search_key = keyword which will be used for searching tweets. here we have hard coded the keyword to #Byjus
'''
def sentiment_analysis(request):

    twitter_api = get_twitter_Connection()
    search_key= "#Byjus"
    response = twitter_api.search(search_key, lang="en", include_entities=False)
    tweets = list()
    clean_data = list()
    tmp_data = list()
    tmp_string = ''
    for i in response:
        tweets.append(i.text)
    for i in tweets:
        st = str(tweets).split()
        for z in st:
            if str(z).find("@") == -1 :
                if str(z).find("http") == -1:
                    if len(z) > 3:
                        clean_data.append(z)

    for i in clean_data:
        x = (i, " : ", stemmer.stem(i))
        tmp_data.append(x[0])
    print(type(tmp_data))
    print(tmp_data)

    return render(request, 'wordCloud.html', {'data': json.dumps(tmp_data)})
