# Generated by Django 3.1.2 on 2021-01-15 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church_api', '0002_auto_20210108_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='PraySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(help_text='Дата и день', verbose_name='Дата и день')),
                ('day_name', models.TextField(blank=True, help_text='Название', null=True, verbose_name='Название')),
                ('schedule', models.TextField(help_text='Расписание', verbose_name='Расписание')),
            ],
        ),
    ]
