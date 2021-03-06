# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherForecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('date', models.CharField(max_length=50)),
                ('max_temp', models.CharField(max_length=10, verbose_name='High Temperature')),
                ('min_temp', models.CharField(max_length=10, verbose_name='Low Temperature')),
                ('wind', models.CharField(max_length=10)),
                ('rain', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
