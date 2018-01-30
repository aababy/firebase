# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-30 02:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0021_auto_20180130_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='subscription',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 30, 2, 49, 25, 401869, tzinfo=utc), verbose_name='upload date'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='cover',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='storage.Graph'),
        ),
    ]
