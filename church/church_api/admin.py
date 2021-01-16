from django.contrib import admin
from .models import News, PraySchedule


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', )


@admin.register(PraySchedule)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('date', 'day_name')