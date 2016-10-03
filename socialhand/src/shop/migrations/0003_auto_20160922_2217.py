# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-23 03:17
from __future__ import unicode_literals

from django.db import migrations, models
import shop.storage


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, storage=shop.storage.OverwriteStorage(), upload_to='products/%Y/%m/%d'),
        ),
    ]
