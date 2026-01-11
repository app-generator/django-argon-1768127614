# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    direccion = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    about_me = models.TextField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Bodega(models.Model):

    #__Bodega_FIELDS__
    producto = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    salida = models.IntegerField(null=True, blank=True)

    #__Bodega_FIELDS__END

    class Meta:
        verbose_name        = _("Bodega")
        verbose_name_plural = _("Bodega")


class Causas(models.Model):

    #__Causas_FIELDS__
    imagen = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    contenido = models.TextField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)

    #__Causas_FIELDS__END

    class Meta:
        verbose_name        = _("Causas")
        verbose_name_plural = _("Causas")


class Eventos(models.Model):

    #__Eventos_FIELDS__
    fecha = models.DateTimeField(blank=True, null=True, default=timezone.now)
    lugar = models.CharField(max_length=255, null=True, blank=True)
    lider = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    contenido = models.TextField(max_length=255, null=True, blank=True)

    #__Eventos_FIELDS__END

    class Meta:
        verbose_name        = _("Eventos")
        verbose_name_plural = _("Eventos")


class Media(models.Model):

    #__Media_FIELDS__
    tipo = models.CharField(max_length=255, null=True, blank=True)
    entity_id = models.IntegerField(null=True, blank=True)

    #__Media_FIELDS__END

    class Meta:
        verbose_name        = _("Media")
        verbose_name_plural = _("Media")


class Mensajes(models.Model):

    #__Mensajes_FIELDS__
    sender_id = models.IntegerField(null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    is_read = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Mensajes_FIELDS__END

    class Meta:
        verbose_name        = _("Mensajes")
        verbose_name_plural = _("Mensajes")


class Post(models.Model):

    #__Post_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Post_FIELDS__END

    class Meta:
        verbose_name        = _("Post")
        verbose_name_plural = _("Post")


class Comments(models.Model):

    #__Comments_FIELDS__
    post_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    replies = models.IntegerField(null=True, blank=True)

    #__Comments_FIELDS__END

    class Meta:
        verbose_name        = _("Comments")
        verbose_name_plural = _("Comments")


class Productos(models.Model):

    #__Productos_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)

    #__Productos_FIELDS__END

    class Meta:
        verbose_name        = _("Productos")
        verbose_name_plural = _("Productos")


class Testimonios(models.Model):

    #__Testimonios_FIELDS__
    content = models.TextField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Testimonios_FIELDS__END

    class Meta:
        verbose_name        = _("Testimonios")
        verbose_name_plural = _("Testimonios")



#__MODELS__END
