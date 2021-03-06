# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-26 23:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='short_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Nombra de tu tienda'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nuestra historia'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email verificado'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Imagen de perfil'),
        ),
    ]
