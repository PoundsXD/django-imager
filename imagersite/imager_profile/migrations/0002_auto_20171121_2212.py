# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-21 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='website',
            field=models.CharField(max_length=180),
        ),
    ]
