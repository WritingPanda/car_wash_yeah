# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(help_text='First name of customer.', max_length=40)),
                ('last_name', models.CharField(help_text='Last name of customer.', max_length=40)),
                ('email_address', models.EmailField(help_text='Email address of customer.', max_length=255)),
                ('vehicle_type', models.CharField(choices=[('0', 'Car'), ('1', 'Truck'), ('2', 'Other')], help_text='The type of vehicle a customer drives.', max_length=1)),
                ('license_plate', models.CharField(help_text='License plate of vehicle.', max_length=10)),
                ('total_revenue', models.DecimalField(decimal_places=2, help_text='The amount of revenue from a single customer.', max_digits=8)),
                ('times_visited', models.IntegerField(help_text='Amount of times customer has been to car wash.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('car_price', models.DecimalField(decimal_places=2, help_text='Price for washing a regular car.', max_digits=4)),
                ('truck_price', models.DecimalField(decimal_places=2, help_text='Price for washing a regular truck.', max_digits=4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
