# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-12 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rockclimb', '0014_auto_20160411_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='climb',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
