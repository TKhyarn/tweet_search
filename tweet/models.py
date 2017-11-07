from mongoengine import *
from tweet_search.settings import DBNAME
import tweepy
connect(DBNAME)

class tweet(Document):
    author = StringField(max_length=30)
    text = StringField(max_length=300)
    sentiment = StringField(max_length=300)
    hastag = StringField(max_length=20)
    date = DateTimeField()

# from tweet_search.settings import DBNAME
# import pymongo
#
# connMongo = pymongo.Connection('mongodb://localhost:27017')
# # Print the available MongoDB databases
# print (connMongo.database_names())
# # Close the MongoDB connection
# connMongo.close()
#
# connect(DBNAME)
#
# class Tweet(Document):
#     author = StringField(max_length=30)
#     text = StringField(max_length=300)
# # Create your models here.
