# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 16:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spartan', '0001_initial'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='spartan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anunturi', to='spartan.Spartan'),
        ),
    ]
