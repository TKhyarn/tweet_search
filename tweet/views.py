from datetime import datetime

import textblob
import tweepy
from django.shortcuts import render

from tweet.models import tweet as tweet_bdd
from tweet_search.settings import consumer_key, consumer_secret, access_token, access_token_secret
from .forms import SearchForm, SearchHastag


def date(request):
    return render(request, 'tweet/date.html', {'date':datetime.now()})


def search_tweet(request):
    formSearch = SearchForm(request.POST or None)
    if formSearch.is_valid():
        l_tweet = []
        sFormValid = "Form is valid"
        author = formSearch.cleaned_data['author']
        hastag = formSearch.cleaned_data['hastag']
        if (author == "" and hastag != ""):
            for post in tweet_bdd.objects(hastag=hastag):
                l_tweet.append(post)
            send = True
        elif (hastag == "" and author != ""):
            for post in tweet_bdd.objects(author=author):
                l_tweet.append(post)
            send = True
        elif (hastag != "" and author != ""):
            for post in tweet_bdd.objects(hastag=hastag, author=author):
                l_tweet.append(post)
            send = True
        elif (hastag == "" and author == ""):
            send = False
    return render(request, 'tweet/search.html', locals())

def home(request):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    hashtag = SearchHastag(request.POST or None)
    if hashtag.is_valid():
        search = hashtag.cleaned_data['hashtag']
        public_tweets = api.search(q=search+'filter:retweets', rpp='2', count='100')
        l_tweet = []
        for tweet in public_tweets:
            try:
                author = tweet.author._json['screen_name']
                text = textblob.TextBlob(tweet.text)
                sentiment = text.sentiment
                hastag = search
                date = str(tweet.created_at)
                tweet = tweet_bdd(author=author, text=str(text), sentiment=str(sentiment), hastag=hastag, date=date)
                tweet.save()
                l_tweet.append(tweet)
            except:
                print("Error")

    return render(request, 'tweet/home.html', locals())