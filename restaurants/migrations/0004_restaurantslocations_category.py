# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 04:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20171127_0432'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantslocations',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
