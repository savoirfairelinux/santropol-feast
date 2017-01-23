# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-16 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_auto_20170116_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='note.NoteCategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='note',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='note.NotePriority', verbose_name='Priority'),
        ),
    ]
