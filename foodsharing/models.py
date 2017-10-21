# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

# Create your models here.

class FoodType(models.Model):
    user1_id = models.ForeignKey('auth.User',related_name='User1')
    user2_id = models.ForeignKey('auth.User', related_name='User2')
    score = models.IntegerField()

    def score_changes():
        score=score+1
class FoodInstance(models.Model):
    text = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    def show(self):
        print 'not working yet either'

class Supply(models.Model):
    user_id = models.ForeignKey('auth.User') 
    riddle_id = models.ForeignKey(Riddle)
    show_time = models.DateTimeField(default=timezone.now)
    def check():
        print 'also not working'

class Disput(models.Model):
    pass

class UserSuggestion(models.Model):
    pass

class UserPerson(models.Model):
    pass

class UserOrganization(models.Model):
    pass
