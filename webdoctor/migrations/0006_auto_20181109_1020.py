# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-09 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webdoctor', '0005_auto_20181109_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='education',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='price',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='professionalstatement',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
