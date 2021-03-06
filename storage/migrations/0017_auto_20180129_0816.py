# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-29 08:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0016_auto_20180129_0813'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='name1',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='feature',
            old_name='url1',
            new_name='url',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='name3',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='url2',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='url3',
        ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 8, 16, 33, 565845, tzinfo=utc), verbose_name='upload date'),
        ),
    ]
