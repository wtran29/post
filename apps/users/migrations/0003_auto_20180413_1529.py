# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 22:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_posts',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
