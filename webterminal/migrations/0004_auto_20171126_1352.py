# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webterminal', '0003_auto_20171126_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sshlog',
            name='start_time',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
