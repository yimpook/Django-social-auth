# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]