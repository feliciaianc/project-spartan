# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='text',
            field=models.CharField(max_length=5000, null=True, verbose_name='Report description'),
        ),
        migrations.AlterField(
            model_name='report',
            name='username',
            field=models.CharField(max_length=20, null=True, verbose_name='Username'),
        ),
    ]
