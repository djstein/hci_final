# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-11 19:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockclimb', '0010_auto_20160411_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
