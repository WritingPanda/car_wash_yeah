# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash_manager', '0004_auto_20170609_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_muddy',
        ),
    ]