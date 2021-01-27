import os
from django.shortcuts import render
from .models import *
from .parsers import NewsParser, ScheduleParser, DaysParser
from django.views.generic import ListView
from .constants import GOOGLE_API_CREDENTIALS, NAME_DAYS, EVENTS
from datetime import date
import datetime
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    today = date.today().strftime('%m-%d')
    today_day = date.today().strftime('%d')

    post = News.objects.all().order_by('time').reverse()[0] # NewsParser.load_last_post()
    img = str(post.image).split("/")[-1]
    text = post.text[:200]

    schedule = []
    schedule += PraySchedule.objects.filter(date__contains=f"{today_day} ")
    schedule += PraySchedule.objects.filter(date__contains=f"{(date.today() + datetime.timedelta(days=1)).strftime('%d')} ")
    schedule += PraySchedule.objects.filter(date__contains=f"{(date.today() + datetime.timedelta(days=2)).strftime('%d')} ")

    name_days = NAME_DAYS[today]
    name_days = re.sub(r'\([^\)]+\)', '', name_days)

    event_today = EVENTS[today]
    event_tomorrow = EVENTS[(date.today() + datetime.timedelta(days=1)).strftime('%m-%d')]

    gallery = []
    gallery_dir = BASE_DIR / 'static/imgs/gallery/'
    for root, dirs, files in os.walk(gallery_dir):
        for file in files:
            gallery.append(file)

    return render(
        request,
        'index.html',
        context={
            'post': post,
            'img': img,
            'text': text,
            'schedule': schedule,
            'name_days': name_days,
            'gallery': gallery,
            'event_today': event_today,
            'event_tomorrow': event_tomorrow,
            'day': today_day
        },
    )


def asks(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/treby">Требы</a></u>'
    return render(
        request,
        'asks.html',
        context={
            "bread_crumps": bread_crumps
        },
    )


def shrines(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/shrines">Святыни</a></u>'
    return render(
        request,
        'shrines.html',
        context={
            "bread_crumps": bread_crumps
        },
    )


def formation(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/formation">Образование</a></u>'
    return render(
        request,
        "formation.html",
        context={
            "bread_crumps": bread_crumps
        },
    )


def ministry(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/ministry">Духовенство</a></u>'
    return render(
        request,
        "ministry.html",
        context={
            "bread_crumps": bread_crumps
        }
    )


def history(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/history">Храм в передельцах</a></u>'
    return render(
        request,
        "history.html",
        context={
            "bread_crumps": bread_crumps
        }
    )


def unction(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/sacraments">Таинства</a></u> / <u><a href="/sacraments/unction">Соборование</a></u>'
    return render(
        request,
        "unction.html",
        context={
            "bread_crumps": bread_crumps
        },
    )


def communion(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/sacraments">Таинства</a></u> / <u><a href="/sacraments/communion">Причастие</a></u>'
    return render(
        request,
        "communion.html",
        context={
            "bread_crumps": bread_crumps
        },
    )


def sacraments(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/sacraments">Таинства</a></u>'
    return render(
        request,
        "sacraments.html",
        context={
            "bread_crumps": bread_crumps
        },
    )


def parse(request):
    NewsParser.load_last_post()

    schedule_parser = ScheduleParser(creds=GOOGLE_API_CREDENTIALS)
    schedule_parser.load_schedules()

    day_events_parser = DaysParser(creds=GOOGLE_API_CREDENTIALS)
    day_events_parser.load_days()


def news(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/news">Новости</a></u>'
    feed = News.objects.all().order_by('time').reverse()
    return render(
        request,
        'news.html',
        context={
            "bread_crumps": bread_crumps,
            "feed": feed
        }
    )


def schedule(request):
    schedule = PraySchedule.objects.all()
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/schedule">Расписание богослужений</a></u>'
    return render(
        request,
        'schedule.html',
        context={
            "bread_crumps": bread_crumps,
            "schedule": schedule
        }
    )


def confession(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/sacraments">Таинства</a></u> / <u><a href="/sacraments/confession">Исповедь</a></u>'
    return render(
        request,
        'confession.html',
        context={
            "bread_crumps": bread_crumps
        }
    )


def marying(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/sacraments">Таинства</a></u> / <u><a href="/sacraments/marying">Венчание</a></u>'
    return render(
        request,
        'marying.html',
        context={
            "bread_crumps": bread_crumps
        }
    )


def build(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/build">Строительство храма</a></u>'
    return render(
        request,
        'build.html',
        context={
            "bread_crumps": bread_crumps
        }
    )


def epiphany(request):
    bread_crumps = '<u><a href="/">Главная</a></u> / <u><a href="/sacraments">Таинства</a></u> / <u><a href="/sacraments/epiphany">Крещение</a></u>'
    return render(
        request,
        'epiphany.html',
        context={
            "bread_crumps": bread_crumps
        }
    )