# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-21 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20160922_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/%Y-%m-%d'),
        ),
    ]