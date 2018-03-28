# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-05 01:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0024_auto_20180205_0149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='image_order',
        ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 5, 1, 59, 37, 316102, tzinfo=utc), verbose_name='upload date'),
        ),
    ]
