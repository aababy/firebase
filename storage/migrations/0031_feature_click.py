# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-16 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0030_auto_20180309_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='click',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='storage.Tag'),
            preserve_default=False,
        ),
    ]
