# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-29 15:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180929_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postadd',
            old_name='img',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='postadd',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 29, 16, 22, 48, 499192)),
        ),
    ]
