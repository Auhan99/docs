# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-10 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdoctor', '0008_city_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='pincode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
