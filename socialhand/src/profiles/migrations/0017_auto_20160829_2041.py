# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-30 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_profile_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background',
            field=models.ImageField(blank=True, null=True, upload_to='profile_background/%Y-%m-%d', verbose_name='Portada'),
        ),
    ]
