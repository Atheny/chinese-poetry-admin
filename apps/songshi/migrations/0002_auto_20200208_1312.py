# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2020-02-08 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songshi', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='songauthor',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='songshi',
            options={'managed': False},
        ),
    ]