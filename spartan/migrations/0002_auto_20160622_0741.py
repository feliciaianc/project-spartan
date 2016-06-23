# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spartan',
            old_name='contBancar',
            new_name='bank_account',
        ),
        migrations.RenameField(
            model_name='spartan',
            old_name='abilitate',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='spartan',
            old_name='nume',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='spartan',
            old_name='prenume',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='spartan',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='spartan',
            old_name='serie',
            new_name='series',
        ),
        migrations.RemoveField(
            model_name='spartan',
            name='data_nasterii',
        ),
        migrations.AddField(
            model_name='spartan',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
