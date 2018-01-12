# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-12 07:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0009_auto_20180112_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='thumb_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='package',
            name='thumb_url',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 12, 7, 53, 17, 336203, tzinfo=utc), verbose_name='upload date'),
        ),
    ]
