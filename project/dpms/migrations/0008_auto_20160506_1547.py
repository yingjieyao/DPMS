# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-06 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpms', '0007_auto_20160506_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='user_id',
        ),
        migrations.AddField(
            model_name='user_info',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
