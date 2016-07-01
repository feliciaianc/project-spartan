# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
        ('spartans', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='receiver',
            field=models.ForeignKey(related_name='reviews', to='spartans.Spartan'),
        ),
        migrations.AddField(
            model_name='review',
            name='submitter',
            field=models.ForeignKey(related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
