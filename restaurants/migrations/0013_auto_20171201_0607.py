# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0012_auto_20171201_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantslocations',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
