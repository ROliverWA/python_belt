# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-19 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('got_got_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='location',
            new_name='plan',
        ),
        migrations.RemoveField(
            model_name='events',
            name='date',
        ),
        migrations.RemoveField(
            model_name='events',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='events',
            name='name',
        ),
        migrations.AddField(
            model_name='events',
            name='dest',
            field=models.CharField(default='Home', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='end',
            field=models.DateField(default='2019-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='events',
            name='start',
            field=models.DateField(default='2019-01-02'),
            preserve_default=False,
        ),
    ]
