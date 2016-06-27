# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone



class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    market = models.CharField(('Nombre de tu tienda'), max_length=30, blank=True)
    picture = models.ImageField('Imagen de perfil',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Nuestra historia", max_length=200, blank=True, null=True,
        help_text=("Relata un poco sobre tu trabajo: cuánto tiempo llevas haciéndolo, cómo empezó, dónde nació tu creatividad, etc"))

    email_verified = models.BooleanField("Email verificado", default=False)

    class Meta:
        abstract = True

    def get_short_name(self):
        "Devuleve el nombre de la tienda"
        return self.market




@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}' Tienda". format(self.user)

#creating post model for entries.

class Post(models.Model):
    author = models.ForeignKey('authtools.User')
    title = models.CharField(max_length=400)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    


    def published(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



























