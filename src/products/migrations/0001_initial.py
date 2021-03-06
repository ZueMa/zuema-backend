# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=32)),
                ('price', models.FloatField()),
                ('num_stocks', models.IntegerField()),
                ('short_description', models.TextField()),
                ('full_description', models.TextField()),
                ('image', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
