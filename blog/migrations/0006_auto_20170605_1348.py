# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170605_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='picture',
        ),
        migrations.AddField(
            model_name='post',
            name='model_pic',
            field=models.ImageField(default='blog/images/already.png', upload_to=''),
        ),
    ]
