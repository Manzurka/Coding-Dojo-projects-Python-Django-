# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0002_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(max_length=255),
        ),
    ]
