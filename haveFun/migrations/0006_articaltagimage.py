# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-27 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haveFun', '0005_auto_20180224_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticalTagImage',
            fields=[
                ('image_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='ArticalTag')),
                ('uploaded_by', models.IntegerField(unique=True)),
            ],
        ),
    ]
