from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name="Заголовок новости", help_text="Заголовок новости",
                             max_length=80, blank=False)
    text = models.TextField(verbose_name="Текст новости", help_text="Текст новости", blank=False)
    image = models.ImageField(verbose_name="Фото", help_text="Фото", blank=True, null=True,
                              upload_to="church_api/static/imgs")
    time = models.DateTimeField(verbose_name="Дата и время публикации", blank=False,
                                help_text="Дата и время публикации")