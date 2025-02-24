# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-01 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses_teacher', to='organization.Teacher', verbose_name='讲师'),
        ),
    ]
