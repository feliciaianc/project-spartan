# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_announcement_spartan'),
        ('spartan', '0001_initial'),
        ('bidding', '0003_oferta_spartan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(null=True)),
                ('kind', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oferte', to='posts.Announcement')),
                ('spartan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='licitari', to='spartan.Spartan')),
            ],
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='post',
        ),
        migrations.RemoveField(
            model_name='oferta',
            name='spartan',
        ),
        migrations.DeleteModel(
            name='Oferta',
        ),
    ]
