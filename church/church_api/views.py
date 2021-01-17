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


def parse_news(request):
    NewsParser.load_last_post()


def parse_shedules(request):
    parser = ScheduleParser(creds=GOOGLE_API_CREDENTIALS)
    parser.load_schedules()


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