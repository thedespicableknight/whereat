# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170304_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='city',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('1', 'Restaurant'), ('2', 'Public Place'), ('3', 'Monument')], max_length=100),
        ),
    ]
