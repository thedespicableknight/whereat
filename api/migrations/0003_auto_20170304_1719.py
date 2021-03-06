# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170304_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_by', models.IntegerField(default=0)),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='email_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item'),
        ),
    ]
