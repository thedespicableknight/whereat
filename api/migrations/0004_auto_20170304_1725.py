# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170304_1719'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
