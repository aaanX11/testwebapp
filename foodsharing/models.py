# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

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
    #cooked raw

class FoodInstance(models.Model):
    type = models.ForeignKey(FoodType, on_delete=models.PROTECT)
    manufacturer = models.CharField(max_length=1024)
    expire_date = models.DateField()

class UserPerson(models.Model):
    name=models.CharField(max_length=1024, unique=True)
    email=models.EmailField()

class Supply(models.Model):
    items=models.ManyToManyField(FoodInstance)
    source = models.ForeignKey(UserPerson,on_delete=models.PROTECT)
    #suggestions=models.ManyToManyField(UserSuggestion)
    date=models.DateTimeField()
    longitude=models.FloatField()
    latitude=models.FloatField()

class UserSuggestion(models.Model):
    user_id=models.ForeignKey(UserPerson, on_delete=models.PROTECT)
    supply=models.ForeignKey(Supply, on_delete=models.PROTECT)
    date=models.DateTimeField()
    longitude=models.FloatField()
    latitude=models.FloatField()

#maybe later
#class UserOrganization(models.Model):
#    pass
