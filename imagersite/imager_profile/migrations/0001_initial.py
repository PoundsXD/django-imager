# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-21 23:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=180)),
                ('location', models.CharField(max_length=50)),
                ('commission', models.FloatField(max_length=20)),
                ('camera', models.CharField(choices=[('NikonD3300', 1), ('CanonT6i', 2), ('Canon5dMarkIII', 3)], default='1', max_length=20)),
                ('services', models.TextField(max_length=2000)),
                ('bio', models.TextField(max_length=2000)),
                ('phone', models.CharField(max_length=14)),
                ('photo_styles', models.TextField(max_length=400)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
