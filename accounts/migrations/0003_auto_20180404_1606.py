# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-04 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180404_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='purchase_price',
            field=models.FloatField(),
        ),
    ]