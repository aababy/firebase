# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-29 08:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0014_auto_20180116_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, default='', max_length=200)),
                ('feature1', models.CharField(blank=True, default='', max_length=400)),
                ('name2', models.CharField(blank=True, default='', max_length=200)),
                ('feature2', models.CharField(blank=True, default='', max_length=400)),
                ('name3', models.CharField(blank=True, default='', max_length=200)),
                ('feature3', models.CharField(blank=True, default='', max_length=400)),
            ],
        ),
        migrations.AlterField(
            model_name='graph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 8, 11, 14, 840159, tzinfo=utc), verbose_name='upload date'),
        ),
        # migrations.AlterField(
        #     model_name='tag',
        #     name='cover',
        #     field=models.CharField(blank=True, default='', max_length=200),
        # ),
    ]
