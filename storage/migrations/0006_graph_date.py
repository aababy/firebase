# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-05 08:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0005_auto_20180105_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 1, 5, 8, 44, 41, 866162, tzinfo=utc), verbose_name='upload date'),
            preserve_default=False,
        ),
    ]
