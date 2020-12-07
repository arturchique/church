from django.shortcuts import render


def index(request):
    return render(
        request,
        'index.html',
        context={},
    )


def asks(request):
    return render(
        request,
        'asks.html',
        context={},
    )