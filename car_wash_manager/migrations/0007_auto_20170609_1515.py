# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash_manager', '0006_auto_20170609_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterField(
            model_name='transaction',
            name='additional_charge',
            field=models.DecimalField(decimal_places=2, default=2.0, help_text='Additional cost to customer for muddy truck.', max_digits=5),
        ),
    ]