# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dojo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='ninja',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ninja',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]