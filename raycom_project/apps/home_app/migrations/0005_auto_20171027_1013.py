# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_delete_itemmanager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='qty',
        ),
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
