# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-28 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0004_auto_20171128_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='commission',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
    ]