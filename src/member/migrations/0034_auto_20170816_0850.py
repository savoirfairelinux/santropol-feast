# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-16 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0033_auto_20170801_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='rid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]