# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsharing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userperson',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
