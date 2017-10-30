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

class FoodInstance(models.Model):
    type = models.ForeignKey(FoodType, on_delete=models.PROTECT)
    manufacturer = models.CharField(max_length=1024)
    expire_date = models.DateField()
    class Meta:
        indexes=[
            models.Index(fields=['expire_date',]),
        ]

class UserPerson(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    rating=models.FloatField(default=0.)
    content_type=models.ForeignKey(ContentType, related_name="content_type_history")
    object_id=models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    rating_history = models.FloatField()

class Supply(models.Model):
    items=models.ManyToManyField(FoodInstance)
    source = models.ForeignKey(UserPerson,on_delete=models.PROTECT)
    #suggestions=models.ManyToManyField(UserSuggestion)
    date=models.DateTimeField()
    longitude=models.FloatField()
    latitude=models.FloatField()
    class Meta:
        indexes=[ 
            models.Index(fields=['date',]),
            models.Index(fields=['latitude','longitude',]),
        ]


class UserSuggestion(models.Model):
    user_id=models.ForeignKey(UserPerson, on_delete=models.PROTECT)
    supply=models.ForeignKey(Supply, on_delete=models.PROTECT)
    date=models.DateTimeField()
    longitude=models.FloatField()
    latitude=models.FloatField()
    class Meta:
        indexes=[ 
            models.Index(fields=['date',]),
        ]


#maybe later
#class UserOrganization(models.Model):
#    pass
