from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок новости", help_text="Заголовок новости",
                             max_length=80, blank=False)
    text = models.TextField(verbose_name="Текст новости", help_text="Текст новости", blank=False)
    image = models.TextField(verbose_name="Фото", help_text="Фото", blank=True, null=True)
    time = models.DateTimeField(verbose_name="Дата и время публикации", blank=False,
                                help_text="Дата и время публикации")


class PraySchedule(models.Model):
    date = models.TextField(verbose_name="Дата и день", help_text="Дата и день", blank=False)
    day_name = models.TextField(verbose_name="Название", help_text="Название", blank=True, null=True)
    schedule = models.TextField(verbose_name="Расписание", help_text="Расписание", blank=False)