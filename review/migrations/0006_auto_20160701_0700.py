# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 07:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_auto_20160701_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 1, 7, 0, 49, 72635, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]
