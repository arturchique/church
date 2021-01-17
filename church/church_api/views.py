from django.shortcuts import render
from .models import *
from .parsers import NewsParser, ScheduleParser
from django.views.generic import ListView
from .constants import GOOGLE_API_CREDENTIALS, NAME_DAYS
from datetime import date
import re


def index(request):
    post = News.objects.all().order_by('time').reverse()[0] # NewsParser.load_last_post()
    img = str(post.image).split("/")[-1]
    text = post.text[:250]
    schedule = PraySchedule.objects.all()[:3]
    name_days = NAME_DAYS[date.today().strftime('%m-%d')]
    name_days = re.sub(r'\([^\)]+\)', '', name_days)

    return render(
        request,
        'index.html',
        context={
            'post': post,
            'img': img,
            'text': text,
            'schedule': schedule,
            'name_days': name_days
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


def history(request):
    return render(
        request,
        "history.html",
        context={}
    )


def unction(request):
    return render(
        request,
        "unction.html",
        context={},
    )


def communion(request):
    return render(
        request,
        "communion.html",
        context={},
    )


def sacraments(request):
    return render(
        request,
        "sacraments.html",
        context={},
    )


def parse_news(request):
    NewsParser.load_last_post()


def parse_shedules(request):
    parser = ScheduleParser(creds=GOOGLE_API_CREDENTIALS)
    parser.load_schedules()


def news(request):
    feed = News.objects.all().order_by('time').reverse()
    return render(
        request,
        'news.html',
        context={
            "feed": feed
        }
    )


def schedule(request):
    schedule = PraySchedule.objects.all()
    return render(
        request,
        'schedule.html',
        context={
            "schedule": schedule
        }
    )