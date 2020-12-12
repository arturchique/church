from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('treby/', asks, name="asks"),
    path('shrines/', shrines, name="shrines"),
]