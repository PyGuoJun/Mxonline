# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-01 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20181129_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='点击数'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='fav_nums',
            field=models.IntegerField(default=0, verbose_name='收藏数'),
        ),
    ]
