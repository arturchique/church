from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('treby/', asks, name="asks"),
    path('shrines/', shrines, name="shrines"),
    path('formation/', formation, name="formation"),
    path('ministry/', ministry, name="ministry"),
    path('history/', history, name="history"),
    path('sacraments/', sacraments, name="sacraments"),
    path('sacraments/unction/', unction, name="unction"),
    path('sacraments/communion/', communion, name="communion"),
    path('sacraments/confession/', confession, name="confession"),
    path('sacraments/marying/', marying, name="marying"),
    path('news/', news, name="news"),
    path('parse_news/', parse_news, name="parse_news"),
    path('parse_schedule/', parse_shedules, name='parse_schedule'),
    path('schedule/', schedule, name='schedule'),
    path('build/', build, name='build')
]