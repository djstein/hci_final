# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockclimb', '0016_remove_climb_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]
