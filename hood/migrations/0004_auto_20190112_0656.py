# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-12 06:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0003_business'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='business',
            name='user',
        ),
        migrations.DeleteModel(
            name='Business',
        ),
    ]
