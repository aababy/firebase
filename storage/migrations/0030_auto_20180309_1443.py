# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-09 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0029_auto_20180302_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='graph',
            name='subscription',
            field=models.BooleanField(default=True),
        ),
    ]
