# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-04 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='purchase_price',
            field=models.FloatField(),
        ),
    ]
