# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-27 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]