# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockclimb', '0009_auto_20160415_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='image',
            field=models.ImageField(blank=True, null='True', upload_to='/img'),
        ),
    ]
