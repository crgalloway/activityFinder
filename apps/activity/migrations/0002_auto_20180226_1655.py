# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 00:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='Lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='Long',
            new_name='lng',
        ),
    ]
