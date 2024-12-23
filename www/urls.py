from django.urls import path
from django.views.generic import detail

from .views import *

urlpatterns = [
    # PATH
    path('', index, name='index'),
    path('game/<slug:slug>/', detail, name='detail'),
    path('company/<slug:slug>/', detail_company, name='detail_company'),
    path('all/games/', all_games, name='all_games'),
    path('all/company/', all_company, name='all_company'),

    # UTILS
    path('subscribe', subscribe, name='subscribe'),
]