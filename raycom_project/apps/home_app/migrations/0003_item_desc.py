# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_auto_20171027_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.CharField(default='description', max_length=255),
            preserve_default=False,
        ),
    ]