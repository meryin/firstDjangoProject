# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haveFun', '0003_auto_20180207_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='articalheadimage',
            name='filename',
            field=models.CharField(default='', max_length=100),
        ),
    ]