# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=250)),
            ],
        ),
    ]
