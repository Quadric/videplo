# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 21:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20160513_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='server',
            name='project',
        ),
        migrations.RemoveField(
            model_name='server',
            name='stage',
        ),
        migrations.DeleteModel(
            name='Server',
        ),
    ]
