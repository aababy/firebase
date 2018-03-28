# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-29 08:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0015_auto_20180129_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='feature1',
            new_name='url1',
        ),
        migrations.RenameField(
            model_name='feature',
            old_name='feature2',
            new_name='url2',
        ),
        migrations.RenameField(
            model_name='feature',
            old_name='feature3',
            new_name='url3',
        ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 8, 13, 17, 302609, tzinfo=utc), verbose_name='upload date'),
        ),
    ]
