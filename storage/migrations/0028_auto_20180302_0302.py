# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-02 03:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0027_auto_20180226_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='original_url',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 2, 3, 2, 50, 536876, tzinfo=utc), verbose_name='upload date'),
        ),
    ]