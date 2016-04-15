# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rockclimb', '0007_auto_20160415_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='image',
            field=models.ImageField(blank=True, null='True', upload_to='media/img'),
        ),
        migrations.AlterField(
            model_name='climb',
            name='notes',
            field=models.TextField(default='', null='True'),
        ),
    ]
