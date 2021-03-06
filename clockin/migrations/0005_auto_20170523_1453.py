# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-23 14:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clockin', '0004_auto_20170523_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(blank=True, default=datetime.date.today, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_in',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, verbose_name='Time In'),
        ),
        migrations.AlterField(
            model_name='work',
            name='time_out',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, verbose_name='Time Out'),
        ),
    ]
