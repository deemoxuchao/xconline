# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-12-04 00:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20181204_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='lesson',
            new_name='course',
        ),
    ]
