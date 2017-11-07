import mongoengine

DBNAME = 'NAME'
_MONGODB_HOST ='localhost'
_MONGODB_USER = 'root'
_MONGODB_PASSWD = 'root'
_MONGODB_NAME = 'NAME'
_MONGODB_DATABASE_HOST = \
    'mongodb://%s:%s@%s/%s' \
    % (_MONGODB_USER, _MONGODB_PASSWD, _MONGODB_HOST, _MONGODB_NAME)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Secret key'


mongoengine.connect('NAME', host='127.0.0.1',  port=27017)

# Tweeter authentification
consumer_key = 'tweeter_consumer_key'
consumer_secret = 'tweeter_consumer_secret'
access_token = '925623295-tweeter_access_token'
access_token_secret = 'tweeter_access_token_secret'