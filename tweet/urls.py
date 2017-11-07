from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home$', views.home, name="home"),
    url(r'^date$', views.date),
    url(r'^search_tweet$', views.search_tweet, name='search_tweet')
]
