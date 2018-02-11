# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-07 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haveFun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articalHeadImage',
            fields=[
                ('image_id', models.AutoField(default=1, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='artical_image')),
                ('uploaded_artical_id', models.IntegerField(unique=True)),
            ],
        ),
    ]
