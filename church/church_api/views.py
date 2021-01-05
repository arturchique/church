from django.shortcuts import render
from .models import *
from .parsers import NewsParser
from django.views.generic import ListView


def index(request):
    post = News.objects.all().order_by('time').reverse()[0] # NewsParser.load_last_post()
    img = str(post.image).split("/")[-1]

    return render(
        request,
        'index.html',
        context={
            'post': post,
            'img': img
        },
    )


def asks(request):
    return render(
        request,
        'asks.html',
        context={},
    )


def shrines(request):
    return render(
        request,
        'shrines.html',
        context={},
    )


def formation(request):
    return render(
        request,
        "formation.html",
        context={},
    )


def ministry(request):
    return render(
        request,
        "ministry.html",
        context={}
    )