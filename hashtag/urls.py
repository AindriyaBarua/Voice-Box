from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('view', views.hashtag_list, name='hashtag_list'),
    path('art', views.hashtag_art, name='hashtag_art'),
    path('food', views.hashtag_food, name='hashtag_food'),
    path('tech', views.hashtag_tech, name='hashtag_tech'),
    path('mood', views.hashtag_mood, name='hashtag_mood'),
    path('wildlife', views.hashtag_wildlife, name='hashtag_wildlife'),
    path('fashion', views.hashtag_fashion, name='hashtag_fashion'),

    ]
