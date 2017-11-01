# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class FoodType(models.Model):
    name = models.CharField(max_length=1024)
    vegeterian='VE'
    vegan='VG'
    ordinary='NO'
    foodtypes = (
        (vegeterian, 'Vegeterian'),
        (vegan, 'Vegan'),
        (ordinary, 'Ordinary')
    )
    type = models.CharField(max_length=2,choices=foodtypes,default=ordinary) 
    #diabetic ??
    pretamanger = models.BooleanField()
    class Meta:
        verbose_name="тип еды"
        verbose_name_plural="типы еды"

class UserPerson(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    rating=models.FloatField(default=0.)
    class Meta:
        verbose_name="пользователь"
        verbose_name_plural="пользователи"

class Supply(models.Model):
#    items=models.ManyToManyField(FoodInstance, related_name='supplies')
    source = models.ForeignKey(UserPerson,on_delete=models.PROTECT)
    #suggestions=models.ManyToManyField(UserSuggestion)
    date=models.DateTimeField()
    longitude=models.FloatField()
    latitude=models.FloatField()
    class Meta:
        verbose_name="поставка"
        verbose_name_plural="поставки"
        indexes=[ 
            models.Index(fields=['date',]),
            models.Index(fields=['latitude','longitude',]),
        ]

class FoodInstance(models.Model):
    type = models.ForeignKey(FoodType, on_delete=models.PROTECT)
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=1024)
    expire_date = models.DateField()
    class Meta:
        verbose_name="экземпляр еды"
        verbose_name_plural="экземпляры еды"
        indexes=[
            models.Index(fields=['expire_date',]),
        ]

class Vote(models.Model):
    user=models.ForeignKey(UserPerson)
    content_type=models.ForeignKey(ContentType)
    object_id=models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
class UserSuggestion(models.Model):
    user_id=models.ForeignKey(UserPerson, on_delete=models.PROTECT)
    supply=models.ForeignKey(Supply, on_delete=models.PROTECT)
    date=models.DateTimeField()
    longitude=models.FloatField()
    latitude=models.FloatField()
    class Meta:
        verbose_name="предложение"
        verbose_name_plural="предложения"
        indexes=[ 
            models.Index(fields=['date',]),
        ]


#maybe later
#class UserOrganization(models.Model):
#    pass
