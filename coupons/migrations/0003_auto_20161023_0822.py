# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-23 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('coupons', '0002_coupon_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='user',
        ),
        migrations.AddField(
            model_name='coupon',
            name='users',
            field=models.ManyToManyField(to='account.Profile'),
        ),
    ]
