# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-18 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
