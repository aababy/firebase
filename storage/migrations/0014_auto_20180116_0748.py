# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-16 07:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0013_auto_20180112_0821'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='tag',
        #     name='cover',
        #     field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='storage.Graph'),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 16, 7, 48, 1, 112661, tzinfo=utc), verbose_name='upload date'),
        ),
    ]
