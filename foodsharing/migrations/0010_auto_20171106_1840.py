# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodsharing', '0009_auto_20171106_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodinstance',
            name='supply',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='foodsharing.Supply'),
        ),
        migrations.AlterField(
            model_name='usersuggestion',
            name='supply',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='foodsharing.Supply'),
        ),
    ]
